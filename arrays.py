# a is array

a.itemsize # size in bytes of items stored in the array
a.append(x) # appends item x to the end of the array
a.count() # Returns the number of occurrences of x in a
a.extend(b) # appends any iterable b to the end of array
a.frombytes(s) # appends items from a string s as an array of machine values

'''
Reads n items, as machine values, from a file object, f and appends them to a
'''
a.fromfile(f, n)
a.fromlist(l)   # appends items from list l
a.insert(i, x) # Inserts item x before index i
# Removes and returns items with index i.
# Defaults to the last item (i = -1) if not specified
a.pop([i])
a.remove(x)  # Removes the first occurence of item x
a.reverse() # Reverse the order of items
a.tofile(f) # Writes all items, as machine values, to file object f
a.tolist() # Converts the array to a list


import array
ba = array.array('i', range(10**6))
bl = list(range(10**6))

import sys
100 * sys.getsizeof(ba) / sys.getsizeof(bl)
