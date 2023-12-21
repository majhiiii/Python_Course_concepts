#recursion using function
'''def fact(x):
    if x == 1:
        return 1

    else:
        return x*fact(x-1)
if __name__ == '__main__' :
        range_= int(input('enter your range : '))
        for x in range(1,range_,1):
          print('no :',x, 'factorial :',fact(x))


#keyword argument
def func(**kwargs):
  print(kwargs)
  print(kwargs['name'])
  print(kwargs['age'])
func(name='shubham',age=20)

#arbitary argument
def func(*args):
  print(args)
func(1,2,3,4,5,6,7,8,9,10)

#keyword arbitary argument
def func(**kwargs):
  print(kwargs)
  print(kwargs['name'])
  print(kwargs['age'])
func(name='shubham',age=20)

#keyword arbitary argument arg=dict
def process_arguments(**kwargs):
  for key, value in kwargs.items():
      print(f"Key: {key}, Value: {value}")
arg_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
process_arguments(**arg_dict)


teama={'a','b','c'}
teamb={'x','y','z'}
result= teama.symmetric_difference(teamb)
print(result)
f1=frozenset(result)
print(f1)

#write a program that takes starting number and ending number and print the numbers 
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

numbers_list = []

print("Numbers between", start_num, "and", end_num, "are:")
for num in range(start_num, end_num + 1):
    numbers_list.append(num)

print("List of numbers:", numbers_list)
min_num = min(numbers_list)
max_num = max(numbers_list)
sum_nums = sum(numbers_list)
avg_num = sum_nums / len(numbers_list)
count_nums = len(numbers_list)

print("Minimum:", min_num)
print("Maximum:", max_num)
print("Sum:", sum_nums)
print("Average:", avg_num)
print("Count:", count_nums)

def generate_numbers_list(start, end):
  numbers_list = list(range(start, end+1 , 1))
  return numbers_list

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

numbers = generate_numbers_list(start_number, end_number)

print("Numbers between", start_number, "and", end_number, "are:")
print(numbers)
min_num = min(numbers)
print(f"min of the numbers: {min_num}")
max_num = max(numbers)
print(f"max of the numbers: {max_num}")
sum_nums = sum(numbers)
print(f"sum of the numbers: {sum_nums}")
avg_num = sum_nums / len(numbers)
print(f"Average of the numbers: {avg_num}")
count_nums = len(numbers)
print(f"count of the numbers: {count_nums}")


def generate_numbers_list(start, end):
  numbers_list = list(range(start, end + 1))
  return numbers_list

def input_additional_numbers(numbers):
  print("Enter 10 additional numbers:")
  for _ in range(10):
      num = int(input("Enter a number: "))
      numbers.append(num)
  return numbers

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

numbers = generate_numbers_list(start_number, end_number)

print("Numbers between", start_number, "and", end_number, "are:")
print(numbers)
min_num = min(numbers)
print(f"min of the numbers: {min_num}")
max_num = max(numbers)
print(f"max of the numbers: {max_num}")
sum_nums = sum(numbers)
print(f"sum of the numbers: {sum_nums}")
avg_num = sum_nums / len(numbers)
print(f"Average of the numbers: {avg_num}")
count_nums = len(numbers)
print(f"count of the numbers: {count_nums}")

continue_input = input("Do you want to continue? (yes/no): ")

if continue_input.lower() == "yes":
  numbers = input_additional_numbers(numbers)
  print("Updated numbers list:", numbers)
  min_num = min(numbers)
  print(f"min of the updated numbers: {min_num}")
  max_num = max(numbers)
  print(f"max of the updated numbers: {max_num}")
  sum_nums = sum(numbers)
  print(f"sum of the updated numbers: {sum_nums}")
  avg_num = sum_nums / len(numbers)
  print(f"Average of the updated numbers: {avg_num}")
  count_nums = len(numbers)
  print(f"count of the updated numbers: {count_nums}")
else:
  print("Exiting the program.")

numbers = []
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# Generating numbers between start_number and end_number
numbers.extend(range(start_number, end_number + 1))

print("Numbers between", start_number, "and", end_number, "are:")
print(numbers)

min_num = min(numbers)
print(f"min of the numbers: {min_num}")

max_num = max(numbers)
print(f"max of the numbers: {max_num}")

sum_nums = sum(numbers)
print(f"sum of the numbers: {sum_nums}")

avg_num = sum_nums / len(numbers)
print(f"Average of the numbers: {avg_num}")

count_nums = len(numbers)
print(f"count of the numbers: {count_nums}")

continue_input = input("Do you want to continue? (yes/no): ")

if continue_input.lower() == "yes":
    print("Enter 10 additional numbers:")
    for _ in range(10):
        num = int(input("Enter a number: "))
        numbers.append(num)

    print("Updated numbers list:", numbers)

    min_num = min(numbers)
    print(f"min of the updated numbers: {min_num}")

    max_num = max(numbers)
    print(f"max of the updated numbers: {max_num}")

    sum_nums = sum(numbers)
    print(f"sum of the updated numbers: {sum_nums}")

    avg_num = sum_nums / len(numbers)
    print(f"Average of the updated numbers: {avg_num}")

    count_nums = len(numbers)
    print(f"count of the updated numbers: {count_nums}")
else:
    print("Exiting the program.")

numbers = []
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# Generating numbers between start_number and end_number
numbers.extend(range(start_number, end_number + 1))

print("Numbers between", start_number, "and", end_number, "are:")
print(numbers)

min_num = min(numbers)
print(f"min of the numbers: {min_num}")

max_num = max(numbers)
print(f"max of the numbers: {max_num}")

sum_nums = sum(numbers)
print(f"sum of the numbers: {sum_nums}")

avg_num = sum_nums / len(numbers)
print(f"Average of the numbers: {avg_num}")

count_nums = len(numbers)
print(f"count of the numbers: {count_nums}")

continue_input = input("Do you want to continue? (yes/no): ")

if continue_input.lower() == "yes":
    print("Enter 10 additional numbers separated by commas:")
    # Taking input of 10 additional numbers separated by commas
    additional_input = input("Enter 10 numbers separated by commas: ")

    # Splitting the input string by commas and converting it into a list of integers
    additional_numbers = [int(num) for num in additional_input.split(',')]

    # Extending the existing numbers list with the additional numbers
    numbers.extend(additional_numbers)

    print("Updated numbers list:", numbers)

    min_num = min(numbers)
    print(f"min of the updated numbers: {min_num}")

    max_num = max(numbers)
    print(f"max of the updated numbers: {max_num}")

    sum_nums = sum(numbers)
    print(f"sum of the updated numbers: {sum_nums}")

    avg_num = sum_nums / len(numbers)
    print(f"Average of the updated numbers: {avg_num}")

    count_nums = len(numbers)
    print(f"count of the updated numbers: {count_nums}")
else:
    print("Exiting the program.")'''









      