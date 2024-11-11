
from django.test import TestCase
from models.mother.Animal import Animal
from models.mother.Food import Food
from models import Ark  # Ajusta la importación de Ark según esté en tu proyecto

class ArkTestCase(TestCase):
    def setUp(self):
        # Configura el objeto inicial de prueba Ark
        self.ark = Ark()

    def test_initial_status(self):
        # Prueba el estado inicial de Ark
        self.assertEqual(self.ark.get_status(), {
            "animals": 0,
            "food": 0,
            "water": 0,
            "max_capacity": {"animal": 100, "food": 1000, "water": 10000},
            "left": False
        })

    def test_add_animal(self):
        # Prueba agregar un solo animal
        herbivore = Animal(tipo=0, size=5)
        self.ark.add_animal(herbivore)
        self.assertEqual(len(self.ark.animals), 1)

    def test_add_food(self):
        # Prueba agregar un solo alimento
        vegetal = Food(tipo=0, calorias=200)
        self.ark.add_food(vegetal)
        self.assertEqual(len(self.ark.foods), 1)

    def test_add_water(self):
        # Prueba agregar agua
        self.ark.add_water(3000)
        self.assertEqual(self.ark.water, 3000)

    def test_add_multi_animal(self):
        # Prueba agregar varios animales
        animals_to_add = [Animal(tipo=1, size=10), Animal(tipo=2, size=8)]
        self.ark.add_multi_animal(animals_to_add)
        self.assertEqual(len(self.ark.animals), 2)

    def test_add_multi_food(self):
        # Prueba agregar varios alimentos
        foods_to_add = [Food(tipo=1, calorias=500), Food(tipo=0, calorias=150)]
        self.ark.add_multi_food(foods_to_add)
        self.assertEqual(len(self.ark.foods), 2)

    def test_left_ark(self):
        # Prueba iniciar el viaje del arca
        self.ark.left_ark()
        self.assertTrue(self.ark.left)

    def test_alimentar_animal(self):
        # Prueba alimentar un animal
        herbivore = Animal(tipo=0, size=5, hunger=True)
        vegetal = Food(tipo=0, calorias=200)
        self.ark.add_animal(herbivore)
        self.ark.add_food(vegetal)
        self.ark.alimentar(herbivore)
        self.assertFalse(herbivore.hunger)

    def test_dar_agua(self):
        # Prueba dar agua a un animal
        herbivore = Animal(tipo=0, size=5, thirst=True)
        self.ark.add_animal(herbivore)
        self.ark.add_water(5000)
        self.ark.dar_agua(herbivore)
        self.assertFalse(herbivore.thirst)
        self.assertEqual(self.ark.water, 4995)  # 5000 - 5 de tamaño del animal
