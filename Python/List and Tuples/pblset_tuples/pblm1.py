# sort the (name, age, height) tuples by ascending order 
# where name is string, age and height are numbers. 
# The tuples are input by console. The sort criteria is    
# 1: Sort based on name 
# 2.Then sort based on age;  
# 3: Then sort by score.

from operator import itemgetter
 
l = []
 
while True:

    s = input("Enter Details: (Name,Age,Score)[Press Enter to end\n")

    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))

#itemgetter to enable multiple key 