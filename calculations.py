
"""
Modules
"""
import numpy as np
import math

"""
Calculs
"""
def masque_cercle_flou(size, radius, log_res=None):
    # Crée un cercle avec des bords flous
    # Définir roll=False pour centrer le cercle au milieu de la matrice. Par défaut, il est centré aux extrémités (meilleur pour la convolution).
    y, x = size
    yy, xx = np.mgrid[:y, :x] # Coordonnées de chaque point
    radiuses = np.sqrt((xx - x / 2) ** 2 + (yy - y / 2) ** 2) # Distance entre les points et le centre
    if log_res is None:
        log_res = math.log(min(*size), 2) # Largeur du flou (base 2 plus simple pour les calculs car la résolution est souvent une puissance de 2)
    with np.errstate(over="ignore"): # Ignore les erreurrs d'infini
        logistic = 1 / (1 + np.exp(log_res * (radiuses - radius)))
    logistic = np.roll(logistic, y // 2, axis=0)
    logistic = np.roll(logistic, x // 2, axis=1)
    # Permet d'avoir une périodicité qui facilite la convolution, il est plus facile de faire la transformée de Fourier d'une fonction périodique (série de Fourier)
    return logistic

class Fourier_masque:
    INNER_RADIUS = 7.0
    OUTER_RADIUS = INNER_RADIUS * 3.0

    def __init__(self, size, inner_radius=INNER_RADIUS, outer_radius=OUTER_RADIUS):
        inner = masque_cercle_flou(size, inner_radius)
        outer = masque_cercle_flou(size, outer_radius)
        annulus = outer - inner

        # Normalise
        inner /= np.sum(inner)
        annulus /= np.sum(annulus)

        # Précalcule les FFT
        self.M = np.fft.fft2(inner)
        self.N = np.fft.fft2(annulus)
