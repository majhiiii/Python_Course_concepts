'''li= ['a', 'b', 'c',]
print(li)
for x in li :
  print('index : ', li.index(x), 'item : ', x)

#insert method
ind= int(input('enter index number: '))
if ind<=len(li):
  li.insert(ind, 'x')
  print('after add at index :', ind) 
  print(li)
else : 
  print('index out boundary')  



#extends method
li=['a', 'b', 'c',]
li1=['x', 'y', 'z']
li.extend(li1)
print(li)

ds = ['abacus', 'rk', 'majhi', 'sahoo', 'sai']
ds1=[]
search=input('enter data :')
for x in ds:
  if search in x:
    ds1.append(x)
print(ds1)

#remove method

li=['a', 'b', 'c',]
li.remove('b')
print(li)
print(len(li))

#pop method
li=['a', 'b', 'c',]
ind= int(input('enter index number: '))
if ind<=len(li):
  li.pop(ind)
  print('after pop at index :', ind) 
  print(li)
else : 
  print('index out boundary')

#push method
li=['a', 'b', 'c',]
ind= int(input('enter index number:'))
if ind<=len(li):
  li.push(ind)
  print('after push at index :', ind) 
  print(li)
else : 
  print('index out boundary')

#delete method
li=['a', 'b', 'c',]
del li[1]
print(li)

#sort method
li=['a', 'b', 'c',]
li.sort()
print(li)

#reverse method
li=['a', 'b', 'c',]
li.reverse()
print(li)

#copy method
li=['a', 'b', 'c',]
li1=li.copy()

#count method
li=['a', 'b', 'c',]
print(li.count('b'))

#index method
li=['a', 'b', 'c',]
print(li.index('b'))

#list comprehension
li1=[x for x in range(1,10,1)]
print(li)

li= ['abacus', 'atos', 'accenture', 'abc',]
li1=[]
search=input('enter data :')
for x in li:
  if search in x:
    li1.append(x)
print(li1)

# User input for the alphabet
alphabet = input("Enter the alphabet to filter the list: ").lower()

# Original list
li = ['abacus', 'atos', 'accenture', 'abc']

# List comprehension to filter elements starting with the user-input alphabet
filtered_list = [word for word in li if word.lower().startswith(alphabet)]

# Print the filtered_list
print("Filtered list:", filtered_list)


li= ['abacus', 'atos', 'accenture', 'abc',]
li1=[x for x in li if 's' in x]
print(li1)



#list modification
li=['a', 'b', 'c',]
li.append('d')
print(li)
li.insert(1, 'x')
print(li)

li= ['abacus', 'atos', 'accenture', 'abc',]
print(li[2:5])
li[2:5]= ['x', 'y', 'z']
print(li)

li= ['abacus', 'atos', 'accenture', 'abc','majhi','sahoo','rakesh']
print(li[::2])
li[::2]=['x', 'y', 'z','s']
print(li)

class dept:
  did=None
  dname=None
  dloc=None
  no_of_employee=None
d=dept()
d.did=1
d.dname='fin'
d.dloc='pune'
d.no_of_employee=1000
d1=dept()
d1.did=2
d1.dname='it'
d1.dloc='mumbai'
d1.no_of_employee=2000
d2=dept()
d2.did=3
d2.dname='cse'
d2.dloc='bangalore'
d2.no_of_employee=3000
ds=[d,d1,d2]
print(len(ds))
print('-----------------------------------------------')
for x in ds:
  print('did: ',x.did, 'dname: ',x.dname, 'dloc: ' ,x.dloc, 'no_of_employee: ' ,x.no_of_employee)


or 



class Department:
  def __init__(self, did=None, dname=None, dloc=None, no_of_employees=None):
      self.did = did
      self.dname = dname
      self.dloc = dloc
      self.no_of_employees = no_of_employees

# Creating department instances
d = Department(did=1, dname='fin', dloc='pune', no_of_employees=1000)
d1 = Department(did=2, dname='it', dloc='mumbai', no_of_employees=2000)
d2 = Department(did=3, dname='cse', dloc='bangalore', no_of_employees=3000)

departments = [d, d1, d2]

print(len(departments))
print('-----------------------------------------------')
for department in departments:
  print(f'did: {department.did}, dname: {department.dname}, dloc: {department.dloc}, no_of_employees: {department.no_of_employees}')'''

class dept:
  did=None
  dname=None
  dloc=None
  no_of_employee=None
d=dept()
d.did=1
d.dname='fin'
d.dloc='pune'
d.no_of_employee=1000
d1=dept()
d1.did=2
d1.dname='it'
d1.dloc='mumbai'
d1.no_of_employee=2000
d2=dept()
d2.did=3
d2.dname='cse'
d2.dloc='bangalore'
d2.no_of_employee=3000
ds=[d,d1,d2]
ds1=[x for x in ds]
print(len(ds))

for x in ds1:
  print('----------------------type {0}-------------------------'.format(type(x)))
  print('did: ',x.did, 'dname: ',x.dname, 'dloc: ' ,x.dloc, 'no_of_employee: ' ,x.no_of_employee)


