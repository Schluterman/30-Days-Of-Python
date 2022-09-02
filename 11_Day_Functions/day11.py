#DAY 11 FUNCTIONS 
from wsgiref.util import request_uri
from xml.etree.ElementTree import PI

# #Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers (num1,num2):
#     sum = num1 + num2
#     return sum
# print(add_two_numbers(4,2))

# #Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))

# def add_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(add_all_nums(2,4,6,43))

# def convert_celsuis_to_fahrenheit(celcius):
#     return (celcius * 9/5)+32
# print(convert_celsuis_to_fahrenheit(12))

# def check_season(month):
#     if month in ["September", "October", "November"]:
#         print("Autumn")
        
#     if month in ["December", "January", "February"]:
#         print("Winter")
#     if month in ["March", "April", "May"]:
#         print("Spring")
#     else:
#         print("Summer")
# print(check_season("January"))

#Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1, x2, y1, y2):
#     m = (y2 - y1) / (x2 - x1)
#     return m

#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# def solve_quadratic_eqn(a, b, c):
#     D = b * b - 4 * a * c
#     X1 = (-b + D) / (2 * a)
#     X2 = (-b - D) / (2 * a)
#     print(X1, X2)

# 8
def print_list(lst):
    for i in lst:
        print(i)


# 9
def reverse_list(a):
    return a[::-1]


# 10
def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a


# 11
def add_item(mutable, tba):
    mutable.append(tba)
    return mutable


# 12
def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable


# 13
def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers


# 14
def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums


# 15
def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums