def MyGenerator(top):
    current = 0
    while current< top:
        yield current
        current +=1

counter = MyGenerator(5)
for i in counter:
    print(i)