from app_arca.models.mother.Food import Food
# Clase hija Vegetables
class Vegetables(Food):
    def __init__(self, name, calorias=None, caducidad=None):
        super().__init__(name, tipo=0, calorias=calorias, caducidad=caducidad)
