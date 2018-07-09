#Sets are mutable but items in set are immutable.
#Cannot create an empty set using a={} because this will create a dictionary
#To create an empty set, we write either a = set() or a = frozenset()

#Set or frozenset methods are as follows:

len(s)
s.copy() #Returns a shallow copy of s
s.difference(t) #Returns a set of all items in s but not in t
s.intersection(t) #Returns a set of all items in both t and s
s.isdisjoint(t) #Returns True if s and t have no items in common
s.issubset(t) #Returns True if all items in s are also in t
s.issuperset(t) #Returns true if all items in t are also in s
s.symmetric_difference(t) #Returns a set of all items that are in s or t, but not both
s.union(t) #Returns a set of all items in s or t.

s.add(item)
s.clear()
s.difference_update(t) #Removes all items in s that are also in t
s.discard(item)

#Removes all items from s that are not in the intersection of s and t
s.intersection_update(t)

#Returns and removes an arbitary item from s
s.pop()

s.remove(item)

#Removes all items from s that are not in the symmetric difference of s and t
s.symmetric_difference_update(t)

#Adds all the items in an iterable object t to s
s.update(t)

#Note that set object does not care that its members are not all of the same type, as long
#as they are immutable. If you try to use a mutable object such as a list or dict in a set,
#you'll get an unhashable type error. 
