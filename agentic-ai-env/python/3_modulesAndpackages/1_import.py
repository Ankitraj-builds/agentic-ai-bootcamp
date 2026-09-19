import math

print(math.sqrt(16))

from math import sqrt,pi

print(pi)
print(sqrt(121))


#numpy need to install

import numpy as np
arr=np.array([1,2,3,4])

print(arr)
print(type(arr))

from math import *

print(sqrt(100))
print(pi)



#import local package

from package.maths import addition
print(addition(10,20))

from package.sub_package.mult import multiply

print(multiply(10,2))