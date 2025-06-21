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

a = (10,'alpha',[1,2])
b = (10,'alpha',[1,2])

a == b

b[-1].append(99)
print(a)
print(b)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10,'alpha',(1,2))
tm = (10,'alpha',[1,2])

fixed(tf)
fixed(tm)

colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

## Tuples are not Just Immutables List

lax_coordinates = (33.9425,-118.408056)
city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country,_ in traveler_ids:
    print(country)

## Tuple Unpacking

lax_coordinates = (33.9425,-118.408056)
latitude,longitude = lax_coordinates
print(latitude)
print(longitude)

divmod(20,8)


### Using * to grab excess items

a,b ,*rest =  range(10)
print(a,b,rest)

a, *body,c,d = range(10)
print(a,body,c,d)

### Nested Tuple Unpacking

def fun(a,b,c,d,*rest):
    return a,b,c,d,rest 

fun(*[1.2],3,*range(4,7))

metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
    ('Mexico City','MX',20.142,(19.433333,-99.133333)),
    ('New York-Newark','US',20.104,(40.808611,-74.020386)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.635833)),
]

metro_areas

### Pattern Matching with Sequences

def handle_command(self,message):
    match message:
        case ["BEEPER",frequency,times]:
            self.beep(frequency,times)
        case ["NECK",angle]:
            self.rotate_neck(angle)
        case ["LED",ident,intensity]:
            self.leds[ident].set_brightness(ident,intensity)
        case ["LED",ident,red,green,blue]:
            self.leds[ident].set_color(red,green,blue)
        case _:
            raise ValueError(f"Invalid command: {message}")



## Pattern matching with match/case 





