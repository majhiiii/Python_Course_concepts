import math
import sys 
#generator in python
'''def names():
  yield 'x'
  yield 1
  yield True
  yield 11.4
print(type(names()))  
print(id(names()))  
for name in names():
  print(name)
'''

#generator object
'''def names():
  yield 'x'
  yield 1
  yield True
  yield 11.4
if __name__== '__main__':
  ob=names()
  print(type(ob))
  print(id(ob))
  print(sys.getsizeof(ob))
  for name in ob:
    print(name)'''


#next function
'''def names():
  yield 'x'
  yield 1
  yield True
  yield 11.4
if __name__== '__main__':
  ob=names()
  print(type(ob))
  print(id(ob))
  print(sys.getsizeof(ob))
  print(next(ob))
  print(next(ob))
  print(next(ob))'''

'''def names():
  for x in range (1,100,1):
    if x%2==0:
      yield x
    else:
      yield x*2  
if __name__== '__main__':
  ob=names()
  print(type(ob))
  print(id(ob))
  print(sys.getsizeof(ob))
  for name in names():
    print(name)'''


'''ds=[x for x in range (65,90,1)]
ds1=[chr(x) for x in range (65,90,1)]
def names():
  for x in range (0,25,1):
    if x%2==0:
      yield 'asci :' + str(ds[x])
    else:
      yield 'char :' + str(ds1[x])
if __name__== '__main__':
  ob=names()
  print(type(ob))
  print(id(ob))
  print(sys.getsizeof(ob))
  for name in names():
    print(name)'''

'''ds=[x for x in range (65,90,1)]
ds1=[chr(x) for x in range (65,90,1)]
def names():
  for x in range (0,25,1):
    if x%2==0:
      yield math.pow(x,2)
    else:
      yield math.sqrt(x)
if __name__== '__main__':
  ob=names()
  print(type(ob))
  print(id(ob))
  print(sys.getsizeof(ob))
  for name in names():
    print(name)'''



'''ds=['rakesh','bibek', 'sai', 'xyz', 'ankit', 'sipu', 'shubh', ]
def names():
  for x in range (0,len(ds),1):
    if x%2==0:
      yield 'even names :' + str(ds[x])
    else:
      yield 'odd names :' + str(ds[x])
if __name__== '__main__':
  ob=names()
  print('-------------------')
  for name in names():
    print(name)'''



'''ds=[['rakesh','bibek', 'sai', 'xyz', 'ankit', 'sipu', 'shubh' ],['abacus','calculator','watch','clock'],['a','b','c']]
def names():
  for x in ds:
    yield x
if __name__== '__main__':
  ob=names()
  print('-------------------')
  for name in names():
    print(name)
'''

#generator with scalar type
'''class message:
 from_= None
 to_=None
 msg_=None

ob=message()
ob.from_='rakesh'
ob.to_='bibek'
ob.msg_='hello'
ob1=message()
ob1.from_='rakesh'
ob1.to_='bibek'
ob1.msg_='kn karucha'
def names():
    yield ob
    yield ob1
if __name__== '__main__':
  result=names()
  print('-------------------')
  for name in result:
    print('from :',name.from_)
    print('to :',name.to_)
    print('msg :' ,name.msg_)'''

'''class Message:
  def __init__(self, from_, to_, msg_):
      self.from_ = from_
      self.to_ = to_
      self.msg_ = msg_

def create_message():
  messages = []
  for i in range(2):  # Creating two message instances, you can adjust this as needed
      from_ = input("Enter 'from' name: ")
      to_ = input("Enter 'to' name: ")
      msg_ = input("Enter message: ")
      message = Message(from_, to_, msg_)
      messages.append(message)
  return messages

if __name__ == '__main__':
  result = create_message()
  print('-------------------')
  for message in result:
      print('from :', message.from_)
      print('to :', message.to_)
      print('msg :', message.msg_)'''




#generator with method
#x=0
'''def disp():
  #x=x+1
  return 'hello :'
def f(x) :
  if (x==1):
    return 1
  else  :
    return x*f(x-1)
def names():
    for i in range (1,10,1):
      if i%2==0:
        yield f(i)
      else:
        yield disp()  
      
if __name__== '__main__':
  result=names()
  print('-------------------')
  for name in result:
      print(name)'''

'''def count_digits(number):
  return len(str(number))

def find_midpoint(number):
  num_str = str(number)
  length = len(num_str)
  midpoint_index = length // 2
  return midpoint_index, length

def find_max_right_side(number, midpoint):
  num_str = str(number)
  right_side = num_str[midpoint:]
  max_right = max(int(digit) for digit in right_side)
  return max_right

def find_min_left_side(number, midpoint):
  num_str = str(number)
  left_side = num_str[:midpoint]
  min_left = min(int(digit) for digit in left_side)
  return min_left

def is_prime(num):
  if num < 2:
      return False
  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
          return False
  return True

user_input = int(input("Enter a number: "))

num_digits = count_digits(user_input)
mid, length = find_midpoint(user_input)
max_right = find_max_right_side(user_input, mid)
min_left = find_min_left_side(user_input, mid)
result = min_left + max_right

print(f"Number of digits: {num_digits}")
print(f"Midpoint and Length: {mid} and {length}")
print(f"Max from right side: {max_right}")
print(f"Min from left side: {min_left}")
print(f"Sum of min and max: {result}")

if is_prime(result):
  print("The sum of min and max is a prime number.")
else:
  print("The sum of min and max is not a prime number.")
'''


def count_digits(number):
  return len(str(number))

def find_midpoint(number):
  num_str = str(number)
  length = len(num_str)
  midpoint_index = length // 2
  midpoint_value = int(num_str[midpoint_index])  
  return midpoint_index, length, midpoint_value

def find_max_right_side(number, midpoint):
  num_str = str(number)
  right_side = num_str[midpoint:]
  max_right = max(int(digit) for digit in right_side)
  return max_right

def find_min_left_side(number, midpoint):
  num_str = str(number)
  left_side = num_str[:midpoint]
  min_left = min(int(digit) for digit in left_side)
  return min_left

def is_prime(num):
  if num < 2:
      return False
  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
          return False
  return True

user_input = int(input('Enter a number: '))

num_digits = count_digits(user_input)
mid, length, midpoint_value = find_midpoint(user_input)
max_right = find_max_right_side(user_input, mid)
min_left = find_min_left_side(user_input, mid)
result = min_left + max_right

print(f"Number of digits: {num_digits}")
print(f"Midpoint and Length: {mid} and {length}")
print(f"Number at the midpoint: {midpoint_value}")
print(f"Max from right side: {max_right}")
print(f"Min from left side: {min_left}")
print(f"Sum of min and max: {result}")

if is_prime(result):
  print("The sum of min and max is a prime number")
else:
  print("The sum of min and max is not a prime number")
