x='python'
def abacus(x):
    print(x)

def atos(x):
    print(x)

# Define the value of x

# Call the functions with the variable x as an argument
abacus(x)
atos(x)


#global varibale within function

def abacus():
  global x
  x='python'
  print(x)
def atos():
  print(x)

abacus()
atos()
print(x)
  