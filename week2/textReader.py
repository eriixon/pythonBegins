import numpy as np
import re
from scipy import spatial

text = ''
lines_count = 0
with open ("text.txt", 'r') as f:
    text = f.readlines()
    lines_count = len(text)

new_text = []


words = {}
i=0
for line in text:
    line = line.lower()
    line = re.split('[^a-z]',line)
    line = list(filter(None, line))
    new_text.append(line)
    for word in line:
        if word not in words:
            words[word] = i
            i+=1

matrix = np.zeros((lines_count, len(words)), dtype=np.int)

for index, line in enumerate(new_text):
    for word in words:
        x = line.count(word)
        matrix[index,words[word]] = x

r = ''
for i in range(1,len(new_text)):
    z = spatial.distance.cosine(matrix[0,],matrix[i,])
    r = "{0}{1} ".format(r,z)
r = r.strip()
with open("first.txt",'w') as f:
    f.write(r)
