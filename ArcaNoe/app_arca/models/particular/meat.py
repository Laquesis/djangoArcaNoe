from mother.Food import Food
# Clase hija Meat
class Meat(Food):
    def __init__(self, name, calorias=None, caducidad=None):
        super().__init__(name, tipo=1, calorias=calorias, caducidad=caducidad)