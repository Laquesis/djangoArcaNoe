from models import Animal
from particular import meat
from models import Food
class Carnival(Animal):
    def __init__(self , name : str, hunger : bool , thirst : bool, type="Carnival"):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.type = type
        self._meat_portion_per_meal = 10
        self._water_per_drink = 0.5
    def feed(self, food : Food):
        if isinstance(food , meat) :
            if self.hunger == True:
                self.hunger = False 
                # reduce the amount of food 
        else:
            raise  "Carnivals only can eat meat"



