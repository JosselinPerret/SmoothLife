"""
Modules
"""
import numpy as np

"""
Fonctions
"""

def sigma(x, x0, alpha):
    # Fonction sigmoïde logistique sur x autour de x0 avec une largeur de transition alpha.
    return 1.0 / (1.0 + np.exp(-4.0 / alpha * (x - x0)))

def hard_threshold(x, x0):
    # Fonction de seuil sur autour de x0
    return np.greater(x, x0)

def linearized_threshold(x, x0, alpha):
    # Seuil x autour de x0 avec une région de transition linéaire alpha.
    return np.clip((x - x0) / alpha + 0.5, 0, 1) # On garde les valeurs entre 0 et 1

def gudermannian(x, x0, alpha):
    # Fonction de Gudermannian sur x autour de x0 avec une largeur de transition alpha.
    return 1.0 / np.pi * (np.arctan(np.sinh(4.0 / alpha *(x-x0))) + np.pi / 2)

def sigma_n(x, a, b, alpha):
    # Fonction logistique sur x entre a et b avec une largeur de transition alpha
    return sigma(x, a, alpha) * (1.0 - sigma(x, b, alpha))

def sigma_n_linearized(x, a, b, alpha):
    # Fonction a<x<b avec des régions de seuil linéarisées
    return linearized_threshold(x, a, alpha) * (1.0 - linearized_threshold(x, b, alpha))

def linear_interpolation(a, b, t):
    # Interpolation linéaire de a à b avec t variant de [0,1].
    return (1.0 - t) * a + t * b

