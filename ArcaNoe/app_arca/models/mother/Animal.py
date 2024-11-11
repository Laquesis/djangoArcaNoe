import random
import threading
import time

class Animal:
    def __init__(self, name, animal_type=0, hunger=False, thirst=False, size=1, sentiment=0, sex=None):
        # Validate type
        if isinstance(animal_type, int) and animal_type in [0, 1, 2]:
            self.animal_type = animal_type
        else:
            raise ValueError("Please enter a valid type: 0 for Herbivores, 1 for Carnivores, 2 for Omnivores")

        # Validate name
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string")

        # Set hunger and thirst as booleans
        if isinstance(hunger, bool):
            self.hunger = hunger
        else:
            raise ValueError("Hunger must be a boolean value")

        if isinstance(thirst, bool):
            self.thirst = thirst
        else:
            raise ValueError("Thirst must be a boolean value")

        # Validate size
        if isinstance(size, int) and size > 0:
            self.size = size
        else:
            raise ValueError("The animal size must be a positive integer")

        # Validate sentiment
        if sentiment in range(6):
            self.sentiment = sentiment  # 0: neutral, 1: happy, 2: sad, 3: angry, 4: in-love, 5: sleepy
        else:
            raise ValueError("Please enter a valid sentiment: 0 for neutral, 1 for happy, 2 for sad, 3 for angry, 4 for in-love, 5 for sleepy")

        # Set sex
        if sex is None:
            self.sex = random.randint(0, 1)  # 0: male, 1: female
        elif sex in [0, 1]:
            self.sex = sex
        else:
            raise ValueError("Sex must be 0 (male) or 1 (female)")

        self.is_alive = True
        threading.Timer(30, self.set_hunger).start()
        threading.Timer(30, self.set_thirst).start()
        threading.Timer(120, self.death).start()

    def __str__(self):
        # Provide string representation of the Animal object
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
        

    def set_name(self ,name):
        if isinstance(name, str):
            self.name = name
        else:
           raise ValueError("Name must be a string")
        
        
    def set_hunger(self):
        self.hunger = True
        print(f"{self.name} is hungry again")


    def set_thirst(self):
        self.thirst = True
        print(f"{self.name} is thirsty again")


    def set_sentimient(self, sentiment):
        if sentiment in range(6):
            self.sentiment = sentiment  # 0: neutral, 1: happy, 2: sad, 3: angry, 4: in-love, 5: sleepy
        else:
            raise ValueError("Please enter a valid sentiment: 0 for neutral, 1 for happy, 2 for sad, 3 for angry, 4 for in-love, 5 for sleepy")
        

    def death(self):
        self.is_alive = False

    
    def get_sentiment(self):
        if not self.is_alive:
            print(f"{self.name} is death")
            return None
        # Translate sentiment code to text
        sentiments = ["Neutral", "Happy", "Sad", "Angry", "In-Love", "Sleepy"]
        return sentiments[self.sentiment]

    def is_hungry(self):
         if not animal.is_alive:
             print("this animal is death, It is not hungry")
             return False
         return(f"{self.name} is not hungry" if self.hunger == False else f"{self.name} is hungry" )
   
   
    def is_thirsty(self):
       return(f"{self.name} is not thirsty" if self.thirst == False else f"{self.name} is thirsty" )


    def feed(self):
        if self.hunger:
            self.hunger = False
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")
        threading.Timer(5, self.set_hunger).start()

    def water(self):
        if self.thirst:
            self.thirst = False
            print(f"{self.name} has been given water.")
        else:
            print(f"{self.name} is not thirsty.")
        threading.Timer(5 , self.set_thirst).start()


# Instantiate and print an animal object
animal = Animal(name="Horse", animal_type=0)



print(animal.is_hungry())
print(animal.is_thirsty())


animal.feed()


time.sleep(10)

print(animal.is_hungry())
print(animal.is_thirsty())