"""
Modules
"""
import json 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from rules import BasicRules, ExtensiveRules
from calculations import Fourier_masque
from parameters import get_user_input


""" 
Animation et sauvegarde de l'animation
"""

def show_animation(resolution=(256,256), cmap='viridis', speed=1, B1=0.278, B2=0.365, D1=0.267, D2=0.445, alpha_n=0.028, alpha_m=0.147, count=None, intensity=1,inner_radius=7, outer_radius=21 , sigmode = 2, sigtype = 2, mixtype = 2, timestepmode = 0, dt = 0.1, glider=False, save=False,): 
    w, h = resolution
    sl = SmoothLife(h, w, B1, B2, D1, D2, alpha_n, alpha_m, inner_radius, outer_radius, sigmode, sigtype, mixtype, timestepmode, dt)
    sl.add_speckles(count, intensity, glider, save)
    sl.step()
    fig = plt.figure()
    im = plt.imshow(
        sl.field, animated=True, cmap=plt.get_cmap(cmap), aspect="equal"
    )

    def animate(*args):
        im.set_array(sl.step())
        return (im,)

    ani = animation.FuncAnimation(fig, animate, interval=speed, blit=True)
    plt.show()

"""
Main
"""
class SmoothLife:
    def __init__(self, height, width, B1, B2, D1, D2, alpha_n, alpha_m, inner_radius, outer_radius, sigmode, sigtype, mixtype, timestep_mode, dt):
        self.width = width
        self.height = height
        self.B1 = B1
        self.B2 = B2
        self.D1 = D1
        self.D2 = D2
        self.alpha_n = alpha_n
        self.alpha_m = alpha_m
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.sigmode = sigmode
        self.sigtype = sigtype
        self.mixtype = mixtype
        self.timestep_mode = timestep_mode
        self.dt = dt

        self.fourier_masque = Fourier_masque((height, width), self.inner_radius, self.outer_radius)
        self.rules = BasicRules(B1 = self.B1, B2 = self.B2, D1 = self.D1, D2 = self.D2, alpha_n = self.alpha_n, alpha_m = self.alpha_m)
        self.rules = ExtensiveRules(B1 = self.B1, B2 = self.B2, D1 = self.D1, D2 = self.D2, alpha_n = self.alpha_n, alpha_m = self.alpha_m, sigmode = self.sigmode, sigtype = self.sigtype, mixtype = self.mixtype, timestep_mode = self.timestep_mode, dt = self.dt)
        self.clear()

    def clear(self):
        self.field = np.zeros((self.height, self.width))
        self.rules.clear()

    def step(self):
        # Pour sommer les voisins, faire des convolutions en multipliant dans le domaine fréquentiel et en revenant au domaine spatial
        field_ = np.fft.fft2(self.field) # Transformée de Fourier 
        M_buffer_ = field_ * self.fourier_masque.M # Produit de convolution
        N_buffer_ = field_ * self.fourier_masque.N # Produit de convolution
        M_buffer = np.real(np.fft.ifft2(M_buffer_)) # Retour au domaine spatial
        N_buffer = np.real(np.fft.ifft2(N_buffer_)) # Retour au domaine spatial

        # Appliquer les règles de transition
        self.field = self.rules.s(N_buffer, M_buffer, field_)
        return self.field

    def add_speckles(self, count=None, intensity=1, glider=False, save=False):
        # Remplie le champ avec des taches aléatoires
        if count is None:
            count = int(
                self.width * self.height / ((self.fourier_masque.OUTER_RADIUS * 2) ** 2)
            )
        radius = int(self.fourier_masque.OUTER_RADIUS)
        
        if glider:
            with open('glider_field.json', 'r') as f:
                self.field = json.load(f)
        
        else:
            for i in range(count):
                r = np.random.randint(0, self.height - radius)
                c = np.random.randint(0, self.width - radius)
                self.field[r : r + radius, c : c + radius] = intensity
        if save:
            with open('field.json', 'w') as f:
                json.dump(self.field.tolist(), f)


"""
Main
"""

if __name__ == "__main__":
    user_input = get_user_input()
    resolution = tuple(map(int, user_input[0].split(',')))
    show_animation(resolution, *user_input[1:])

"""
Jeu de base
python smoothlife.py --resolution "256,256" --cmap "viridis" --speed 60 --B1 0.278 --B2 0.365 --D1 0.267 --D2 0.445 --alpha_n 0.028 --alpha_m 0.147 --count 100 --intensity 1 --inner_radius 7 --outer_radius 21
python smoothlife.py --resolution "256,256" --cmap "binary" --speed 60 --B1 0.278 --B2 0.365 --D1 0.267 --D2 0.445 --alpha_n 0.028 --alpha_m 0.147 --count 100 --intensity 1 --inner_radius 7 --outer_radius 21

Jeu de base avec planeur
python smoothlife.py --resolution "256,256" --cmap "viridis" --speed 60 --B1 0.278 --B2 0.365 --D1 0.267 --D2 0.445 --alpha_n 0.028 --alpha_m 0.147 --count 100 --intensity 1  --inner_radius 7 --outer_radius 21 --glider

Jeu de base avec paramètres différents - structure stable
python smoothlife.py --resolution "256,256" --cmap "viridis" --speed 60 --B1 0.258 --B2 0.310 --D1 0.180 --D2 0.440 --alpha_n 0.030 --alpha_m 0.127 --intensity 1 --inner_radius 7 --outer_radius 21

Jeu de base avec paramètres différents - structure stable
python smoothlife.py --resolution "256,256" --cmap "gnuplot" --speed 60 --B1 0.258 --B2 0.310 --D1 0.010 --D2 0.740 --alpha_n 0.030 --alpha_m 0.127 --intensity 1 --inner_radius 6 --outer_radius 6.6
"""