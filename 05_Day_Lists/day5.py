# # Declare an empty list
# from itertools import count


# empty_list= []
# # Declare a list with more than 5 items
# list= [1,2,3,4,5]
# # Find the length of your list
# len(list)
# # Get the first item, the middle item and the last item of the list
# list[0]
# list[2]
# list[-1]
# # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_types = ['preston',24,5.4,False,'USA']
# # Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle'  'Amazon']
# # Print the list using print()
# print(it_companies)
# # Print the number of companies in the list
# print(len(it_companies))
# # Print the first, middle and last company
# print(it_companies[0])
# print(it_companies[3])
# print(it_companies[-1])
# # Print the list after modifying one of the companies
# it_companies.pop(0)
# print(it_companies)
# # Add an IT company to it_companies
# it_companies.insert(2,'dell')
# # Insert an IT company in the middle of the companies list
# it_companies.insert(3,'blue')
# # Change one of the it_companies names to uppercase (IBM excluded!)
# print(it_companies[0].capitalize())
# # Join the it_companies with a string '#;  '
# print('#;  '.join(it_companies))
# # Check if a certain company exists in the it_companies list.
# if 'Apple' in it_companies:
#     print('YES IM HERE')
# # Sort the list using sort() method
# print(it_companies.sort())
# # Reverse the list in descending order using reverse() method
# print(it_companies.reverse())
# # Slice out the first 3 companies from the list
# print(it_companies[0:3])
# # Slice out the last 3 companies from the list
# print(it_companies[-3:0])
# # Slice out the middle IT company or companies from the list
# print(it_companies[-5:-3]) #not Sure
# # Remove the first IT company from the list
# del it_companies[0]
# print(it_companies)
# # Remove the middle IT company or companies from the list

# # Remove the last IT company from the list
# del it_companies[-1]
# print(it_companies)
# # Remove all IT companies from the list
# it_companies.clear()
# print(it_companies)
# # Destroy the IT companies list
# del it_companies
# #join the following list
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# full_stack = front_end.extend(back_end)
# print(full_stack)

#LEVEL TWO 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_ages = min(ages)
max_ages = max(ages)
print(ages)

# Find the median age (one middle item or two middle items divided by two)

# Find the average age (sum of all items divided by their number )

# Find the range of the ages (max minus min)

# Compare the value of (min - average) and (max - average), use abs() method
