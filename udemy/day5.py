#OOP
# class BigObject: #class
#     #code
#     pass

# obj1 = BigObject() #instanciate
# obj2 = BigObject() #instanciate
# obj3 = BigObject() #instanciate

# print(type(BigObject))

# class PlayerCharacter:
#     #Class Object Attribute
#     membership = True
#     def __init__(self, name='anonymous', age=0):
#         if (age > 18):
#             self.name = name #attributes
#             self.age = age
#     def shout(self):
#         print(f'my name is {self.name}')
    

# player1 = PlayerCharacter('Cindy',40)
# player2 = PlayerCharacter('Tom',20)

# print(player1.name)
# print(player2.name)
# print(player1.shout())

# #attributes and methods 
# #help(player1)#returns the bluePrint 
# #EXERCISE OOP
# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('Peanut', 5)
# cat2 = Cat('Garfield', 3)
# cat3 = Cat('snickers',1)
# # 2 Create a function that finds the oldest cat
# def get_oldest_cat (*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")


# #class Method 
# @classmethod
# def adding_things(cls, num1, num2): #cls is class
#     return cls('Teddy', num1 + num2)

# @staticmethod 
# def adding_things( num1, num2): #doesnt use cls 
#     return  num1 + num2
# player3 = PlayerCharacter.adding_things(2,3)
# print(PlayerCharacter.adding_things(2,3))

#public vs private exp. self._name  using _ is known as  private *dont modify for method or atribute 

#dundermethod built in functions in python 

#inheritance 
#users -wizards - archers 
# class user(object):
#     def sign_in(self):
#         print('logged in')

# class Wizard(user):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of {self.power}')

# class Archer(user):
#      def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#      def attack(self):
#         print(f'attacking with arrows: left- {self.num_arrows}')

# wizard1 = Wizard('merlin',50)
# archer1 = Archer('man',40)

# # def player_attack(char):
# #     char.attack()
# # player_attack(wizard1)
# # for char in [wizard1, archer1]:
# #     char.attack()


# print(isinstance(wizard1, object))

#polymorphism many forms

#inheritance-exercise
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Mark(Cat):
#     def sing(self,sounds):
#         return f'{sounds}'
# my_cats = [Simon('Simon', 4),Sally('Sally',21),Mark('Mark', 1)]
# my_pets = Pets(my_cats)
# my_pets.walk()

# class user(object):
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print('logged in')

# class Wizard(user):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
# def attack(self):
#     print(f'attacking with power of {self.power}')

# class Archer(user):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#     def attack(self):
#         print(f'attacking with arrows: left- {self.num_arrows}')
# #introspection
# wizard1 = Wizard('merlin',40, 'merlin@gmail.com')
# print(wizard1.email)
# print(dir(wizard1)) # dir shows what it has acess to
# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
    
# action_figure = Toy('red',0)
# print(action_figure.__str__())
# print(str(action_figure)
# )
# class SuperList(list):
#     def __len__(self):
#         return 1000
# super_list1 = SuperList()

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(list, object))

#MRO METHOD resolution order
class A:
    num = 10

class B:
    pass
class C(A):
    num = 1

class D(B, C):
    pass
