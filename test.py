import json

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
g = (data['fruits'])
# the print displays:
# [u'apple', u'banana', u'orange']

f = ['apple', 'banana']

for x in g:
    if x in f:
        print("in")