import package1.generic_functions.generic_functions

print(package1.generic_functions.generic_functions.add(10, 5))
print(package1.generic_functions.generic_functions.div(10, 5))

import package1.generic_functions.generic_functions as gf


print(gf.add(10, 5))
print(gf.div(10, 5))

from package1.generic_functions.generic_functions import add ,div
print(add(10, 5))
print(div(10, 5))

from package1.generic_functions.generic_functions import add as addition  ,div as division
print(addition(10, 5))
print(division(10, 5))
