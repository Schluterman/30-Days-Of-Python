from stringprep import in_table_b1


print('Thirty' + 'Days' + 'Python')
print('Coding' + 'For' +  'All')
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
#Q8
company.capitalize()
company.title()
company.swapcase()
#print(company[6:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
x= company.find('coding')
print(x)
# Replace the word coding in the string 'Coding For All' to Python.
python= company.replace('coding','python')
# Change Python for Everyone to Python for All using the replace method or other methods.
everyone= python.replace('python','Everyone')

# Split the string 'Coding For All' using space as the separator (split()) .
company.split(" ")
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies_list = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list.split(",")
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
def fxn(stng):
    lst = stng.split()
    oupt = ""
    for word in lst:
        oupt += word[0]
    oupt = oupt.upper()
    return oupt
inpt1 = "Python For Everyone"
print(fxn(inpt1))
# Create an acronym or an abbreviation for the name 'Coding For All'.
inpt2 = 'Coding For All'
print(fxn(inpt2))
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
snt = 'You cannot end a sentence with because because because is a conjunction'
print(snt.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(snt.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str1 = snt[:30] + snt[54:]
print(str1)
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Repeated Question
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Repeated Question
# Does ''Coding For All' start with a substring Coding?
fullstring = 'Coding For All'
print(fullstring.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(fullstring.endswith('Coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
spacedstr = '   Coding For All      '
print(spacedstr.strip())
# #Q31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.


print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
print('Name\t      Age\t     Country\t   City')
print('Asabeneh\t  250\t     Finland\t   Helsinki')

#35 
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

#36
math1 = " {num1} + {num2} = {total}".format(num1= 8, num2= 6, total= 8 + 6)
math2 = " {num1} - {num2} = {total}".format(num1= 8, num2= 6, total= 8 - 6)
math3 = " {num1} * {num2} = {total}".format(num1= 8, num2= 6, total= 8 * 6)
math4 = " {num1} / {num2} = {total}".format(num1= 8, num2= 6, total= 8 / 6)
math5 = " {num1} % {num2} = {total}".format(num1= 8, num2= 6, total= 8 % 6)
math6 = " {num1} // {num2} = {total}".format(num1= 8, num2= 6, total= 8 // 6)
math7 = " {num1} ** {num2} = {total}".format(num1= 8, num2= 6, total= 8 ** 6)
print(math1)
print(math2)
print(math3)
print(math4)
print(math5)
print(math6)
print(math7)