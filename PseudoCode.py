# Return the " centered" average of an array of ints, which we'll say is the
# mean average of the values, except ignoring the largest and smallest values
# in the array

# centered_average([-10, -4, -2, -4, -2, 0]) -> -3

import statistics

'''
a = [-10, -4, -2, -4, -2, 0]
 a.sort()
[-10, -4, -4, -2, -2, 0]
b = a[1:-1]
b
[-4, -4, -2, -2]
sum(b) / len(b)
-3.0
'''

a = [-10, -4, -2, -4, -2, 0]


def centered_avg(a):
    a.sort()
    print(a)
    b = a[1:-1]
    print(b)
    c = sum(b) - len(b)
    print(c)


centered_avg(a)  # NOTE: this doesn't work...I missed something
