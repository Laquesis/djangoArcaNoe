from app_arca.models.particular.carnival import Carnival
from app_arca.models.particular.omnivore import Omnivore
from app_arca.models.particular.hervibal import Herbivore
from app_arca.models.particular.vegetables import Vegetables
from app_arca.models.particular.meat import Meat
from app_arca.models.mother.Food import Food
from app_arca.models.mother.Ark import Ark

def run_integration_test():
    print("=== INICIO DE LA SIMULACIÓN DEL ARCA ===")

    # Crear animales de diferentes tipos
    herbivore = Herbivore(name="Deer", hunger=True, thirst=True, size=3)
    carnivore = Carnival(name="Tiger", hunger=True, thirst=True, size=5)
    omnivore = Omnivore(name="Bear", hunger=True, thirst=True, size=4)

    # Crear diferentes tipos de alimentos
    vegetable = Vegetables(calorias=200)
    meat = Meat(calorias=500)

    # Inicializar el arca con capacidad limitada
    ark = Ark(max_capacity={"animal": 10, "food": 10, "water": 1000})

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

if __name__ == "__main__":
    run_integration_test()
