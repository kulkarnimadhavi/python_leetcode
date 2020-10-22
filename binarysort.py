"""
Sort an array of binary nos so that all 0s coem on the right nad all 1's come on left
"""
from array import array

array_x = array('b',[0, 1, 1, 0, 0, 1, 0, 0, 1])

k = list(array_x)
k.sort()
print(k)
