# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog['color'] = 'brown'
dog['name'] = 'bran'
dog['breed'] = 'boxer'
dog['legs'] = 4
dog['age'] = 3
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student ={
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'gender':'Male',
    'age':250,
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Finland',
    'city': 'wels',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(len(student['skills']))
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('Java')
print(student['skills'])
# Get the dictionary keys as a list
keys = student.keys()
print(keys)
# Get the dictionary values as a list
values = student.values()
print(values)
# Change the dictionary to a list of tuples using items() method
tuple_list = []
for i in student:
    tpl = (i, student[i])
    tuple_list.append(tpl)
print(tuple_list)
# Delete one of the items in the dictionary
delete_item = student.pop('gender')
print(delete_item)
# Delete one of the dictionaries
del student