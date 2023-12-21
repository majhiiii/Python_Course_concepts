#import array as arr
from re import search
'''
ds= arr.array( 'i', [1,2,3,4,5,6,7,8,9,10,3])
print(ds)
for x in ds:
    print(x)'''
'''#search in array
search=int(input( "Enter the number to search: "))
if search in ds:
    print("The number is present in the array")
else:
    print("The number is not present in the array")

#append in array
ds.append(20)
print(ds)
for x in ds :
  print(x)

#insert in array
ds.insert(0,30)
print(ds)
for x in ds :
  print(x)'''

'''#sort in array
li=list(ds)
li.sort()
print(li)
li.sort(reverse=True)
print(li)
ds1=arr.array('i',li)
print(ds1)'''

'''#remove item as per the index
ds.pop(3)
print(ds)
for x in ds :
  print(x)

#remove specified item only from first 

ds.remove(3)
print(ds)
for x in ds :
  print(x)'''

'''
#clear
ds.clear()
print(ds)
for x in ds :
  print(x)

#del
del ds
print(ds)
for x in ds :
  print(x)'''

'''#slice in array

ds1=ds[3:6]
print(ds1)
for x in ds1 :
  print(x)'''

'''ids=arr.array('i',[1,2,3,4,5,6,7,8,9,10,3])
sal=arr.array('d',[1,2,3,4,5,6,7,8,9,10,3])
rating=arr.array('d',[1,2,3,4,5,6,7,8,9,10,3])
for x in range(len(ids)):
    print('ids :',ids[x],'sale :',sal[x],'ratings :',rating[x])
'''


'''def is_palindrome(s):
  return s == s[::-1]

def array_operations(arr):
  # Finding the midpoint of the array
  midpoint = len(arr) // 2

  # Finding the average, min, and max of the left side of the midpoint
  left_side = arr[:midpoint]
  avg_left = sum(left_side) / len(left_side) if len(left_side) > 0 else 0
  min_left = min(left_side) if len(left_side) > 0 else float('inf')
  max_left = max(left_side) if len(left_side) > 0 else float('-inf')

  # Checking if elements on the right side of the midpoint are palindromes
  right_side = arr[midpoint + 1:]
  right_palindromes = [is_palindrome(str(x)) for x in right_side]

  return {
      'midpoint': midpoint,
      'avg_left': avg_left,
      'min_left': min_left,
      'max_left': max_left,
      'right_palindromes': right_palindromes
  }

# Taking user input for the array
input_array = input("Enter the array elements separated by spaces: ")
input_array = list(map(int, input_array.split()))

result = array_operations(input_array)
print("Midpoint:", result['midpoint'])
print("Average of left side:", result['avg_left'])
print("Minimum of left side:", result['min_left'])
print("Maximum of left side:", result['max_left'])
print("Are elements on the right side palindromes?", result['right_palindromes'])'''


'''
def is_palindrome(s):
  return s == s[::-1]

def array_operations(arr):
  # Finding the midpoint of the array
  midpoint = len(arr) // 2

  # Slicing the array into left and right sides
  left_side = arr[:midpoint]
  right_side = arr[midpoint + 1:]

  # Calculate average, minimum, and maximum of the left side
  if left_side:
      average_left = sum(left_side) / len(left_side)
      min_left = min(left_side)
      max_left = max(left_side)
  else:
      # If left side is empty, set defaults
      average_left = 0
      min_left = float('inf')
      max_left = float('-inf')

  # Get the element present at the midpoint
  midpoint_element = arr[midpoint] if len(arr) % 2 != 0 else None

  # Check for palindromes in the right side
  right_palindromes = [is_palindrome(str(x)) for x in right_side]

  return {
      'midpoint': midpoint,
      'midpoint_element': midpoint_element,
      'avg_left': average_left,
      'min_left': min_left,
      'max_left': max_left,
      'right_palindromes': right_palindromes
  }

# Taking user input for the array
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = array_operations(input_array)

# Displaying results
print("Midpoint:", result['midpoint'])
print("Element at the midpoint:", result['midpoint_element'])
print("Average of left side:", result['avg_left'])
print("Minimum of left side:", result['min_left'])
print("Maximum of left side:", result['max_left'])
print("Are elements on the right side palindromes?", result['right_palindromes'])'''


'''
def is_palindrome(s):
  return s == s[::-1]

def array_operations(arr):
  # Finding the midpoint of the array
  midpoint = len(arr) // 2

  # Slicing the array into left and right sides
  left_side = arr[:midpoint]
  right_side = arr[midpoint + 1:]

  # Calculate average, minimum, and maximum of the left side
  if left_side:
      average_left = sum(left_side) / len(left_side)
      min_left = min(left_side)
      max_left = max(left_side)
  else:
      # If left side is empty, set defaults
      average_left = 0
      min_left = float('inf')
      max_left = float('-inf')

  # Get the element present at the midpoint
  midpoint_element = arr[midpoint] if len(arr) % 2 != 0 else None
  if len(arr) % 2 != 0:
    midpoint_element = arr[midpoint]
  else:
    midpoint_element = None

  # Concatenate the elements on the right side to form a number
  right_number = int(''.join(map(str, right_side))) if right_side else 0
  is_right_palindrome = is_palindrome(str(right_number))

  if right_side:
      right_number = int(''.join(map(str, right_side)))
  else:
      right_number = 0

  is_right_palindrome = is_palindrome(str(right_number))

  return {
      'midpoint': midpoint,
      'midpoint_element': midpoint_element,
      'avg_left': average_left,
      'min_left': min_left,
      'max_left': max_left,
      'right_number': right_number,
      'is_right_palindrome': is_right_palindrome
  }
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))

result = array_operations(input_array)

print("Midpoint:", result['midpoint'])
print("Element at the midpoint:", result['midpoint_element'])
print("Average of left side:", result['avg_left'])
print("Minimum of left side:", result['min_left'])
print("Maximum of left side:", result['max_left'])
print("Number formed by elements on the right side:", result['right_number'])
print("Is the number formed by right side elements a palindrome?", result['is_right_palindrome'])
'''

'''import array

def is_palindrome(s):
    return s == s[::-1]

input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))

arr = array.array('i', input_array)

midpoint = len(arr) // 2

left_side = arr[:midpoint]
right_side = arr[midpoint + 1:]

if left_side:
    average_left = sum(left_side) / len(left_side)
    min_left = min(left_side)
    max_left = max(left_side)
else:
    average_left = 0
    min_left = float('inf')
    max_left = float('-inf')

if len(arr) % 2 != 0:
    midpoint_element = arr[midpoint]
else:
    midpoint_element = None

if right_side:
    right_number = int(''.join(map(str, right_side)))
else:
    right_number = 0

is_right_palindrome = is_palindrome(str(right_number))

print("Midpoint:", midpoint)
print("Element at the midpoint:", midpoint_element)
print("Average of left side:", average_left)
print("Minimum of left side:", min_left)
print("Maximum of left side:", max_left)
print("Number formed by elements on the right side:", right_number)
print("Is the number formed by right side elements a palindrome?", is_right_palindrome)'''
'''
import array

arr=[]
row,cols=5,5
for i in range(row):
  col=[]
  for j in range(cols):
    col.append(0)
  arr.append(col)

print(arr)'''

'''import array

arr = array.array('i')  # Create an empty array of integers

row, cols = 5, 5

for i in range(row):
    col = input().split()  # Split the input into separate strings
    for val in col:
        arr.append(int(val))  # Convert each string to an integer and append to the array

print(arr)
'''

twod=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(twod)):
  for j in range(len(twod[i])):
    print(twod[i][j])