import matplotlib.pyplot as plt
import math

x = list(range(1, 100))
#l = []; l2 = []; a = 1
plt.plot(x, [y * y for y in x])
plt.plot(x, [(7 * y) * math.log(y, 2) for y in x])
plt.plot(x, [y for y in x])
plt.show()


'''
O(1)
e.g: append, get item, set item

O(logn)
e.g: Finding an element in a sorted array

O(n)
e.g: Copy, insert, delete operation

nlogn
e.g: Sort a list, merge-sort

n^2
e.g: Find the shortest path between two nodes in a graph. Nested loops.

n^3
e.g: Matrix Multiplication

2^n
e.g: Towers of honoi, backtracking

'''

'''
i = 1
while i <= n;
    i = i * 2
    print(i)

Time Complexity: O(log(n))
