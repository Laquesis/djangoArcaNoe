
import random
import threading

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
        if sentiment in range(9):
            self.sentiment = sentiment  # 0: neutral, 1: happy, 2: sad, 3: angry, 4: in-love, 5: sleepy, 6: Afraid　, 7: Territoriality , 8: Playful
        else:
            raise ValueError("Please enter a valid sentiment: 0 for Neutral, 1 for Happy, 2 for Sad, 3 for Angry,\n4 for In-love, 5 for Sleepy, 6 Afriad, 7 Territoriality, 8 Playful")


        # Set sex
        if sex is None:
            self.sex = random.randint(0, 1)  # 0: male, 1: female
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
        print(f"{self.name} is hungry.\n")


    def set_thirst(self):
        self.thirst = True
        print(f"{self.name} is thirsty.\n")


    def set_sentimient(self, sentiment):
        if sentiment in range(6):
            self.sentiment = sentiment  # 0: neutral, 1: happy, 2: sad, 3: angry, 4: in-love, 5: sleepy, 6: Afraid　, 7: Territoriality , 8: Playful
        else:
            raise ValueError("Please enter a valid sentiment: 0 for Neutral, 1 for Happy, 2 for Sad, 3 for Angry,\n4 for In-love, 5 for Sleepy, 6 Afriad, 7 Territoriality, 8 Playful")
        
    
    def get_calm(self):
        self.sentiment = 0
        print(f"{self.name} has calmed down.\n")
    

    def territorial_response(self):
        self.sentiment = 6
   

    def death(self):
        self.is_alive = False

    
    def get_sentiment(self):
        if not self.is_alive:
            print(f"{self.name} is death.\n")
            return None
        # Translate sentiment code to text
        sentiments = ["Neutral", "Happy", "Sad", "Angry", "In-Love", "Sleepy" ,"Afraid", "Territoriality" , "Playful" ]
        return sentiments[self.sentiment]


    def is_hungry(self):
         if not self.is_alive:
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
        if self.is_alive == False:
            print(f"{self.name} is death.")
            return
        if self.thirst:
            self.thirst = False
            print(f"{self.name} has been given water.")
        else:
            print(f"{self.name} is not thirsty.")
        threading.Timer(5 , self.set_thirst).start()

    def instinctive_reaction(self, animal):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot react.")
            return

        # Set reactions based on animal type
        if self.animal_type == 0:  # Herbivore
            if animal.animal_type in [1, 2]:  # Carnivore or Omnivore
                self.sentiment = 6  # Afraid
                animal.sentiment = 3  # Angry
            elif animal.animal_type == 0:
                self.sentiment = 8  # Playful
                animal.sentiment = 8  # Playful

        elif self.animal_type == 1:  # Carnivore
            if animal.animal_type == 2:
                self.sentiment = 7  # Territoriality
                animal.sentiment = 7  # Territoriality
            elif animal.animal_type == 0:
                self.sentiment = 3  # Angry
                animal.sentiment = 6  # Afraid
            elif animal.animal_type == 1:
                self.sentiment = 7  # Territoriality
                animal.sentiment = 7  # Territoriality

        elif self.animal_type == 2:  # Omnivore
            if animal.animal_type == 0:
                self.sentiment = 3  # Angry
                animal.sentiment = 6  # Afraid
            elif animal.animal_type == 1:
                self.sentiment = 7  # Territoriality
                animal.sentiment = 7  # Territoriality
            elif animal.animal_type == 2:
                self.sentiment = 7  # Territoriality
                animal.sentiment = 7  # Territoriality

                
    def have_a_baby(self , animal):
        if (self.name == animal.name) and (self. sex != animal.sex) :
            baby_animal = Animal(self.name , animal_type= self.animal_type , sex = random.randint(0,1), hunger= True , thirst= True)
            return baby_animal