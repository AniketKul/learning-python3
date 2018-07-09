'''

With dict, python will throw a KeyError when attempting to access a key that is not already in the
dictionary.
The defaultdict overrides one method, __missing__(key) and creates a new instance variable, default_factory.
This new instance variable will be used to run the function.

A simple use of defaultdict is to set 'default_factory' to int and use it to quickly tally the counts
of items in the dictionary.
'''

def isprimary(c):
    if (c == 'red') or (c == 'green') or (c == 'blue'):
        return True
    else:
        return False


dd2 = defaultdict(bool)

for word in words:
    dd2[word] = isprimary(word)

'''
Output:

defaultdict(bool, {'blue': True, 'green': True, 'red': True, 'yellow': False})
