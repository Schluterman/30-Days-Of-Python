# #Decorators
# # @classmethod @staticmethod supercharge a function
# def hello(func):
#     func()

# def greet():
#     print('here')

# a = hello(greet)
# print(a)

# #Higher Order Function
# def greet(func):
#     func()
# #exp 2 Returns a function 
# def greet2():
#     def func():
#         return 5
#     return func


# def my_decorator(func):
#     def wrap_func(x):
#         print('****')
#         func(x)
#         print('****')
#     return wrap_func

# @my_decorator
# def helo(greeting):
#     print(greeting)




# helo('hiiii')

#DECORATOR PATTERNS
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)

# hello('hiiii')

# from time import time
# from unittest import result
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'it took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(10000):
#         i*5
# long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kawrgs):
    if args[0]['valid']:
        return fn(*args, **kawrgs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)