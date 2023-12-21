#set 

import sys
'''
teamA= {'a','b','c','d','q'}
teamB= {'a','b','c','d','k'}
#get result from the above two set item not match from teamA to teamB and teamB to teamA
print(teamA.difference(teamB))
print(teamA.symmetric_difference(teamB))
print(teamB.difference(teamA))

teamA= {'a','b','c','d','q'}
#add 'k' if not in teamA use if statement also
if 'k' not in teamA:
  teamA.add('k')
print(teamA)

teamA= {'a','b','c','d','q'}
#replace 'x' in place of c
teamA.remove('c')
teamA.add('x')
print(teamA)

teamA={'rakesh','rama', 'dama', 'sama'}
teamB={'rakesh', 'rama'}
#find out which is superset and which is subset
print(teamA.issuperset(teamB))
print(teamA.issubset(teamB))

teamA = {'rakesh', 'rama', 'dama', 'sama'}
teamB = {'rakesh', 'rama'}

# Check if teamA is a superset of teamB
if teamA.issuperset(teamB):
    print('teamA is a superset of teamB')

# Check if teamB is a subset of teamA
if teamB.issubset(teamA):
    print('teamB is a subset of teamA')


teamA = {'rakesh', 'rama', 'dama', 'sama'}
teamB = {'rakesh', 'rama'}
#find candidate present in both team and display all candidate names and number of candidates
print(teamA.intersection(teamB))
print(len(teamA.intersection(teamB)))
all_candidates = teamA.union(teamB)
toatal_num_of_candidates = len(teamA.union(teamB))
print(all_candidates)
print(toatal_num_of_candidates)

teamA = {'rakesh', 'rama', 'dama', 'sama'}
teamB = {'rakesh', 'rama'}
update= teamA.update(teamB)

#write any program using difference update
teamA = {'rakesh', 'rama', 'dama', 'sama'}
teamB = {'rakesh', 'rama'}
update= teamA.difference_update(teamB)
print(teamA)
print(update)

#write any program using symmetric difference update
teamA = {'rakesh', 'rama', 'dama', 'sama'}
teamB = {'rakesh', 'rama'}
update= teamA.symmetric_difference_update(teamB)
print(teamA)
print(update)


set1={1,2,4,9,6,3}
#convert and assign  to list
List1=list(set1)
print(List1)
#sort List1 in ascending order
List2=sorted(List1)
print(List2)
#sort  in descending order
List3=sorted(List1,reverse=True)
print(List3)
#assign List3 to set1
set1=set(List3)
print(set1)



#write any program to identify whether a set is unsort and not indexed

#set is by default unsorted and not in index

#declare set with three candidates with id,name,skillset, status record in a set and display all record with scalar type



# Set of candidate records
candidate_records = [
    {"id": 1, "name": "John", "skillset": {"Python", "Java"}, "status": "Active"},
    {"id": 2, "name": "Alice", "skillset": {"JavaScript",}, "status": "Inactive"},
    {"id": 3, "name": "Bob", "skillset": {"C++", "Python"}, "status": "Active"}
]

# Display all records with scalar type
for candidate in candidate_records:
    print(f"ID: {candidate['id']}, Name: {candidate['name']}, Skillset: {', '.join(candidate['skillset'])}, Status: {candidate['status']}")

class Candidate:
  def __init__(self, candidate_id, name, skillset, status):
      self.id = candidate_id
      self.name = name
      self.skillset = tuple(skillset)  # Convert skillset to a tuple for hashability
      self.status = status

  def display_info(self):
      skillset_str = ', '.join(self.skillset)
      return f"ID: {self.id}, Name: {self.name}, Skillset: {skillset_str}, Status: {self.status}"


# Set to store candidate records
candidate_records = set()

# Input candidate records
for i in range(1, 4):
  print(f"\nEnter details for Candidate {i}:")
  candidate_id = int(input("Enter ID: "))
  candidate_name = input("Enter Name: ")
  candidate_skillset = set(input("Enter Skillset (comma-separated): ").split(','))
  candidate_status = input("Enter Status: ")

  # Create a Candidate object and add it to the set
  candidate = Candidate(candidate_id, candidate_name, candidate_skillset, candidate_status)
  candidate_records.add(candidate)

# Display all records using scalar types
for candidate in candidate_records:
  print(candidate.display_info())


#write a program to create a set with number 1 to 10

number_set = set(range(1, 11))

print("Set with numbers from 1 to 10:", number_set)


#write a program to check number of prime numbers in a set

def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True
number_set = {2, 3, 5, 7, 11, 14, 17, 20}
prime_count = sum(1 for num in number_set if is_prime(num))
print("Set:", number_set)
print("Number of prime numbers in the set:", prime_count)

#write a program to copy all the even numbers from one set to another set

# Function to copy even numbers from one set to another set
def copy_even_numbers(source_set):
    even_numbers_set = {num for num in source_set if num % 2 == 0}
    return even_numbers_set

# Get user input for the set of numbers (comma-separated)
numbers_input = input("Enter numbers separated by commas: ")

# Convert the input string to a set of integers
original_set = {int(num) for num in numbers_input.split(',')}

# Copy even numbers to a new set
even_numbers_set = copy_even_numbers(original_set)

# Display the original set and the set of even numbers
print("Original Set:", original_set)
print("Set of Even Numbers:", even_numbers_set)'''

setA= {'x','y','z'}
setB={'x','y','q'}
result=setA.symmetric_difference(setB)
print(result)
search= input('data :')
if search in result :
  print ('data found:', search)






