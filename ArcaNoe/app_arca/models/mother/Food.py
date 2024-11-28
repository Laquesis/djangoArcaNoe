#from app_arca.models.mother.Animal import Animal
#from app_arca.models.mother.Ark import Ark
import random
import uuid

class Food:
    # Tipos de alimento
    # vegetal = 0
    # animal = 1

    def __init__(self, name, tipo=None, calorias=None, caducidad=None):
        # Validación de tipo de dato para cada atributo
        try:
            self.id=uuid.uuid1()          
            if not isinstance(name, str):
                raise TypeError("El nombre debe ser una cadena de texto.")
            self.name = name
            
            if tipo is not None and not isinstance(tipo, int):
                raise TypeError("El tipo debe ser un número entero.")
            self.tipo = tipo

            if calorias is not None and not isinstance(calorias, int):
                raise TypeError("Las calorías deben ser un número entero.")
            self.calorias = calorias

            if caducidad is not None and not isinstance(caducidad, int):
                raise TypeError("La caducidad debe ser un número entero.")
            self.caducidad = caducidad
        except TypeError as e:
            print(f"Error al crear el alimento: {e}")
    def __eq__(self, other):
        if isinstance(other, Food):  # Verifica que sea de la misma clase
            return self.id == other.id  # Comparación basada en el atributo `id`
        return False  # Si no es de la misma clase, no son iguales

    def crear_alimento(self,food):
        from app_arca.models.mother.Ark import Ark
        # Generación aleatoria de valores y validación
        try:
            if not isinstance(self.name, str):
                raise TypeError("El nombre debe ser una cadena de texto.")
            self.name = self.name

            if not isinstance(self.tipo, int):
                raise TypeError("El tipo debe ser un número entero.")
            self.tipo = int(random.randint(0, 1)) if self.tipo is None else self.tipo

            if not isinstance(self.calorias, int):
                raise TypeError("Las calorías deben ser un número entero.")
            self.calorias = int(random.randint(0, 10) )if self.calorias is None else self.calorias

            if not isinstance(self.caducidad, int):
                raise TypeError("La caducidad debe ser un número entero.")
            self.caducidad = int(random.randint(0, 10)) if self.caducidad is None else self.caducidad

            # Aquí es donde se añade el alimento a Ark
            Ark.add_food(food)
            print(f"Alimento '{self.name}' creado correctamente.")

        except TypeError as e:
            print(f"Error al crear el alimento: {e}")

    def eliminar_caducados(foods):  
        from app_arca.models.mother.Ark import Ark 
        # Restar 1 a la caducidad de cada alimento en self.Ark.foods
        for food in foods:
            food.caducidad -= 1

        # Eliminar los alimentos cuya caducidad es 0 dentro de self.Ark.foods
        Ark.foods = [food for food in foods if food.caducidad > 0]



    def __str__(self):
        # Provide string representation of the Animal object
        return (
            f"Name: {self.name}\n"
            f"Tipo: {'Vegetable' if self.tipo== 0 else 'Carne' }\n"
            f"Calorias: {self.calorias}\n"
            f"Caducidad: {self.caducidad}\n"         
        )

   
                


