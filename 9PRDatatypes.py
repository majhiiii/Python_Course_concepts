import sys 
''''x=1
print('value :',x, 'data type :',type(x),'address :',id(x),'size :', sys.getsizeof(x))
x=15464984894
print('value :',x, 'data type :',type(x),'address :',id(x),'size :', sys.getsizeof(x))
x=49894654654984
print('value :',x, 'data type :',type(x),'address :',id(x),'size :', sys.getsizeof(x))

s='10'
print(s,type(s))
x=int(s)
print(s)
print(type(s))'''

#boolean type contains value True or False. Default is always False 
#type name boolean class name bool conversion bool()


''''s=True
print(s,type(s))'''

''''s='false'
print(s,type(s), sys.getsizeof(s))
status=bool(s)
print(status, type(status),sys.getsizeof(status))
status=True
print(status, type(status),sys.getsizeof(status))

s='false'
print(s,type(s), sys.getsizeof(s))
status=bool(s)
print(status, type(status),sys.getsizeof(status))
status=False
print(status, type(status),sys.getsizeof(status))


ob=None
print(ob, type(ob),sys.getsizeof(ob),id(ob))
ob=1
print(ob, type(ob),sys.getsizeof(ob),id(ob))
ob=1.1
print(ob, type(ob),sys.getsizeof(ob),id(ob))
ob=True
print(ob, type(ob),sys.getsizeof(ob),id(ob))

string type is a collection that manages alphanumeric data as per index like
0 1 2 3 4 5
a b a c u s 

string type is common type takes any type data within string format.

s='abacus'
print(s)
print(len(s))
print(type(s))
print(id(s))
print(sys.getsizeof(s))


read data as per index

s='abacus'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print('---------')
print(len(s))
print('---------')
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])'''

#slice operation

''''
s='rakesh'
print(s[2:]) #2 onwards
print(s[:3]) #till 3
print(s[2:5])
print(s[-2])
print(s[-2:-5])
print(s[-5:-2])
print(s[::1])
print(s[::3])
print(s[::-2])
#string reverse
print(s[::-1])'''

#single line string
''''''ss="i am rakesh majhi"
print(ss)

#multi-line string

rk='''i am a student'''
rkm="""i am learning python"""
rkma="i " +\
     "am "+\
     "rakesh "
print(rk,rkm,rkma)

#escape sequence
"""\n: Newline. Inserts a newline character.
\t: Tab. Inserts a tab character.
\': Single Quote. Inserts a single quote character.
\": Double Quote. Inserts a double quote character.
\\: Backslash. Inserts a backslash character."""

''''r='i'
k='am'
m='rakesh'
sentence= r+k+m
print(sentence)
#string conversion using str

id_=1
name_='you'
status=False
skillset='AI'
result= str(id_)+' '+name_+' '+str(status)+' '+skillset
print(result)'''

#string format
id_=1
name_="you"
status=False
comp="TCS"
result='id {0} name{1} status{2} comp{3}'.format(id_,name_,status,comp )
print(result)


id_=None
name_=None
sal=0
id_=input('enter your id :')
name_=input('enter your name :')
sal=float(input('enter your id :'))
report='redg no : {0} name :{1} salary: {2}'.format(id_,name_,sal)
print(report)
