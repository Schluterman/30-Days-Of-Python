#OOP
class BigObject: #class
    #code
    pass

obj1 = BigObject() #instanciate
obj2 = BigObject() #instanciate
obj3 = BigObject() #instanciate

print(type(BigObject))

class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name #attributes
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    

player1 = PlayerCharacter('Cindy',40)
player2 = PlayerCharacter('Tom',20)

print(player1.name)
print(player2.name)
print(player1.shout())

#attributes and methods 
#help(player1)#returns the bluePrint 
#EXERCISE OOP
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Peanut', 5)
cat2 = Cat('Garfield', 3)
cat3 = Cat('snickers',1)
# 2 Create a function that finds the oldest cat
def get_oldest_cat (*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")

#public vs private exp. self._name  using _ is known as  private *dont modify for method or atribute 

#dundermethod built in functions in python 

#inheritance 
#users -wizards - archers 
class user:
    def sign_in(self):
        print('logged in')

class Wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(user):
     def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
     def attack(self):
        print(f'attacking with arrows: left- {self.num_arrows}')

wizard1 = Wizard('merlin',50)
archer1 = Archer('man',40)

print(wizard1.sign_in())
wizard1.attack()

