from django.test import TestCase
from app_arca.models.particular.carnival import Carnival
from app_arca.models.particular.omnivore import Omnivore
from app_arca.models.particular.hervibal import Herbivore
from app_arca.models.particular.vegetables import Vegetables
from app_arca.models.particular.meat import Meat
from app_arca.models.mother.Food import Food
from app_arca.models.mother.Ark import Ark
from app_arca.models.mother.Animal import Animal
import random

class ArkIntegrationTestCase(TestCase):
    def test_run_cyclic_integration(self):
        print("=== TEST 1===")
        print("=== INICIO DE LA SIMULACIÓN DEL ARCA ===")

        # Inicializar el arca con capacidad limitada
        ark = Ark(max_capacity={"animal": 10, "food": 10, "water": 1000})

        # Añadir recursos iniciales
        ark.add_food(Vegetables(name="zanahoria",calorias=200,caducidad=4))
        ark.add_food(Meat(name="pavo",calorias=500,caducidad=2))
        ark.add_water(500)
        
        # Ciclo de simulación
        cycle = 1
        animals = []
        while True:
            print(f"=== Ciclo {cycle} ===")
            
            # Generar nuevos animales aleatoriamente si hay espacio
            if len(animals) < ark.max_capacity["animal"]:
                new_animal_type = random.choice(["Herbivore", "Carnivore", "Omnivore"])
                if new_animal_type == "Herbivore":
                    animals.append(Herbivore(name=f"Herbivore{cycle}", hunger=True, thirst=True,sentiment=random.randint(1, 8), size=random.randint(1, 10),sex=random.randint(0,1)))
                elif new_animal_type == "Carnivore":
                    animals.append(Carnival(name=f"Carnivore{cycle}", hunger=True, thirst=True,sentiment=random.randint(1, 8) ,size=random.randint(1, 10),sex=random.randint(0,1)))
                elif new_animal_type == "Omnivore":
                    animals.append(Omnivore(name=f"Omnivore{cycle}", hunger=True, thirst=True,sentiment=random.randint(1, 8), size=random.randint(1, 10),sex=random.randint(0,1)))
                print(f"Añadido {new_animal_type}")

            # Alimentar y dar de beber a los animales
            for animal in animals[:]:  # Iterar sobre una copia para permitir eliminación
                ark.alimentar(animal)
                ark.dar_agua(animal)
                # Eliminar animales que no sobrevivieron por falta de recursos
                if animal.hunger or animal.thirst:
                    print(f"{animal.name} ha muerto por falta de recursos")
                    animals.remove(animal)
            
            # Verificar estado del arca
            ark_status = ark.get_status()
            print("Animales en el arca:", ark_status["animals"])
            print("Comida restante en el arca:", ark_status["food"])
            print("Agua restante en el arca:", ark_status["water"])

            # Condición de fin del ciclo
            if not animals or ark_status["food"] <= 0 or ark_status["water"] <= 0:
                print("=== FIN DE LA SIMULACIÓN DEL ARCA ===")
                break
            
            cycle += 1
    def test_run_integration(self):
        print("=== TEST 2 ===")
        print("=== INICIO DE LA SIMULACIÓN DEL ARCA ===")

        # Inicializar el arca con capacidad limitada
        ark = Ark(max_capacity={"animal": 10, "food": 10, "water": 1000})
        
        herbivore = Animal(name="Deer", animal_type=0, hunger=True, thirst=True, size=3, sentiment=1, sex=0)
        carnivore = Animal(name="Tiger", animal_type=1, hunger=True, thirst=True, size=5, sentiment=2, sex=1)
        omnivore = Animal(name="Bear", animal_type=2, hunger=True, thirst=True, size=4, sentiment=1, sex=0)

        # Crear diferentes tipos de alimentos
        vegetable = Vegetables(name="zanahora",calorias=200,caducidad=7)
        meat = Meat(name="pavo",calorias=500,caducidad=5)

      
        # Añadir animales al arca
        print("\n--- Añadiendo Animales al Arca ---")
        ark.add_animal(herbivore)
        ark.add_animal(carnivore)
        ark.add_animal(omnivore)
        print("Animales actuales en el arca:", ark.get_status()["animals"])

        # Añadir alimentos al arca
        print("\n--- Añadiendo Alimentos al Arca ---")
        ark.add_food(vegetable)
        ark.add_food(meat)
        print("Cantidad actual de comida en el arca:", ark.get_status()["food"])

        # Añadir agua al arca
        print("\n--- Añadiendo Agua al Arca ---")
        ark.add_water(500)
        print("Cantidad actual de agua en el arca:", ark.get_status()["water"])

        # Simulación de alimentación
        print("\n--- Alimentando a los Animales ---")
        ark.alimentar(herbivore)
        ark.alimentar(carnivore)
        ark.alimentar(omnivore)

        # Verificar estado de hambre
        print(f"{herbivore.name} está {'hambriento' if herbivore.hunger else 'satisfecho'}")
        print(f"{carnivore.name} está {'hambriento' if carnivore.hunger else 'satisfecho'}")
        print(f"{omnivore.name} está {'hambriento' if omnivore.hunger else 'satisfecho'}")

        # Simulación de hidratación
        print("\n--- Hidratando a los Animales ---")
        ark.dar_agua(herbivore)
        ark.dar_agua(carnivore)
        ark.dar_agua(omnivore)

        # Verificar estado de sed
        print(f"{herbivore.name} está {'sediento' if herbivore.thirst else 'hidratado'}")
        print(f"{carnivore.name} está {'sediento' if carnivore.thirst else 'hidratado'}")
        print(f"{omnivore.name} está {'sediento' if omnivore.thirst else 'hidratado'}")

        # Estado final del arca
        print("\n=== ESTADO FINAL DEL ARCA ===")
        print("Animales en el arca:", ark.get_status()["animals"])
        print("Comida restante en el arca:", ark.get_status()["food"])
        print("Agua restante en el arca:", ark.get_status()["water"])
        print("=== FIN DE LA SIMULACIÓN DEL ARCA ===")
