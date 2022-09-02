#generators  give a list of values over a course of time 
# range(100)
# list(range(100))
# def make_list(num):
#     result = []
#     for i in range(n):
#         result.append(i*2)
#     return result
# my_list = make_list(100)
# print(my_list)

#iterable something we can loop through  __iter__ 
# iterate is to take an item do something then go to the next item and repeat to the next

# def generator_func(num):
#     for i in range(num):
#         yield i #pauses the function 
# g = generator_func(100)
# next(g)
# next(g)
# print(g)

# for item in generator_func(10):
#     print(item)

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
# special_for([1,2,3])

# class MyGen():
#     current = 0
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     def __iter__(self):
#         return self
#     def __next__ (self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current +=1
#             return num
#         raise StopIteration

# gen = MyGen(0,100)
# for i in gen:
#     print(i)

#Fibonacci num
# from cgitb import reset


# def fib(num): #with generator
#     a = 0
#     b= 1
#     for i in range(num):
#         yield a 
#         temp = a 
#         a = b 
#         b = temp + b
# for x in fib(21):
#     print(x)

def fib2(num):
    a = 0
    b= 1
    result = []
    for i in range(num):
        result.append(a) 
        temp = a 
        a = b 
        b = temp + b
    return result
fib2(100)
print(fib2(100))