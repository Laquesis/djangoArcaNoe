import random
import threading
from app_arca.models.mother.Animal import Animal

class Herbivore(Animal):
    def __init__(self, name, hunger=False, thirst=False, size=1, sentiment=0, sex=None):      
        super().__init__(name, animal_type=0, hunger=hunger, thirst=thirst, size=size, sentiment=sentiment, sex=sex)
    
    def feed(self):
        if self.hunger:
            self.hunger = False
            print(f"{self.name}  está rumiando.")
            # Simular el comportamiento de rumiar después de alimentarse
            threading.Timer(3, self.ruminate).start()
        else:
            print(f"{self.name} no tiene hambre.")
        # Volver a tener hambre después de un tiempo
        threading.Timer(5, self.set_hunger).start()

    def ruminate(self):
        print(f"{self.name} está rumiando.")
