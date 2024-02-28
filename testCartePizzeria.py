import unittest
from unittest.mock import MagicMock, patch
from cartePizzeria import CartePizzeria
from cartePizzeriaException import CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        # Création de quelques pizzas fictives pour les tests
        self.mock_pizza1 = MagicMock(name="Pizza 1")
        self.mock_pizza2 = MagicMock(name="Pizza 2")

    def test_is_empty(self):
        # Teste si la méthode is_empty retourne True pour une carte vide
        carte_pizzeria = CartePizzeria()
        self.assertTrue(carte_pizzeria.is_empty())

        # Teste si la méthode is_empty retourne False lorsque des pizzas sont ajoutées
        carte_pizzeria.add_pizza(self.mock_pizza1)
        self.assertFalse(carte_pizzeria.is_empty())

    def test_nb_pizzas(self):
        # Teste si la méthode nb_pizzas retourne le nombre correct de pizzas
        carte_pizzeria = CartePizzeria()
        self.assertEqual(carte_pizzeria.nb_pizzas(), 0)

        # Ajout de deux pizzas fictives et vérification du nombre
        carte_pizzeria.add_pizza(self.mock_pizza1)
        carte_pizzeria.add_pizza(self.mock_pizza2)
        self.assertEqual(carte_pizzeria.nb_pizzas(), 2)

    def test_add_pizza(self):
        # Teste si la méthode add_pizza ajoute correctement une pizza à la carte
        carte_pizzeria = CartePizzeria()
        carte_pizzeria.add_pizza(self.mock_pizza1)
        self.assertIn(self.mock_pizza1, carte_pizzeria.pizzas)

    @patch('cartePizzeria.CartePizzeriaException')
    def test_remove_pizza(self, mock_exception):
        # Teste si la méthode remove_pizza supprime correctement une pizza de la carte
        carte_pizzeria = CartePizzeria()

        # Ajout de quelques pizzas fictives
        carte_pizzeria.add_pizza(self.mock_pizza1)
        carte_pizzeria.add_pizza(self.mock_pizza2)

        # Suppression d'une pizza existante
        carte_pizzeria.remove_pizza(self.mock_pizza1.name)
        self.assertNotIn(self.mock_pizza1, carte_pizzeria.pizzas)

        # Suppression d'une pizza qui n'existe pas
        with self.assertRaises(CartePizzeriaException):
            carte_pizzeria.remove_pizza("Pizza inexistante")

        # Vérification que l'exception est bien levée
        mock_exception.assert_called_with("Pizza 'Pizza inexistante' not found in the menu")

if __name__ == '__main__':
    unittest.main()