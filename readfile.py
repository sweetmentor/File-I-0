# f = open('data.txt', 'r') 
# lines = f.readlines()
# f.close()
# print(lines)
# ----------Reading a file with readlines

# f = open('data.txt', 'r')
# lines = f.read().split('\n')
# f.close()
# print(lines)
# import re
# text = open('1155-0.txt').read().lower()
# words = re.findall('\w+', text)


# print(words[:11])
#---------------------
# import re
# text = open('1155-0.txt').read().lower()
# words = re.findall('\w+', text)
# print(words)
#print(type(words))
#---------------------------20 most commonly used words
# import re
# import collections
# text = open('1155-0.txt').read().lower()
# words = re.findall('\w+', text)
# most_common = collections.Counter(words).most_common(20)
# print(most_common)
#-------------------------------------5 character words 10 commonly used words-----

import re
import collections
text = open('1155-0.txt').read().lower()
words = re.findall('\w+', text)
long_words = []
for word in words:
    if len(word) >= 5:
        long_words.append(word)
most_common = collections.Counter(long_words).most_common(10)
print(most_common)