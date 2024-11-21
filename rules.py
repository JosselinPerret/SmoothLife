"""
Modules
"""
import numpy as np
from functions import (
    sigma,
    sigma_n,
    sigma_n_linearized,
    hard_threshold,
    linear_interpolation
)

"""
Règles
"""
class BasicRules:
    # On peut choisir B1, B2, D1, D2, alpha_n, alpha_m

    # Intervalle de naissance
    B1 = 0.278
    B2 = 0.365

    # Intervalle de survie
    D1 = 0.267
    D2 = 0.445

    # Largeur de transition
    alpha_n = 0.028
    alpha_m = 0.147

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown parameter: {key}")
            
    def clear(self):
        pass

    def s(self, n, m):
        """
        Fonction de transition
        """
        s = sigma(m, 0.5, self.alpha_m)
        threshold1 = linear_interpolation(self.B1, self.D1, s)
        threshold2 = linear_interpolation(self.B2, self.D2, s)
        new_health = sigma_n(n, threshold1, threshold2, self.alpha_n)
        return np.clip(new_health, 0, 1) 

class ExtensiveRules(BasicRules):
    sigmode = 0
    sigtype = 0
    mixtype = 0
    timestep_mode = 0
    dt = 0.1
    

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown parameter: {key}")
            
    # Historique pour timestep_mode 5
    esses = [None] * 3
    esses_count = 0

    def sigmoid_n(self, x, a, b):
        if self.sigtype == 0:
            return hard_threshold(x, a) * (1 - hard_threshold(x, b))
        elif self.sigtype == 1:
            return sigma_n_linearized(x, a, b, self.alpha_n)
        elif self.sigtype == 2:
            return sigma_n(x, a, b, self.alpha_n)
        else:
            raise ValueError(f"Unsupported sigtype value: {self.sigtype}")

    def sigmoid_m(self, x, y, m):
        if self.mixtype == 0:
            intermediate = hard_threshold(m, 0.5)
        elif self.mixtype == 1:
            intermediate = sigma_n_linearized(m, 0.5, self.alpha_m)
        elif self.mixtype == 2:
            intermediate = sigma(x, 0.5, self.alpha_m)
        else:
            raise ValueError(f"Unsupported mixtype value: {self.mixtype}")
        return linear_interpolation(x, y, intermediate)

    def clear(self):
        self.esses = [None] * 3
        self.esses_count = 0

    def s(self, n, m, field):
        if self.sigmode == 0:
            b_thresh = self.sigmoid_n(n, self.B1, self.B2)
            d_thresh = self.sigmoid_n(n, self.D1, self.D2)
            transition = linear_interpolation(b_thresh, d_thresh, m)
        elif self.sigmode == 1:
            b_thresh = self.sigmoid_n(n, self.B1, self.B2)
            d_thresh = self.sigmoid_n(n, self.D1, self.D2)
            transition = self.sigmoid_m(b_thresh, d_thresh, m)
        elif self.sigmode == 2:
            threshold1 = linear_interpolation(self.B1, self.D1, m)
            threshold2 = linear_interpolation(self.B2, self.D2, m)
            transition = self.sigmoid_n(n, threshold1, threshold2)
        elif self.sigmode == 3:
            threshold1 = self.sigmoid_m(self.B1, self.D1, m)
            threshold2 = self.sigmoid_m(self.B2, self.D2, m)
            transition = self.sigmoid_n(n, threshold1, threshold2)
        else:
            raise ValueError(f"Unsupported sigmode value: {self.sigmode}")

        if self.timestep_mode == 0:  # Temps discret
            nextfield = transition

        # Temps continu (à partir de l'ED)
        elif self.timestep_mode == 1:
            nextfield = field + self.dt * (2 * transition - 1)
        elif self.timestep_mode == 2:
            nextfield = field + self.dt * (transition - field)
        elif self.timestep_mode == 3:
            nextfield = m + self.dt * (2 * transition - 1)
        elif self.timestep_mode == 4:
            nextfield = m + self.dt * (transition - m)
        elif self.timestep_mode == 5:
            s0 = transition - m
            s1, s2, s3 = self.esses
            if self.esses_count == 0:
                delta = s0
            elif self.esses_count == 1:
                delta = (3 * s0 - s1) / 2
            elif self.esses_count == 2:
                delta = (23 * s0 - 16 * s1 + 5 * s2) / 12
            else:  # self.esses_count == 3:
                delta = (55 * s0 - 59 * s1 + 37 * s2 - 9 * s3) / 24
            self.esses = [s0] + self.esses[:-1]
            if self.esses_count < 3:
                self.esses_count += 1
            nextfield = field + self.dt * delta

        return np.clip(nextfield, 0, 1)