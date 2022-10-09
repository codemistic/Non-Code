#top 3 items in a shop 
from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)