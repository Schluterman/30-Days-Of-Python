#ERRORS IN PYTHON error that crashes is an expection 

#error handling let the code continue 

#syntax error
# def hoooo()
#     pass

# while True:
#     try: 
#         age = int(input('what is your age '))
#         print(age)
#     except ValueError: 
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('plz enter age higher then zero')
#     else: 
#         print('thank u')
#         break

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'pzz enter numbers {err}')

# print(sum(1,2))
while True:
    try: 
        age = int(input('what is your age '))
        10/age
        #raise ValueError('hey cut it out') throwing your own errors 
    except ValueError: 
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('plz enter age higher then zero')
        break
    else: 
        print('thank u')
    
    finally:
        print('ok im done')
    print('can you hear me')
