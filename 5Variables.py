#python supports variable with dynamic type ; size type at runetime

x=10 # x is the variable with int value
y='you' # y is the variable with str value
print(x, type(x))
print(y,type(y))
#type function returns class name of respective type

#python also supports multiple variable initialisation with same value

x=y=z=10
print(x,y,z)


#Variable with memory addess as per value

x=y=z=10
print(x,y,z)
print (id(x))
print (id(y))
print (id(z))

x = y = z = 20
print(x, y, z)
print(*(id(var) for var in (x, y, z)))


#variable can be local or global

#local variable scope within function

def abacus():
  x='python' #local variable
  print(x)
def atos():
  print(x)


# global variables

x='python'
def abacus():
  print(x)

def atos():
  print(x)

abacus()
atos()