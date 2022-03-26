
import sys
def multy(x):
    for i in range(1, 11):
        print('{0:2d} * {1:2d} = {2:3d}'.format(i, x, i*x))

x = int(sys.argv[1])

multy(int(x))