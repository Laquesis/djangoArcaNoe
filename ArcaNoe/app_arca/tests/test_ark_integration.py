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
import time

class ArkIntegrationTestCase(TestCase):
    def test_run_cyclic_integration(self):
        print("=== TEST 1===")
        print("=== INICIO DE LA SIMULACIÓN DEL ARCA ===")

        # Inicializar el arca con capacidad limitada
        ark = Ark(max_capacity={"animal": 500, "food": 1000, "water": 1000})

        # Añadir recursos iniciales
      
        # Ciclo de simulación
        cycle = 1
        animals = []
        inicio=True
        while True:
            print(f"=== Ciclo {cycle} ===")
            if inicio==True:
                for i in range(50):             
                    ark.add_food(Vegetables(name=f"vegetal{i}",calorias=200,caducidad=4))
                    ark.add_food(Meat(name=f"carne{i}",calorias=500,caducidad=2))
                for a in ark.foods:
                    print(a)
                ark.add_water(10000)
                for i in range(50):
                    if len(animals) < ark.max_capacity["animal"]:
                        new_animal_type = random.choice(["Herbivore", "Carnivore", "Omnivore"])
                        if new_animal_type == "Herbivore":
                            ark.add_animal(Herbivore(name=f"Herbivore{str(i)}", hunger=True, thirst=True,sentiment=random.randint(1, 8), size=random.randint(1, 10),sex=random.randint(0,1)))
                        elif new_animal_type == "Carnivore":
                            ark.add_animal(Carnival(name=f"Carnivore{str(i)}", hunger=True, thirst=True,sentiment=random.randint(1, 8) ,size=random.randint(1, 10),sex=random.randint(0,1)))
                        elif new_animal_type == "Omnivore":
                            ark.add_animal(Omnivore(name=f"Omnivore{str(i)}", hunger=True, thirst=True,sentiment=random.randint(1, 8), size=random.randint(1, 10),sex=random.randint(0,1)))
                        print(f"Añadido {new_animal_type}")
                inicio=False
            
            ark_status = ark.get_status()
            print("Animales en el arca:", ark_status["animals"])
            print("Comida restante en el arca:", ark_status["food"])
            print("Agua restante en el arca:", ark_status["water"])
            # Alimentar y dar de beber a los animales
            for animal in ark.animals:
                print(animal)
            for animal in ark.animals:  # Iterar sobre una copia para permitir eliminación
                ark.alimentar(animal)
                ark.dar_agua(animal)              
            ark.eliminarMuertos()
            ark.eliminarCaducados()          

            
            # Verificar estado del arca
           
            ark_status2 = ark.get_status()
            print("Animales en el arca:", ark_status2["animals"])
            print("Comida restante en el arca:", ark_status2["food"])
            print("Agua restante en el arca:", ark_status2["water"])

            # Condición de fin del ciclo
            if ark_status2["animals"]<=0 or ark_status2["food"] <= 0 or ark_status2["water"] <= 0:
                print("=== FIN DE LA SIMULACIÓN DEL ARCA ===")  
                ark.eliminarMuertos()
                ark.eliminarCaducados()   
                ark_status3 = ark.get_status()
                print("Animales en el arca:", ark_status3["animals"])
                print("Comida restante en el arca:", ark_status3["food"])
                print("Agua restante en el arca:", ark_status3["water"])
                print("=== SUPERVIVIENTES FINALES ===")
                for e in ark.animals:
                    print(e)
                print("=== FIN ===")            
                break
            
            cycle += 1
      
        
    def test_run_integration(self):
        print("=== TEST 2 ===")
        print("=== INICIO DE LA SIMULACIÓN DEL ARCA ===")

        # Inicializar el arca con capacidad limitada
        ark = Ark(max_capacity={"animal": 10, "food": 10, "water": 1000})
        
        herb = Herbivore(name="Deer",  hunger=True, thirst=True, size=3, sentiment=1, sex=0)
        carn = Carnival(name="Tiger",  hunger=True, thirst=True, size=5, sentiment=2, sex=1)
        omni = Omnivore(name="Bear",  hunger=True, thirst=True, size=4, sentiment=1, sex=0)

        # Crear diferentes tipos de alimentos
        vegetable = Vegetables(name="zanahora",calorias=200,caducidad=7)
        meat = Meat(name="pavo",calorias=500,caducidad=5)

      
        # Añadir animales al arca
        print("\n--- Añadiendo Animales al Arca ---")
        ark.add_animal(herb)
        ark.add_animal(carn)
        ark.add_animal(omni)
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
        ark.alimentar(herb)
        ark.alimentar(carn)
        ark.alimentar(omni)

        # Verificar estado de hambre
        print(f"{herb.name} está {'hambriento' if herb.hunger else 'satisfecho'}")
        print(f"{carn.name} está {'hambriento' if carn.hunger else 'satisfecho'}")
        print(f"{omni.name} está {'hambriento' if omni.hunger else 'satisfecho'}")

        # Simulación de hidratación
        print("\n--- Hidratando a los Animales ---")
        ark.dar_agua(herb)
        ark.dar_agua(carn)
        ark.dar_agua(omni)

        # Verificar estado de sed
        print(f"{herb.name} está {'sediento' if herb.thirst else 'hidratado'}")
        print(f"{carn.name} está {'sediento' if carn.thirst else 'hidratado'}")
        print(f"{omni.name} está {'sediento' if omni.thirst else 'hidratado'}")
        ark.eliminarCaducados()
        ark.eliminarMuertos()
        # Estado final del arca
        print("\n=== ESTADO FINAL DEL ARCA 2 ===")
        ark_status4 = ark.get_status()
        print("Animales en el arca:", ark_status4["animals"])
        print("Comida restante en el arca:", ark_status4["food"])
        print("Agua restante en el arca:", ark_status4["water"])
        print("=== FIN DE LA SIMULACIÓN DEL ARCA 2===")
