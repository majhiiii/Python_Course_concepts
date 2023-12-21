#operators in python like 
#1.Concatenate : connecting strings
#2.Arithmetic : +-*/
'''x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x+y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x-y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x*y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x/y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x%y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x//y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
x=int(input('enter 1st no:'))
y=int(input('enter 2nd no:'))
z=x**y
result='x value {0} y value{1} final value{2}'.format(x,y,z)
print(result)
pname=input('enter product name : ')
ptype=input('enter product type : ')
pcost=float(input('enter product cost : '))
gst=pcost*10/100
total= pcost+gst
result='--------\n sales report \n----------'
print(result)
bill='pname {0} \n ptype{1} \n pcost{2} \n gst{3} \n grand total {4} '
print(bill.format(pname,ptype,str(pcost),str(gst),str(total)))
result='\n--------copyright to Wipro----------\n'
print(result)'''

#assignment operators
''''s='abacus'
s+=' Bhubaneswar'
s+=' Odisha '
print(s)
a=10
print(a)
a+=10
print(a)
a-=10
print(a)
a*=10
print(a)
a/=10
print(a)
a%=10
print(a)
a//=10
print(a)
a**=10
print(a)'''

#comparison operator or relational operator

''''uid_= input('enter ur name :')
pwd_=input('enter ur password:')
print(uid_=='you')
print(pwd_=='me')
uid_= input('enter ur name :')
pwd_=input('enter ur password:')
print(uid_!='you')
print(pwd_!='me')
status=True
print(status!=True)
cost=float(input('enter a cost:'))
gst=cost*10/10
total=cost+gst
result='cost={0} gst={1} total{2}'.format(cost,gst,total)
print(result)
cost=float(input('enter a cost:'))
gst=None
if cost>=200:
  gst=10
else: 
  gst=6
gstp=cost*gst/100
total=cost+gstp
print('gst on product:',str(gst)+'%')
result='cost={0} gst={1} total{2}'.format(cost,gst,total)
print(result)'''
#identity operator
'''x=10
y=10
print(x,y,id(x),id(y))
print(x is y)
x=10
y=11
print(x,y,id(x),id(y))
print(x is y)
x=10
y=10
print(x,y,id(x),id(y))
print(x is not y)
x=10
y=11
print(x,y,id(x),id(y))
print(x is not y)
x=[10]
y=[10]
print(x,y,id(x),id(y))
print(x is y)'''

#membership operator
''''s='i am rakesh majhi'
if 'rakesh' in s :
  print('found')
else: 
  print('not found')  
s='i am rakesh majhi'
if 'rakesh' not in s :
  print('found')
else: 
  print('not found')  

li=['rakesh', 'majhi', 'wipro', 'tcs']
search=input('enter search data: ')
if search in li:
  print('found')
else:
  print('not found') 

uid_= input('enter user name: ')
pwd_= input('enter ur password: ')
if (uid_ == 'rk'and pwd_== 'me') :
  print('thanks for log in')
else:
  print('invalid log in')
  
uid_= input('enter user name: ')
pwd_= input('enter ur password: ')
user_data='rk,pk,gk,ck,dk'
if (uid_ in user_data and pwd_== 'me') :
  print('thanks for log in')
else:
  print('invalid log in')
uid_= input('enter user name: ')
pwd_= input('enter ur password: ')
user_data='rk,pk,gk,ck,dk'
user_data1='sk,fk,mk'
if (uid_ in user_data or user_data1) and pwd_== 'me' :
  print('thanks for log in')
else:
  print('invalid log in')
uid_= input('enter user name: ')
pwd_= input('enter ur password: ')
user_data='rk,pk,gk,ck,dk'
user_data1='sk,fk,mk'
if (uid_ in user_data or user_data1) and pwd_== 'me' :
  print('thanks for log in')
else:
  print('invalid log in')
first= input('enter city name: ')
s1= 'delhi,mumbai,'
s2= 'bbsr,kolkata'
if first in s1 or first in s2:
  print('metrocity: ',first)
else:
  print('invalid city name')
city = input('Enter city name: ')
s1 = 'delhi,mumbai,'
s2 = 'bbsr,kolkata'

if city not in s1 or city not in s2:
    print('Metro city:', city)
else:
    print('Invalid city name')

x=input('enter option: ')
if x=='first':
  print('python')
else :
  print('no condtion satisfied')
  
x=input('enter option for day: ')
if x=='1':
  print('Monday')
elif x=='2':
  print('Tuesday')
elif x=='3':
  print('Wednesday')
elif x=='4':
  print('Thursday')
elif x=='5':
  print('Friday')
elif x=='6':
  print('Saturday')
  data==input('enter your choice: ')
  if data=='ok':
    print('transaction read:')
  elif data=='cancel':
    print('transaction cancelled')
  else : print('no transaction')  
elif x=='7':
  print('Sunday')
else:  
  print('no condtion satisfied')'''

ptype=input('enter product type : ')
cost=float(input('enter product cost : '))
gst= 0.0
total= 0.0
gstp=' '
if ptype=='elect':
  gstp='12%'
elif ptype=='food':
  gstp='10%'
elif ptype=='Jewel':
  gstp='18%'
elif ptype=='Edu':
  gstp='14%'
elif ptype=='cloth':
  gstp='12%'
else : gstp='00%'
gst_=int(gstp.strip('%'))  
gst= (cost*gst_/100)
total= cost+gst
print('----------------------------------------------------')
print('product type: ',ptype)
print('product cost: ',cost)
print('gst: ',gst)
print('----------------------------------------------------')
print('total: ',total)