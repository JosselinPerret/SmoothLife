
import unittest
import numpy as np
from functions import (
    sigma,
    hard_threshold,
    linearized_threshold,
    sigma_n,
    linear_interpolation,
    gudermannian,
)
from calculations import Fourier_masque, masque_cercle_flou
from rules import BasicRules, ExtensiveRules
from smoothlife import SmoothLife, show_animation

"""
TDD - Test Driven Development
"""

class TestSmoothLife(unittest.TestCase):

    def test_sigma(self):
        # Test de la fonction sigmoïde
        self.assertAlmostEqual(sigma(0.5, 0.5, 0.1), 0.5, delta=0.01)
        self.assertGreater(sigma(0.6, 0.5, 0.1), 0.5)
        self.assertLess(sigma(0.4, 0.5, 0.1), 0.5)

    def test_hard_threshold(self):
        # Test de la fonction de seuil dur
        self.assertEqual(hard_threshold(0.6, 0.5), True)
        self.assertEqual(hard_threshold(0.4, 0.5), False)

    def test_linearized_threshold(self):
        # Test du seuil linéarisé
        self.assertAlmostEqual(linearized_threshold(0.5, 0.5, 0.1), 0.5, delta=0.01)
        self.assertEqual(linearized_threshold(0.6, 0.5, 0.1), 1.0)
        self.assertEqual(linearized_threshold(0.4, 0.5, 0.1), 0.0)

    def test_gudermannian(self):
        # Test de la fonction de Gudermann
        self.assertAlmostEqual(gudermannian(0.5, 0.5, 0.1), 0.5, delta=0.01)

    def test_sigma_n(self):
        # Test de la fonction logistique entre deux seuils
        result = sigma_n(0.35, 0.2, 0.4, 0.1)
        self.assertGreater(result, 0.0)
        self.assertLess(result, 1.0)

    def test_linear_interpolation(self):
        # Test de l'interpolation linéaire
        self.assertEqual(linear_interpolation(0, 1, 0.5), 0.5)
        self.assertEqual(linear_interpolation(0, 1, 0.0), 0.0)
        self.assertEqual(linear_interpolation(0, 1, 1.0), 1.0)

    def test_masque_cercle_flou(self):
        # Test de la génération du masque flou
        mask = masque_cercle_flou((256, 256), 50)
        self.assertEqual(mask.shape, (256, 256))
        self.assertGreater(mask.sum(), 0)

    def test_Fourier_masque(self):
        # Test des masques Fourier
        fourier_mask = Fourier_masque((256, 256), 7, 21)
        self.assertEqual(fourier_mask.M.shape, (256, 256))
        self.assertEqual(fourier_mask.N.shape, (256, 256))

    def test_BasicRules(self):
        # Test des règles de transition basiques
        rules = BasicRules(B1=0.2, B2=0.3, D1=0.1, D2=0.4, alpha_n=0.05, alpha_m=0.15)
        n, m = 0.3, 0.4
        field = 0.5
        result = rules.s(n, m)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)

    def test_ExtensiveRules(self):
        # Test des règles de transition extensives
        rules = ExtensiveRules(B1=0.2, B2=0.3, D1=0.1, D2=0.4, alpha_n=0.05, alpha_m=0.15, sigmode=2, sigtype=2, mixtype=2, timestep_mode=0, dt=0.1)
        n, m = 0.3, 0.4
        field = 0.5
        result = rules.s(n, m, field)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)

    def test_SmoothLife_initialization(self):
        # Test de l'initialisation de SmoothLife
        sl = SmoothLife(256, 256, 0.2, 0.3, 0.1, 0.4, 0.05, 0.15, 7, 21, 2, 2, 2, 0, 0.1)
        self.assertEqual(sl.field.shape, (256, 256))

    def test_SmoothLife_step(self):
        # Test d'une étape dans SmoothLife
        sl = SmoothLife(256, 256, 0.2, 0.3, 0.1, 0.4, 0.05, 0.15, 7, 21, 2, 2, 2, 0, 0.1)
        initial_state = np.copy(sl.field)
        new_state = sl.step()
        self.assertEqual(new_state.shape, (256, 256))
        self.assertFalse(np.array_equal(initial_state, new_state))

    def test_add_speckles(self):
        # Test de l'ajout de speckles
        sl = SmoothLife(256, 256, 0.2, 0.3, 0.1, 0.4, 0.05, 0.15, 7, 21, 2, 2, 2, 0, 0.1)
        sl.add_speckles(count=10, intensity=1)
        self.assertGreater(sl.field.sum(), 0)

    def test_show_animation(self):
        # Test de la fonction d'animation
        try:
            show_animation(resolution=(256, 256), cmap='viridis', speed=60)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"show_animation a levé une exception: {e}")

if __name__ == '__main__':
    unittest.main()
# coverage : python -m pytest --cov=. --cov-report html test.py