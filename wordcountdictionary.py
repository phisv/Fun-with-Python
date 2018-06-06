import re

words = {}
with open('text.txt') as file:
    content = file.read()
content = content.replace('\n', '')
content = content.replace('.', '')
content = content.replace(',','')
content = content.replace('-','')
content = content.lower()
content = content.split()
#content = re.sub('[^\w]',' ', content).split()
for word in content:
    if word in words:
        words[word] = words[word]+1
    else:
        words[word] = 1
for word in words.keys():
    print('%12s  %12s' %(word, words[word]))
