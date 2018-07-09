'''
Ordered dictionaries: they remember the insertion order. So when we iterate over them,
they return values in the order they were inserted.

For normal dictionary, when we test to see whether two dictionaries are equal,
this equality os only based on their K and V.

For ordered dictionary, when we test to see whether two dictionaries are equal,
insertion order is considered as an equality test between two OrderedDicts with
same key and values but different insertion order.
'''

od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 = OrderedDict()
od2['two'] = 2
print(od1 == od2) #Output: False

'''
OrderedDict is often used in conjunction with sorted method to create a sorted dictionary.
For example,
'''

od3 = OrderedDict(sorted(od1.items(), key = lambda t : (4*t[1]) - t[1]**2))
od3.values() #Output: odict_values([6, 5, 4, 1, 3, 2])
