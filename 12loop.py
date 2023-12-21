#for loop

'''for num in range(2, 21, 2):
  print(num)


s='India'
for x in range (0, len(s),1):
      print ('index :',x, 'char:' , s[x])

for x in s:
  print(x)
#even or/ odd number 

if __name__=='__main__':
    for x in range (1,20,1):
      if x%2==0:
        print('even no:',x)
      else:
        print('odd no:',x)    

#read data from collections:
if __name__=='__main__':
  ds=['you','rama','raja','rani']
  print (ds)
  print(type(ds))
  for x in range (0,len(ds),1):
    if x%2==0:
      print('even no index :',x,'item :',ds[x])
    else:  
      print('odd no index :',x,'item :',ds[x])

#nested loop
if __name__=='__main__':
  for x in range (1,10,1):
    for y in range (1,x+1,1):
      print( y, end='')
    print('\n')  
if __name__=='__main__':
  for x in range (1,10,1):
    for y in range (1,x+1,1):
      print( '*', end='')
    print('\n')  
if __name__=='__main__':
  print(ord('A'))
  print(chr(ord('A')))
  for x in range (65,91,1):
    for y in range (65,x+1,1):
      print( chr(y), end='')
    print('\n')  

#for loop start step and incremenet
x=range(1,10,1)
print(x)
print(x.step)
print(x.start)
print(x.stop)

range(1, 10)
1
1
10

#for loop start step and incremenet
for x in range(1,10,2):
    print(x)

    1
3
5
7
9

#for loop start step and incremenet
for x in range(1,50,2):
    if x%2==0:
        print('evn number :',x)
    else:print('odd number :',x)
odd number : 1
odd number : 3
odd number : 5
odd number : 7
odd number : 9
odd number : 11
odd number : 13
odd number : 15
odd number : 17
odd number : 19
odd number : 21
odd number : 23
odd number : 25
odd number : 27
odd number : 29
odd number : 31
odd number : 33
odd number : 35
odd number : 37
odd number : 39
odd number : 41
odd number : 43
odd number : 45
odd number : 47
odd number : 49

#for loop start step and incremenet
#index012345
data='BHARAT'
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print('-----------------------')
for x in range(0,len(data),1):
    print(data[x])   
B
H
A
R
A
T
-----------------------
B
H
A
R
A
T


data='BHARAT'
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print('-----------------------')
for x in range(0,len(data),1):
    if(x>=2):
        break
    print(data[x])   
B
H
A
R
A
T
-----------------------
B
H

data='BHARAT'
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print('-----------------------')
for x in range(0,len(data),1):
    if(x>=2):
        print('pass')
        pass       
    print(data[x])   

B
H
A
R
A
T
-----------------------
B
H
pass
A
pass
R
pass
A
pass
T



data='BHARAT'
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print('-----------------------')
for x in range(0,len(data),1):
    if(x>=2):
        break      
    print(data[x])   

data='BHARAT'
#for each loop initialisation condition and increment automatic
#start from 0 and continue till last element of collection
#default incremenet 1
#efficient to read all data from collection from start to end
for x in data:
    print(x)

B
H
A
R
A
T

#for loop reverse
for x in range(0,-20,-1):
    print(x)

0
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
-11
-12
-13
-14
-15
-16
-17
-18
-19

   #for loop reverse
data='BHARAT'
for x in range(0,-6,-1):
    print(x,data[x])

0 B
-1 T
-2 A
-3 R
-4 A
-5 H


nested

#for loop nested
for x in range(1,20,1):
    for y in range(1,x+1,1):
        print(y,end='')
        #end='' terminates new line manage in same line
    print(' ')
1 
12 
123 
1234 
12345 
123456 
1234567 
12345678 
123456789 
12345678910 
1234567891011 
123456789101112 
12345678910111213 
1234567891011121314 
123456789101112131415 
12345678910111213141516 
1234567891011121314151617 
123456789101112131415161718 
12345678910111213141516171819 


#for loop nested
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print(y,end=' ')

    print(' ')
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
1 2 3 4 5 6  
1 2 3 4 5 6 7  
1 2 3 4 5 6 7 8  
1 2 3 4 5 6 7 8 9  



#for loop nested
import math
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print('v',y,'p',math.pow(y,2),end=' ')

    print('')

v 1 p 1.0 
v 1 p 1.0 v 2 p 4.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 v 5 p 25.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 v 5 p 25.0 v 6 p 36.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 v 5 p 25.0 v 6 p 36.0 v 7 p 49.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 v 5 p 25.0 v 6 p 36.0 v 7 p 49.0 v 8 p 64.0 
v 1 p 1.0 v 2 p 4.0 v 3 p 9.0 v 4 p 16.0 v 5 p 25.0 v 6 p 36.0 v 7 p 49.0 v 8 p 64.0 v 9 p 81.0 

#for loop nested
import math
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print('*',end=' ')

    print('')

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 

#for loop nested
import math
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print('a',end=' ')

    print('')

a 
a a 
a a a 
a a a a 
a a a a a 
a a a a a a 
a a a a a a a 
a a a a a a a a 
a a a a a a a a a 


ASCII, in full American Standard Code for Information Interchange, a standard data-encoding format for electronic communication between computers. ASCII assigns standard numeric values to letters, numerals, punctuation marks, and other characters used in computers.
print(ord('a'))
print(ord('b'))
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print('a',end=' ')

    print('')
97
98
a 
a a 
a a a 
a a a a 
a a a a a 
a a a a a a 
a a a a a a a 
a a a a a a a a 
a a a a a a a a a 
-----------------------------------------------------------------------------------
#for loop nested
for x in range(97,123,1):
    for y in range(97,x+1,1):
        print(chr(y),end=' ')  #chr function converts ascii to char
    print('')
a 
a b 
a b c 
a b c d 
a b c d e 
a b c d e f 
a b c d e f g 
a b c d e f g h 
a b c d e f g h i 
a b c d e f g h i j 
a b c d e f g h i j k 
a b c d e f g h i j k l 
a b c d e f g h i j k l m 
a b c d e f g h i j k l m n 
a b c d e f g h i j k l m n o 
a b c d e f g h i j k l m n o p 
a b c d e f g h i j k l m n o p q 
a b c d e f g h i j k l m n o p q r 
a b c d e f g h i j k l m n o p q r s 
a b c d e f g h i j k l m n o p q r s t 
a b c d e f g h i j k l m n o p q r s t u 
a b c d e f g h i j k l m n o p q r s t u v 
a b c d e f g h i j k l m n o p q r s t u v w 
a b c d e f g h i j k l m n o p q r s t u v w x 
a b c d e f g h i j k l m n o p q r s t u v w x y 
a b c d e f g h i j k l m n o p q r s t u v w x y z 


#nested for each loop
#       0         1          2
coll=[['a','x'],['b','y'],['c','z']]
        0   1     0 1       0   1
print(coll)


#nested for each loop
coll=[['a','x'],['b','y'],['c','z']]
for x in coll:
    for y in x:
        print(x) 

#while loop

from sys import meta_path


#performs with checking comditions it means until a condition is met

#while loop
x=1
while x<=5:
    print(x)
    x=x+1

import time

while True:
    time.sleep(1)
    print('hello')

import time
x=1
while True:
  print('counter :',x)
  x=x+1
  time.sleep(1)
  if(x>=10):
    print('ur session is completed..')
    break

import time

while True:
  print('enter 1 for add :')
  print('enter 2 for edit :')
  print('enter 3 for delete :')
  choice= input('enter ur choice :')
  if choice=='1':
    print('new account opened')
  elif choice=='2':  
    print('ur account edited')
  elif choice=='3':
    print('ur account deleted')
  else: 
    print('error / enter valid option')  
  option= input('do you like to continue again :')
  if option in ['Y' , 'y', 'Yes', 'ok', 'OK' , 'OKAY']:
    continue
  elif option in ['N' , 'n', 'NO', 'no', 'NOPE']:
    break'''


import time

while True:
  print('enter 1 for add :')
  print('enter 2 for edit :')
  print('enter 3 for delete :')
  choice= input('enter ur choice :')
  if choice=='1':
    print('new account opened')
  elif choice=='2':  
    print('ur account edited')
  elif choice=='3':
    print('ur account deleted')
  else: 
    print('error / enter valid option')  
  option= input('do you like to continue again :')
  if option in ['Y' , 'y', 'Yes', 'ok', 'OK' , 'OKAY']:
    continue
  elif option in ['N' , 'n', 'NO', 'no', 'NOPE']:
    break

