f=open("test.txt","w+")
for i in range(100):
    f.write("Hello from %d\n" % (i+1))
f.close()
ff = open("test.txt","r")
d = ff.readlines()
for i in d:
    print(i)
ff.close()