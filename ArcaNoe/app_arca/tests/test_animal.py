
from django.test import TestCase
from models.mother.Animal import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        # Configura un animal inicial para las pruebas
        self.animal = Animal(name="Horse", animal_type=0, hunger=True, thirst=True, size=5, sentiment=0, sex=0)

    def test_initial_attributes(self):
        # Verifica los atributos iniciales del animal
        self.assertEqual(self.animal.name, "Horse")
        self.assertEqual(self.animal.animal_type, 0)
        self.assertEqual(self.animal.hunger, True)
        self.assertEqual(self.animal.thirst, True)
        self.assertEqual(self.animal.size, 5)
        self.assertEqual(self.animal.sentiment, 0)
        self.assertEqual(self.animal.sex, 0)
        self.assertTrue(self.animal.is_alive)

    def test_set_type(self):
        # Prueba cambiar el tipo de animal
        self.animal.set_type(1)
        self.assertEqual(self.animal.animal_type, 1)

    def test_set_name(self):
        # Prueba cambiar el nombre del animal
        self.animal.set_name("Tiger")
        self.assertEqual(self.animal.name, "Tiger")

    def test_set_hunger(self):
        # Prueba activar el hambre en el animal
        self.animal.set_hunger()
        self.assertTrue(self.animal.hunger)

    def test_set_thirst(self):
        # Prueba activar la sed en el animal
        self.animal.set_thirst()
        self.assertTrue(self.animal.thirst)

    def test_set_sentiment(self):
        # Prueba cambiar el sentimiento del animal
        self.animal.set_sentimient(1)
        self.assertEqual(self.animal.sentiment, 1)

    def test_death(self):
        # Prueba el método de muerte
        self.animal.death()
        self.assertFalse(self.animal.is_alive)

    def test_get_sentiment(self):
        # Prueba obtener el sentimiento del animal
        self.animal.set_sentimient(3)
        self.assertEqual(self.animal.get_sentiment(), "Angry")

    def test_is_hungry(self):
        # Prueba verificar si el animal tiene hambre
        self.assertEqual(self.animal.is_hungry(), "Horse is hungry")

    def test_is_thirsty(self):
        # Prueba verificar si el animal tiene sed
        self.assertEqual(self.animal.is_thirsty(), "Horse is thirsty")

    def test_feed(self):
        # Prueba alimentar al animal
        self.animal.feed()
        self.assertFalse(self.animal.hunger)

    def test_water(self):
        # Prueba dar agua al animal
        self.animal.water()
        self.assertFalse(self.animal.thirst)
