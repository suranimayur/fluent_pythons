from collections import abc
issubclass(tuple,abc.Sequence)

# List Comprehensions and Readibility

symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

codes

code1 = [ord(symbol) for symbol in symbols]
code1

# Listcomps Versus map and filter

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

colors = ['black','white']
sizes= ['M','L','S']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

### Generator Expression

symbols ='$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

import array
array.array("I", (ord(symbol) for symbol in symbols))

for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)






















