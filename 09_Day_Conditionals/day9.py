#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
#  If below 18 give feedback to wait for the missing amount of years. Output:

# age = input('enter a value for age')
# years = 18 - int(age) 
# if int(age) >= 18:
#     print('You are old enough to learn to drive')
# else:
#     print(f'you need {years} years to learn to drive')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# your_age = input('Enter your age:')
# my_age = 24
# older = int(your_age) - int(my_age)
# younger = int(my_age) - int(your_age)
# if int(your_age)> int(my_age):
#     print(f'you are {older} years older then me ')
# elif int(your_age) == int(my_age):
#     print('we are the same age')
# else:
#     print(f"you are {younger} years younger then me ")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# a = input('enter value for a ')
# b = input('enter value for b ')
# if int(a) > int(b):
#     print(f'{a} is greater then {b}')
# elif int(a) == int(b):
#     print('they are the same number')
# else:
#     print(f'{a} is less then {b} ')


#LEVEL TWO
#Write a code which gives grade to students according to theirs scores:
# score = int(input('what value score did you get'))
# if score >=90:
#     print('A')
# elif score <90 and score ==80:
#     print('B')
# elif score <80 and score == 70:
#     print('c')
# elif score <70 and score == 60:
#     print('d')
# else:
#     print('f')

#attempting to figure out to get solution to run through the dic to find input value match as a item and return the key 
# select_month = str(input('type out any months full name  '))
# season = {
#     'Autumn': ['September', 'October','November'],
#     'Winter': ['December', 'January','February'],
#     'Spring': ['March', 'April', 'May'],
#     'Summer': ['June', 'July', 'August']
# }
# if select_month in season.values():
#     print(f"{select_month} is in  ")

# a if elif else solution to this 
# month = input("Input the month (e.g. January, February etc.): ")
# day = int(input("Input the day: "))

# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'

# new_fruit = str(input('name a fruit: '))
# fruits = ['banana', 'orange', 'mango', 'lemon']
# if new_fruit in fruits:
#     print(f'{new_fruit} is already in the list')
# else:
#     fruits.append(new_fruit)
#     print(fruits)


#LEVEL THREE
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 #Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if person ['skills']:
    print(person['skills'][len(person['skills'])])
    print('Python' in person['skills'])
    if ['Javascript', 'React'] == person['skills']:
        print('Front End Developer')
    elif ['Node', 'MongoDB', 'React'] == person['skills']:
        print('Full Stack Developer')
    else:
        print("Unknown Title")

 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

 #* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
 #* If the person is married and if he lives in Finland, print the information in the following format: