#set - unordered collection of unique elements
#set collections dont relate with order and index. it deletes duplicate elements.
import sys 
'''s={'a','b','c','c'}
a={'1','2','4','2','3'}
print(s)
print(type(s))
print(sys.getsizeof(s))
print(a)
print(type(a))
print(sys.getsizeof(a))
search= input('enter data :')
if search in s:
  print("Data found :",search)
else:
  print("Data not found :")

#copy one set to another
s1={'a','b','c','d'}
s2=s1.copy()
print('s2 :',s2)

#converting any other collection to set
l1=[1,2,3,4,5,6,7,8,9]
s3=set(l1)
print('s3 :',s3)

#adding data to set
s4={'a','b','c','d'}
s4.add('e')
print('s4 :',s4)

tt=set({'a','b'})
print(tt)
print(type(tt))
print(len(tt))
tt.add(input('enter data'))
print('tt :',tt)

#remove data from set
s5={'a','b','c','d'}
data=input('enter data to be removed :')
if data in s5:
  s5.remove('c')
  print(s5)
else :
  print('no such data to remove')

#set discard
s6={'a','b','c','d'}
s6.discard('k')
print('s6 :',s6)

#pop data from set
s7={'a','b','c','d'}
s7.pop() #first item will be removed
print('s7 :',s7)

#clear data from set
s8={'a','b','c','d'}
s8.clear()
print('s8 :',s8) 
del s8 #delete set

tt=set({'a',1, True, 1.1})
print(tt)
print(type(tt))
print(len(tt))

class emp:
  id_=1
  name_='myself'
ob=emp()
ob1=emp()
ob1.id_=10
ob1.name_='rakesh'
tt= set({ob,ob1})
print(type(tt))
print(len(tt))
for x in tt :
  print (x.id_, x.name_)

#set union function
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s3=s1.union(s2)
print('s3 :',s3)

#set union operator
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s3=s1 s2
print('s3 :',s3)

#set intersection
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s3=s1.intersection(s2)
print('s3 :',s3)

#set difference
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s3=s1.difference(s2)
print('s3 :',s3)

#set symmetric difference
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s3=s1.symmetric_difference(s2)
print('s3 :',s3)

#set intersection update
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s1.intersection_update(s2)
print('s1 :',s1)

#set union update
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s1.update(s2)
print('s1 :',s1)

#set dif update
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s1.difference_update(s2)
print('s1 :',s1)

#set sym dif update
s1={'a','b','c','d'}
s2={'e','f','g','h'}
s1.symmetric_difference_update(s2)
print('s1 :',s1)

#subset
s1={'a','b','c','d'}
s2={'e','f','g','h'}
print(s1.issubset(s2))

#superset
s1={'a','b','c','d'}
s2={'e','f','g','h'}
print(s1.issuperset(s2))

#disjoint
s1={'a','b','c','d'}
s2={'e','f','g','h'}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))'''


#frozen set
#it converts mutable to immutable

set1={'python','java', 'c++'}  
print(set1)
set1.add('r')
print(set1)
set1.remove('c++')
print(set1)
f1=frozenset(set1)
for x in f1 :
  print(x)
f1.add('a')  