# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['dell','hbo','lenovo'])
# Remove one of the companies from the set it_companies
it_companies.remove('Google')
# What is the difference between remove and discard
print('Remove Raise Errors if item is not in the set: Discard does not raise errors')
# Exercises: Level 2
# Join A and B
A.union(B)
# Find A intersection B
A.intersection(B)
# Is A subset of B
A.issubset(B)
# Are A and B disjoint sets
A.isdisjoint(B)
B.isdisjoint(A)
# Join A with B and B with A
print(A.union(B))
print(B.union(A))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
A.clear
B.clear
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age)) #length of list age
len((age_set)) #length of Set age
# Explain the difference between the following data types: string, list, tuple and set
# A list is a collection of ordered data. MUTABLE
# A tuple is an ordered collection of data.	IMMUTABLE
# A set is an unordered collection.	 MUTABLE NO DUPLICATES
# A dictionary is an unordered collection of data that stores data in key-value pairs.
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

# python program to print all
# the unique words in a string
# in python using set() method
# function to print unique words
def printWords(l):
    # for loop for iterating
    for i in l:
        print(i)
# Driver code
str = 'I am a teacher and I love to inspire and teach people.'
# storing string in the form of list of words
s = set(str.split(" "))
# passing list to print words function
printWords(s)
