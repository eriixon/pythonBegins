import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

z = math.sqrt((b**2) - (4*a*c))
x1 = int((-b - z)/(a*2))
x2 = int((-b + z)/(a*2))

print(x1)
print(x2)