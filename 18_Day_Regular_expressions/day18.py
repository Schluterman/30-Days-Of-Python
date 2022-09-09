import re
import string
from collections import Counter
from pprint import pprint
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
#1
split_it = paragraph.split()
Counter = Counter(split_it)
most_occur = Counter.most_common()
print(most_occur)

#2
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12
#note comeback to this question

#LEVEL TWO
#1
def is_valid_variable(potential_variable):
    if re.search(r"^[a-zA-Z_]\w*$", potential_variable):
        return True
    else:
        return False
print(is_valid_variable("first_name"))

#LEVEL THREE
sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'

def clean_text(text):
    text = text.lower()
    text = re.sub("\[.*?]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    return text


pprint(clean_text(sentence))
pprint(most_common_words(clean_text(sentence))[:3])