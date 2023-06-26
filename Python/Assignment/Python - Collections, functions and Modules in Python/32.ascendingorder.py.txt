"""
Write a Python script to sort (ascending and descending) a dictionary by
value. 
"""
#asending order
d={1:2,3:4,4:3,2:1,0:0}
l=sorted(d.items())
print('Ascending order is',l)

#decending oder
l=list(d.items())
l.sort(reverse=True)
print('Descending order is',l)




