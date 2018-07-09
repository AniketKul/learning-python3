dictionary = {'one': 'uno', 'two':'dos', 'three':'tres'}
print(dictionary['one'])
dictionary['four'] = 'cuatro'
print(dictionary['four'])
#del dictionary['four']
print(dictionary['four'])

#as a map
course_professors = {'calculus' : 'Prof. Kotter',
                     'diff eq' : 'Prof. Feeny',
                     'linear algebra' : 'Prof. Kotter',
                     'real analysis' : 'Prof. Crabtree'}

student_courses = {'vinnie' : ['calculus', 'diff eq'],
                   'arnold' : ['calculus', 'linear algebra'],
                   'juan luis' : ['real analysis']}

#this is a set.
student_courses = {'vinnie' : {'calculus', 'diff eq'},
                   'arnold' : {'calculus', 'linear algebra'},
                   'juan luis' : {'real analysis'}}

student_professors = {} #which student has which professor? #Empty dictionary
#student_professors = dict()

for student in student_courses:
    for course in student_courses[student]:
        if student not in student_professors:
            student_professors[student] = set()
        student_professors[student].add(course_professors[course])

print(student_professors)


#creating a dictionary

#Way 1
xs = {1:1, 2:4, 3:9}
print(xs)

#Way 2
xs = dict(one='uno', two='dos')
print(xs)

#Way 3
xs = dict([('uno', 'one'),
           ('dos', 'two'),
           ('tres', 'three'),])
print(xs)

#Way 4
from string import ascii_lowercase
xs = dict.fromkeys(ascii_lowercase, 0)
print(xs)

#Way 5
xs = {1:1, 2:4, 3:9}
ys = dict(xs)
print(ys)

'''
Useful dictionary Methods
'''

#dict.update
xs = {1:1, 2:4, 3:9}
ys = {}
ys.update(xs)
print(ys)

#Display all the methods of a dictionary
print(dir({}))

#Usually mehtods starting with '__' are internal to Python so let's have a look at the methods
#which we'll use as a developer
print('\n')
print('Dictionary Methods: ')
print([attr for attr in dir({}) if '__' not in attr])

xs = {'one':'uno'}
xs['two'] = 'dos'
print(xs)

#dict.clear method
xs.clear()

#dict.copy method : Shallow Copy Technique
xs = {'one':'uno'}
ys = xs.copy()
xs.clear()
print(ys)

xs = {'one' : {'spanish' : 'uno',
                'german' : 'ein',
                'french' : 'un'}}

print(xs)

ys = xs.copy()
xs['one'].clear()
print(ys)

#dict.get method

xs = {'one':'uno'}

def get_word(d, word, default=None):
    if word in d:
        return d[word]
    return None

print(get_word(xs, 'two'))
print(xs.get('three', 'default_value'))

english_word = 'one'
spanish_word = xs[english_word] #xs.get(english_word, '')
len(spanish_word)

#dict.pop
xs = {'one':'uno', 'two':'dos'}
print(xs.pop('one'))
print(xs)

#dict.keys, dict.values, dict.items
#dict.items is used for iterating over K,V
print('Iterating Over Dictionary: ')
d = {'uno':'one', 'dos':'two', 'tres':'three'}

print('Iterating Over Dictionary Keys: ')
for key in d:
    print(key)

print('Iterating Over Dictionary Keys: ')
for key in d.keys():
    print(key)

print('Iterating Over Dictionary Values: ')
for value in d.values():
    print(value)

print('Iterating Over Dictionary<K,V> pairs: ')
for item in d.items():
    print(item)

'''
iterkeys, itervalues and iteritems are present in Python 2 and not in Python 3
'''

#dictionaries are immutable
''' You cannot iterate over dictionaries and delete an element from dictionary.
Instead, you create a set add that element to set and delete elements from the dictionary'''

#Idiomatic Way to Delete elements from dictionary.
deleted_keys = set()
for key in d:
    if key =='uno':
        deleted_keys.add(key)

for key in deleted_keys:
    del d(key)
