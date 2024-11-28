from app_arca.models.mother.Animal import Animal
from app_arca.models.particular.meat import Meat
from app_arca.models.mother.Food import Food
class Carnival(Animal):
    def __init__(self, name,  animal_type=None, hunger=None, thirst=None, size=None, sentiment=None , sex=None):
        super().__init__(name, animal_type=1, hunger=False, thirst=False, size=size, sentiment=sentiment, sex=sex)     
     
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

