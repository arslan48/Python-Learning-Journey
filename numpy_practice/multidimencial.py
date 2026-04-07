import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

Ass = array[0,0,0] + array[2,0,0] + array[2,0,0]

print(Ass)

print(array.shape)

# 2

cat = array[0,0,2] + array[0,0,0] + array[2,0,1]

print(cat)

dog = array[0,1,0] + array[1,1,2] + array[0,2,0]

print(dog)

sit = array[2,0,0] + array[0,2,2] + array[2,0,1]

print(sit)

name = array[0,0,0] + array[1,0,2] + array[0,2,2] + array[0,0,2] + array[0,1,1]

print(name)