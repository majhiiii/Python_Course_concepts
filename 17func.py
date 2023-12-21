'''def disp():
  print("Hello World")

if __name__ == "__main__":
  disp()


#function with parameters
def disp(x):
  print(x)
  print(type(x))
  print(id(x))

if __name__ == "__main__":
  disp(input('enter data :'))



def disp(x):
  print(x)
  print(type(x))
  print(id(x))

if __name__ == "__main__":
  disp(1)
  disp(1.1)
  disp(True)
  disp(10j)
  disp(b'10')



def disp(x,y,z ='abacus'):
  print(x,y,z)

if __name__ == "__main__":
  disp(10,1)
  disp(1,'u' ,'atos')


def disp(no):
  for x in range(1,no,1):
    for y in range(1,no+1,1):
      print('+',end='')
    print(' ')  
if __name__=="__main__":
  disp(3)
  print('--------------------')
  disp(5)
  print('--------------------')
  disp(6)
  print('--------------------')


class emp:
  did=1
  dname='fin'
  dloc='pune'
def disp(ob):
  print('did {0} dname {1} dloc {2}' .format(ob.did,ob.dname,ob.dloc))
if __name__=="__main__":
  ob=emp()
  disp(ob)

class emp:
  did = 1
  dname = 'fin'
  dloc = 'pune'

def disp(ob):
  print('did {0} dname {1} dloc {2}'.format(ob.did, ob.dname, ob.dloc))

# Create an instance of the emp class and call the disp function
ob = emp()
disp(ob)


def disp(x,y,z):
  print('did {0} dname {1} dloc {2}'.format(x,y,z))
if __name__=="__main__":
  disp(x='01',y='fin', z='pune')

def disp(*args):
  print(type(args))
  for x in args:
    print(x)
if __name__=="__main__":
 disp(10,20,30)

def disp(id_,name_,loc_,*args):
  print(id_)
  print(name_)
  print(loc_)
  for x in args:
    print(x)
if __name__=='__main__' :
  disp('01','fin','pune',1,2,3,4,5,6,7,8,9)

def disp(**args):
  print(args['id_'],args['name_'])
if __name__  == '__main__' :
  disp(id_='01',name_='fin')
import math  
def disp(x):
  return math.pow(x,2)
if __name__  == '__main__' :
  print(disp(20))
    
  
#recursion function
def fact(x):
  if x==1:
    return 1
  else:
    return x*fact(x-1)
if __name__ == '__main__' :
  range_= int(input('enter your range : '))
  for x in range(1,range_,1):
    print('no :',x, 'factorial :',fact(x))

  
  
#nested functions

def disp(x):
  def disp2(y):
    print(x,y)
  disp2(10)
disp(10)

def disp():
  def a():
    print('hello')
  def b():
    print('ok')
  x= input('enter ur choice :') 
  if(x=='u'):
    a()
  elif(x=='you'):
    b()
  else: 
    print('please enter valid data')  

#if __name__== '__main__':
disp()





#Python supports predefined functions

#1 math function

import math 
print(math.pow(4,2))
print(math.sqrt(16))
print(math.pi)
print(math.cos(2))
print(math.tan(2))
print(math.log(2))
print(math.log10(2))
print(math.ceil(2.56)) #round to nearest whole number
print(math.ceil(-2.56))
print(math.floor(-56.56))
print(math.floor(-2.56))

import math
def disp(nos):
  for f in nos:
    print('no :', f, 'fact :', math.factorial(f))


if __name__=='__main__' :
  nos=[1,2,5,6,7,8,9]
  disp(nos)

#conversion function
s='10'
x=int(s)
print(x,type(x))

s='10.1'
xx=float(s)
print(xx,type(xx))

s='111j'
xxx=complex(s)
print(xxx,type(xxx))

s='true'
x=bool(s)
print(x,type(x))

s=b'10'
print(s,type(s))
xx=memoryview(s)
print(xx,type(xx))

a= (1,2,3,4)
print(a,type(a))
li=list(a)
print(li,type(li))
b= tuple(li)
print(b,type(b))

record= ('a','b','c')
team1= set(record)
print(team1, type(team1))

record= set(('a','b','c'))
print(record)


#string function
s='hello world'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.split())
print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.isspace())
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isdecimal())
print(s.isidentifier())
print(s.isprintable())
print(s.isascii())
print(s.strip()) #removes space if any
print(s.lstrip()) #removes space from left
print(s.rstrip()) #removes space from right
print(s.count('o'))

s= 'abacus'
print(s.find('a'))
print(s.find('c'))
print(s.find('c',3))
print(s.find('c',3,5))
print(s.rfind('c'))
print(s.rfind('c',3,5))
print(s.index('c'))
print(s.index('c',3,5))
print(s.count('a'))
for x in s :
  print(x, s.count(x))

print(s.index('a'))
for x in s :
  print(x, s.index(x))'''

s='abacus'
print(s.index('a'))
for x in s :
  print(x, ord(x),chr(ord(x)))