import re
#pattern = re.compile('this')
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'

a = pattern.search(string)
password = 'dgfa42'
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}[0,9]")
print(a) #good for multiple searches 
check = pattern2.fullmatch(password)
print(check)
