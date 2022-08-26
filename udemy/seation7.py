#Functional Programming 
#seperation of concern
#sepration of data and behavior of a program *same input same output should return everytime 
from doctest import NORMALIZE_WHITESPACE
from functools import reduce
from multiprocessing.reduction import duplicate
from typing import Iterable 
#map() example with a pure function 
my_list = [1,2,3]
your_list = [10,20,40]
def multiply_2(item):
    return item*2

print(list(map(multiply_2, my_list)))
print(my_list)

#filter()
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(only_odd)

#zip() joins first items from each list togther then 2nd and so forth 
print(list(zip(my_list, your_list)))

#reduce()
def accumulator(acc, item):
    print(acc + item)
    return acc + item

print(reduce(accumulator, my_list, 0))

#Exercises: map, filter, zip, reduce
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize_pets(item):
    return item.upper()
print(list(map(capitalize_pets,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
def zipping_list(acc,item):
    print(acc + item)
    return acc + item
print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def passing_score(item):
    return item > 50
print(list(filter(passing_score, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))

#lamda Expressions anonimus functions that you use only use once 
#lamda param: action(param)
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print((reduce(lambda acc, item: acc+item, my_list)))

#lambda Exercise:
new_list = [5,4,3]
print(list(map(lambda item: item**2,new_list)))

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)

#list, set, dictionary; comprehension 
my_list3 = [char for char in 'Hello']
my_list4 = [num for num in range(0,100)]
my_list5 = [num**2 for num in range(0,100)]
my_list6 = [num**2 for num in range(0,100) if num %2 ==0]
print(my_list3)
print(my_list4)
print(my_list5)
print(my_list6)

simple_dict = {
    'a':1,
    "b":2
}
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)


#exercise 
some_list = ['a','b','b','c','d','d','e']
duplicates = list(set([x for x in some_list if some_list.count(x) >1]))
print(duplicates)