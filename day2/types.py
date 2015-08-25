#!/usr/bin/env python

#integer can be unlimited
i = 10000000   

#floating point/real
f = 0.333


#make an int a float
# int * 1.0
#or
i_as_f = float(i)
f_as_i = int(f)
#string
s = "A string"

#boolean
truthy = True
falsy = False


#[] creats list 

#lists -- convention contains only one type
l=[1,2,3,4,5]
l.append(7) #add element cant add in tuple

#tuple -- frequently contain multiple types are immuntable 
t=(1,"foo",5.0)

#Dictionary 
d1 ={"key1": "value1", "key2": "value2"}
d2 = dict(key1="value1", key2="value2")
d3 = dict([("key1","valeu1"),("key2","value2")])  # list of tuples
d4 ={"key1": ["lions","tigers","bears"], "key":"value2"} 

for value in (i, f, s, truthy, l, t, d1, d2, d3, d4):
    print value, type(value)












