'''
Python has an immutable set type called frozenset.
It works pretty much exactly like set apart from not allowing methods
or operations that changes values such as the add() and clear() methods.

For example, since normal sets are mutable and therefore, not hashable. Hence, they cannot be
used as members of other sets. frozenset can be used as a member of a set.
'''

s1.add(frozenset(s2))

'''
Also immutable property of frozenset means we can use it for a key to a dictionary
For example,
'''

fs1 = frozenset(s1)
fs2 = frozenset(s2)
dict = {fs1: 'fs1', fs2: 'fs2'}
