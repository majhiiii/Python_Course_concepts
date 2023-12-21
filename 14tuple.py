#tuple is a collection type like list organised item as per index order 
#tuple is immutable it means the items cannt be modified
#tuple can be used when elements are read only
#tuple is ordered
#tuple is iterable
#tuple is hashable

''''tu=()#empty tuple with no items
ids=(1,2,3,4,5)#tuple with 5 items
names=("a","b","c","d","e")
loc=("india","usa","canada","uk","france")
print(ids)
print(names)
print(loc)
for x in range (0,len(ids),1):
    print(ids[x],names[x],loc[x])

#tuple unpacking
a,b,c,d,e=ids
print(a,b,c,d,e)
#tuple slicing
print(ids[0:3])
print(ids[:3])
print(ids[3:])
print(ids[::2])
print(ids[::-1])
print(ids[::-2])
#tuple concatenation
print(ids+loc)
print(ids+loc+(100,))
#tuple iteration
for x in ids:
    print(x)

#tuple methods
print(ids.count(1))
print(ids.index(1))
print(ids.index(1,2))
print(ids.index(1,2,5))

#tuple hashing
print(hash(ids))
print(hash(loc))

#tuple append
ids.append(7)
print(ids)
#tuple insert
ids.insert(6,8)
print(ids)
#tuple pop
ids.pop()
print(ids)
#tuple remove
ids.remove(1)
print(ids)
#tuple clear
ids.clear()
print(ids)
#tuple reverse
ids.reverse()
print(ids)
#tuple sort
ids.sort()
print(ids)
#tuple extend
ids.extend(loc)
print(ids)
#tuple min
print(min(ids))
#tuple max
print(max(ids))
#tuple length
print(len(ids))
#tuple print
print(ids)
#tuple copy
ids1=ids.copy()
print(ids1)
#tuple count
print(ids.count(1))
#tuple join
print(ids.join(loc))


#tuple with any other collection
li= [1,2,3,4,5]
tu= tuple(li)
print(tu)
#tuple with nested lists
li= [[1,2,3],[4,5,6]]
tu= tuple(li)
print(tu)
#tuple with nested tuples
li= ((1,2),(3,4))
tu= tuple(li)
print(type(tu))'''


#tuple modification
tu=('a', 'b', 'c', 'd', 'e')
print(tu)
li=list(tu)
li[1]='rakesh'
tu=tuple(li)
print(tu)

#tuple append

