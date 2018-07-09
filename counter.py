'''
Counter is a subclass of a dictionary where each dictionary key is a hashable
object and the associated value in an integer count of that object.
There are 3 ways to initialize a counter.
'''
from collections import Counter
c1 = Counter('anysequence')
c2 = Counter({'a':1, 'c':1, 'e':3})
c3 = Counter(a=1, c=1, e=3)
print(c1)

'''
We can also create an empty counter object and populate it by passing
its update method on iterable or a dictionary
'''
from collections import Counter
ct = Counter() #creates an empty counter object
ct.update('abca') #populates the object
print(ct) #Output: Counter({'a': 2, 'b': 1, 'c' : 1})
ct.update({'a':3}) #updates the 'a' count
print(ct) #Output: Counter({'a': 5, 'b': 1, 'c': 1})

for item in ct:
    print('%s : %d' % (item, ct[item]))

'''
Notable difference between counter objects and dictionaries is that counter
objects return a zero count for missing items rather than raising a key error.

e.g: ct['x'] will return 0
'''

ct.update({'a':-3, 'b':-2, 'd':3, 'e':2}) #perform an update
sorted(ct.elements()) #returns a sorted list from the iterator

'''
Two other Counter methods: most_common() and subtract()
most_common() takes a positive integer argument that determines the number of
most common elements to return. Elements are returned as a list of (key, value).

subtract() works exactly like update except instead of adding values, it subtracts them.
'''
ct.most_common()
ct.subtract({'a':2})
