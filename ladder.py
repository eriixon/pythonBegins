import sys
num_steps = int(sys.argv[1])

for s in range(0, num_steps):
    z = " "*(num_steps-s-1) + "#"*(s+1)
    print(z)