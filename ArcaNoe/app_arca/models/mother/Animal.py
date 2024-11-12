
import random
import threading

class Animal:
    def __init__(self, name, animal_type=0, hunger=False, thirst=False, size=1, sentiment=0, sex=None):
        if isinstance(animal_type, int) and animal_type in [0, 1, 2]:
            self.animal_type = animal_type
        else:
            raise ValueError("Please enter a valid type: 0 for Herbivores, 1 for Carnivores, 2 for Omnivores")

        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string")

        if isinstance(hunger, bool):
            self.hunger = hunger
        else:
            raise ValueError("Hunger must be a boolean value")

        if isinstance(thirst, bool):
            self.thirst = thirst
        else:
            raise ValueError("Thirst must be a boolean value")

        if isinstance(size, int) and size > 0:
            self.size = size
        else:
            raise ValueError("The animal size must be a positive integer")

        if sentiment in range(9):  # Expanded range to cover all valid values
            self.sentiment = sentiment
        else:
            raise ValueError("Please enter a valid sentiment: 0 for Neutral, 1 for Happy, 2 for Sad, 3 for Angry, "
                             "4 for In-love, 5 for Sleepy, 6 Afraid, 7 Territoriality, 8 Playful")

        if sex is None:
            self.sex = random.randint(0, 1)
        elif sex in [0, 1]:
            self.sex = sex
        else:
            raise ValueError("Sex must be 0 (male) or 1 (female)")
        
        self.slept = False
        self.is_alive = True
        threading.Timer(30, self.set_hunger).start()
        threading.Timer(30, self.set_thirst).start()
        threading.Timer(120, self.death).start()

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Type: {'Herbivore' if self.animal_type == 0 else 'Carnivore' if self.animal_type == 1 else 'Omnivore'}\n"
            f"Size: {self.size}\n"
            f"Sex: {'Male' if self.sex == 0 else 'Female'}\n"
            f"Feeling: {self.get_sentiment()}\n"
            f"Is Hungry: {'Yes' if self.hunger else 'No'}\n"
            f"Is Thirsty: {'Yes' if self.thirst else 'No'}"
        )

    def set_type(self, animal_type):
        if isinstance(animal_type, int) and animal_type in [0, 1, 2]:
            self.animal_type = animal_type
        else:
            raise ValueError("Please enter a valid type: 0 for Herbivores, 1 for Carnivores, 2 for Omnivores")
        
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string")

    def set_hunger(self):
        self.hunger = True
        print(f"{self.name} is hungry.")

    def set_thirst(self):
        self.thirst = True
        print(f"{self.name} is thirsty.")

    def set_sentiment(self, sentiment):
        if sentiment in range(9):  # Expanded range
            self.sentiment = sentiment
        else:
            raise ValueError("Please enter a valid sentiment: 0 for Neutral, 1 for Happy, 2 for Sad, 3 for Angry, "
                             "4 for In-love, 5 for Sleepy, 6 Afraid, 7 Territoriality, 8 Playful")

    def get_calm(self):
        self.sentiment = 0
        print(f"{self.name} has calmed down.")

    def territorial_response(self):
        self.sentiment = 7

    def death(self):
        self.is_alive = False

    def get_sentiment(self):
        if not self.is_alive:
            print(f"{self.name} is dead.")
            return None
        sentiments = ["Neutral", "Happy", "Sad", "Angry", "In-Love", "Sleepy", "Afraid", "Territoriality", "Playful"]
        return sentiments[self.sentiment]

    def is_hungry(self):
        if not self.is_alive:
            print("This animal is dead, it is not hungry.")
            return False
        return f"{self.name} is hungry" if self.hunger else f"{self.name} is not hungry"

    def is_thirsty(self):
        return f"{self.name} is thirsty" if self.thirst else f"{self.name} is not thirsty"

    def feed(self):
        if self.hunger:
            self.hunger = False
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")
        threading.Timer(5, self.set_hunger).start()

    def give_water(self):
        if not self.is_alive:
            print(f"{self.name} is dead.")
            return
        if self.thirst:
            self.thirst = False
            print(f"{self.name} has been given water.")
        else:
            print(f"{self.name} is not thirsty.")
        threading.Timer(5, self.set_thirst).start()
