#from Animal import Animal
#from Food import Food

class Ark:
    def __init__(self, animals=None, foods=None, water=None, max_capacity=None, left=False, tiempo=None):
        from app_arca.models.mother.Animal import Animal
        from app_arca.models.mother.Food import Food
        try:
            if animals is None:
                animals = []
            if foods is None:
                foods = []
            if water is None:
                water = 0
            if tiempo is None:
                tiempo = 0
            if max_capacity is None:
                max_capacity = {"animal": 100, "food": 1000, "water": 10000}

            if not isinstance(animals, list):
                raise TypeError("El atributo 'animals' debe ser una lista.")
            if not all(isinstance(animal, Animal) for animal in animals):
                raise TypeError("Todos los elementos de 'animals' deben ser instancias de la clase Animal.")

            if not isinstance(foods, list):
                raise TypeError("El atributo 'foods' debe ser una lista.")
            if not all(isinstance(food, Food) for food in foods):
                raise TypeError("Todos los elementos de 'foods' deben ser instancias de la clase Food.")
            if not isinstance(water, int):
                raise TypeError("El atributo 'water' debe ser un número entero.")
            if not isinstance(tiempo, int):
                raise TypeError("El atributo 'tiempo' debe ser un número entero.")
            if not isinstance(max_capacity, dict):
                raise TypeError("El atributo 'max_capacity' debe ser un diccionario.")
            if not isinstance(left, bool):
                raise TypeError("El atributo 'left' debe ser un valor booleano.")
            
            self.animals = animals
            self.foods = foods
            self.water = water
            self.max_capacity = max_capacity
            self.left = left
            self.tiempo = tiempo
        except TypeError as e:
            print(f"Error en la inicialización de Ark: {e}")
  

    def left_ark(self):
        try:            
            if self.left == False:
                self.left = True
                self.tiempo += 1         
        except TypeError as e:
            print(f"Error en left_ark: {e}")

    def add_animal(self, animal):
        from app_arca.models.mother.Animal import Animal
        try:
            if len(self.animals) < self.max_capacity["animal"] and not self.left:
                self.animals.append(animal)
            else:
                print("No se pueden añadir más animales.")
        except KeyError as e:
            print(f"Error en add_animal: clave no encontrada en max_capacity: {e}")
        except Exception as e:
            print(f"Error en add_animal: {e}")

    def add_food(self, food):
        try:
            if len(self.foods) < self.max_capacity["food"]:
                self.foods.append(food)
            else:
                print("No se puede añadir más comida.")
        except KeyError as e:
            print(f"Error en add_food: clave no encontrada en max_capacity: {e}")
        except Exception as e:
            print(f"Error en add_food: {e}")

    def add_water(self, water):
        try:
            if not isinstance(water, int):
                raise TypeError("El parámetro 'water' debe ser un número entero.")
            if self.water + water <= self.max_capacity["water"]:
                self.water += water
            else:
                print("No se puede añadir más agua.")
        except KeyError as e:
            print(f"Error en add_water: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_water: {e}")

    def add_multi_animal(self, list_animal):
        from app_arca.models.mother.Animal import Animal
        try:
            if not all(isinstance(animal, Animal) for animal in list_animal):
                raise TypeError("Todos los elementos de 'list_animal' deben ser instancias de la clase Animal.")
            if len(self.animals) + len(list_animal) <= self.max_capacity["animal"] and not self.left:
                self.animals.extend(list_animal)
            else:
                print("No se pueden añadir más animales.")        
        except KeyError as e:
            print(f"Error en add_multi_animal: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_multi_animal: {e}")

    def add_multi_food(self, list_food):
        from app_arca.models.mother.Food import Food
        try:            
            if not all(isinstance(food, Food) for food in list_food):
                raise TypeError("Todos los elementos de 'list_food' deben ser instancias de la clase Food.")
            if len(self.foods) + len(list_food) <= self.max_capacity["food"]:
                self.foods.extend(list_food)
            else:
                print("No se puede añadir más comida.")
        except KeyError as e:
            print(f"Error en add_multi_food: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_multi_food: {e}")

    def get_status(self):
        return {
            "animals": len(self.animals),
            "food": len(self.foods),
            "water": self.water,
            "max_capacity": self.max_capacity,
            "left": self.left
        }

    def search_list_suitable_food(food, animal_type):
        from app_arca.models.mother.Food import Food
        if not isinstance(food, Food):
            raise TypeError("El parámetro 'food' debe ser de la clase Food.")

        is_suitable = {
            0: lambda f: f.tipo == 0,    
            1: lambda f: f.tipo == 1,    
            2: lambda _: True            
        }

        return is_suitable.get(animal_type, lambda _: False)(food)
        
    def alimentar(self, animal):  
        from app_arca.models.mother.Animal import Animal
        from app_arca.models.mother.Food import Food 
   
        if not isinstance(animal, Animal):
            raise ValueError("El parámetro 'animal' debe ser una instancia válida de Animal.")
        

        if not animal.hunger:
            return None

        if len(self.foods) <= 0:
            return None

        calorias_necesarias = animal.size
        suitable_foods = [
            food for food in self.foods 
            if Ark.search_list_suitable_food(food, animal.animal_type)
        ]
        
        for food in suitable_foods[:]:
            #print(food)
            if calorias_necesarias <= 0:
                break
            if food.calorias <= calorias_necesarias:
                calorias_necesarias -= food.calorias              
                print(len(self.foods))                
                idFoodEliminar=food.id
                # Buscar el objeto con el ID coincidente
                self.foods = [food_ for food_ in self.foods if food.id != idFoodEliminar]               
            else:
                food.calorias -= calorias_necesarias
                calorias_necesarias = 0

        if calorias_necesarias > 0:
            animal.set_hunger(True)
            animal.death()            
            print(len(self.animals))                     
            print(f"{animal.name} ha muerto por falta de comida.")
        else:
            animal.set_hunger(False)
            print(f"{animal.name} se ha alimentado.")

        self.tiempo += 1
        if self.tiempo == 5:
            for alimento in self.foods:
                alimento.caducar()  
            self.tiempo = 0
   


    def caducar(self):  
        from app_arca.models.mother.Food import Food
        # Restar 1 a la caducidad de cada alimento en self.Ark.foods
        for food in self.foods:
            food.caducidad -= 1  
        

    def dar_agua(self, animal):
        if animal.thirst == True and self.water > 1:
            self.water -= 1
            animal.thirst = False   
            print(f"{animal.name} ha bebido")    
        else:
            self.water = 0
            animal.thirst = True
            animal.is_alive = False            
            print(f"{animal.name} ha muerto por falta de agua")

    def eliminarMuertos(self):
        from app_arca.models.mother.Animal import Animal
        for animal in self.animals:
            if animal.is_alive==False:
                self.animals.remove(animal)

    def eliminarCaducados(self):
        from app_arca.models.mother.Food import Food
        for food in self.foods:
            if food.caducidad==0:
                self.foods.remove(food)
