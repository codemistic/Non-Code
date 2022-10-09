#sort a tuple of tuples by 2nd item

tup = (('a', 23),('b', 37),('c', 11), ('d',29))
h = sorted(tup,key=lambda a: a[1])
print(h)