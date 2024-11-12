from app_arca.models.mother.Animal import Animal
from app_arca.models.particular.meat import Meat
from app_arca.models.mother.Food import Food
class Carnival(Animal):
    def __init__(self , name : str, hunger : bool , thirst : bool,size:int, type=1):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.type = type
        self._meat_portion_per_meal = 10
        self._water_per_drink = 0.5
    def feed(self, food : Food):
        if isinstance(food , Meat) :
            if self.hunger == True:
                self.hunger = False 
                # reduce the amount of food 
        else:
            raise  "Carnivals only can eat meat"
    def cazar(self, animal:Animal):
        if animal.animal_type not in [0,2]:
            print(f"{self.name} cannot hunt {animal.name}")
        else:
            self.set_hunger(False)
            animal.is_alive = False
#lion = Carnival(name="Lion" , hunger= True)
#rabit = Animal(name="Rabit" , type=0)
#lion.cazar(rabit)


