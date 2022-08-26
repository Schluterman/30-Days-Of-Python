empty_tuple = () # or using the tuple constructor
empty_tuple = tuple()
sisters = ('paige','shelby')
brothers =('mitch','jackson')
siblings = brothers + sisters
parents = ('dad','mom')
print(siblings)
print(len(siblings))

family_members = siblings + parents
print(family_members)

#LEVEL TWO
siblings = family_members[:4]
parents = family_members[4:]
print(siblings)
print(parents)

fruits = ('apple','banana')
vegatables = ('carrot','brocoli')
animal_products = ('steak','pork')
food_stuff_tp = fruits + vegatables + animal_products 
food_stuff_tupled_list = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_tupled_list)
slice_middle = food_stuff_tupled_list[:2] + food_stuff_tupled_list[4:]
print(slice_middle)
del(food_stuff_tp)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('Estonia sure is a Nordic Country')
else:
    print('Estonia is not a nordic country')
print('Iceland' in nordic_countries)
