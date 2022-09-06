#1
import random
import string

# def random_user_id():
#     identity = ''
#     for _ in range(6):
#         identity += random.choice(string.ascii_letters)
#     return identity


# print(random_user_id())

#2
# def user_id_gen_by_user():
#     num_chars = int(input('number of characters '))
#     ids = int(input('number of ids needed to generate '))
#     for _ in range(ids):
#         identify= ''.join([random.choice(string.ascii_letters) for _ in range(num_chars)])
#         print(identify)
# print(user_id_gen_by_user())

#3 
def rgb_color_gen():
    r = str(random.randint(0,255))
    g = str(random.randint(0,255))
    b = str(random.randint(0,255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())
