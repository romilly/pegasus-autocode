__author__ = 'romilly'

v1 = 1.0
v2 = 1.0
n1 = 1
while v2 > 10e-6:
    v2 = v2 / n1
    v1 = v1 + v2
    n1 = n1 + 1
print v1
