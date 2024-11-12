from django.test import TestCase
from models.mother.Animal import Animal
from models.mother.Food import Food
from models.mother import Ark  # Ajusta la importación de Ark según la ubicación de tu modelo

class ArkIntegrationTestCase(TestCase):
    def setUp(self):
        # Crear una instancia de Ark y algunos animales y alimentos
        self.ark = Ark()
        self.herbivore = Animal(name="Horse", animal_type=0, hunger=True, thirst=True, size=5)
        self.carnivore = Animal(name="Tiger", animal_type=1, hunger=True, thirst=True, size=8)
        self.omnivore = Animal(name="Bear", animal_type=2, hunger=True, thirst=True, size=7)
        
        self.vegetable_food = Food(tipo=0, calorias=300)  # Alimento vegetal para herbívoros
        self.meat_food = Food(tipo=1, calorias=500)       # Alimento de carne para carnívoros
        self.general_food = Food(tipo=2, calorias=400)    # Alimento general para omnívoros

    def test_ark_operations(self):
        # Agregar animales al arca
        self.ark.add_animal(self.herbivore)
        self.ark.add_animal(self.carnivore)
        self.ark.add_animal(self.omnivore)
        self.assertEqual(len(self.ark.animals), 3)

        # Agregar alimentos al arca
        self.ark.add_food(self.vegetable_food)
        self.ark.add_food(self.meat_food)
        self.ark.add_food(self.general_food)
        self.assertEqual(len(self.ark.foods), 3)

        # Agregar agua al arca
        self.ark.add_water(5000)
        self.assertEqual(self.ark.water, 5000)

        # Iniciar el viaje del arca
        self.ark.left_ark()
        self.assertTrue(self.ark.left)

        # Alimentar al herbívoro
        self.ark.alimentar(self.herbivore)
        self.assertFalse(self.herbivore.hunger)  # Verificar que el herbívoro ya no tiene hambre

        # Alimentar al carnívoro
        self.ark.alimentar(self.carnivore)
        self.assertFalse(self.carnivore.hunger)  # Verificar que el carnívoro ya no tiene hambre

        # Alimentar al omnívoro
        self.ark.alimentar(self.omnivore)
        self.assertFalse(self.omnivore.hunger)  # Verificar que el omnívoro ya no tiene hambre

        # Dar agua a todos los animales
        self.ark.dar_agua(self.herbivore)
        self.ark.dar_agua(self.carnivore)
        self.ark.dar_agua(self.omnivore)
        self.assertFalse(self.herbivore.thirst)
        self.assertFalse(self.carnivore.thirst)
        self.assertFalse(self.omnivore.thirst)
        
        # Verificar el estado final del arca
        final_status = self.ark.get_status()
        print("Estado final del Ark:", final_status)
        self.assertGreater(final_status["water"], 0)  # Queda algo de agua
        self.assertEqual(len(final_status["foods"]), 0)  # Todos los alimentos fueron consumidos