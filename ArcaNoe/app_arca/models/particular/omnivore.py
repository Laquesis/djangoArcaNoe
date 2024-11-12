import random
import threading
from app_arca.models.mother.Animal import Animal
from app_arca.models.mother.Food import Food

class Omnivore(Animal):
    def __init__(self, name, hunger=False, thirst=False, size=1, sentiment=0, sex=None):      
        super().__init__(name, animal_type=2, hunger=hunger, thirst=thirst, size=size, sentiment=sentiment, sex=sex)
    
    def feed(self,alimento):
        if self.hunger:
            if Food(alimento).tipo == 0:  # Alimento vegetal
                print(f"{self.name} está rumiando.")
                threading.Timer(5, self.ruminate).start()  # Comportamiento de rumiar
            elif  Food(alimento).tipo == 1:  # Alimento carne
                print(f"{self.name} está cazando.")
                threading.Timer(2, self.hunt).start()  # Comportamiento de cazar
        else:
            print(f"{self.name} no tiene hambre.")
        # Volver a tener hambre después de un tiempo
        threading.Timer(5, self.set_hunger).start()

    def ruminate(self):
        print(f"{self.name} está rumiando.")

    def hunting(self):
        print(f"{self.name} está cazando.")