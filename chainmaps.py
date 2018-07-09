'''
collections.chainmap was added in Python 3.2 and it provides a way to link a number of
dictionaries or other mappings so that they can be treated as one object.

The underlying mappings for ChainMap objects are stored in a list
and are accessible using maps[i] attribute to retrieve the ith dictionary.

Note: Even if dictionaries are unordered, ChainMaps are an ordered list of dictionaries.
'''

from collections import ChainMap
defaults = {'theme':'Default', 'language':'eng', 'showIndex':True, 'showFooter':True}
cm = ChainMap(defaults) #creates a chainmap with default configuration
cm2 = cm.new_child({'theme':'bluesky'}) #creates a new chainmap with a child that overrides the parent
print(cm2['theme']) #returns the overridden theme
print(cm2.pop('theme')) #returns and removes child theme value
print(cm2['theme']) #returns the default theme
cm2.maps[0] = {'theme':'desert', 'showIndex':False} #adds a 'root context' same as new_child
cm2['showIndex']
cm2.parents #retuns defaults
chainMap({'theme':'Default', 'showFooter': True, 'language': 'eng', 'showIndex': True})
