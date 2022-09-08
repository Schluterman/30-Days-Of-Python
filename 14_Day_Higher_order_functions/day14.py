#High Order Functions 
from functools import reduce
from re import I


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#LVL ONE
#1 
#The map() function is a built-in function that takes a function and iterable as parameters.
#The Map actually only iterates over a list 
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
#The reduce() function does not return another iterable, instead it returns a single value

#2 Explain the difference between higher order function, closure and decorator
#higher order function
# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable
#Closure  nested function to access the outer scope
#decorator  A decorator is a design pattern in Python that allows a user to add new functionality to an existing object while  accepting new parameters

#3 Define a call function before map, filter or reduce, see examples
def cube(num):
    return num ** 3


def vowel_name(name):
    if name[0] in 'aeiouAEIOU':
        return True
    return False


def sum_of_cubes(num1, num2):
    return num1 + num2

print(list(filter(vowel_name, names)))
print(list(map(cube, numbers)))
print(reduce(sum_of_cubes, list(map(cube, numbers))))

#4
for i in countries:
    print(i)
#5
for i in names:
    print(i)
#6
for i in numbers:
    print(i)


#LEVEL TWO 
#1
def change_to_upper(countries):
    return countries.upper()
countries_upper_cased = map(change_to_upper,countries)
print(list(countries_upper_cased))

#2
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

#3
def names_to_upper(names):
    return names.upper()
names_upper_cased = map(names_to_upper,names)
print(list(names_upper_cased))



