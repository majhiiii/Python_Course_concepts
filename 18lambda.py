#lambda
'''x= lambda x:x
print(x(10))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))'''


#lambda with collection type
'''x= lambda x:x
print(type(x))
print(x([1,2,3]))

print(x({'u','name','bbsr'}))'''

#lambda with user defined

'''x= lambda x:x

class product:
  p_id=1
  p_name='TV'
  p_cost= 3400

ob=product()
ob1=x(ob)
print(ob1.p_id,ob1.p_name,ob1.p_cost)
'''
# lambda with functio 
'''x= lambda x:x
def display(cost):
  return lambda gst, other: (cost+(cost*gst)+other)
result=display(float(input('enter the cost of product:')))(float(input('enter the gst:')),float(input('enter the other charges:')))
print(result)'''

'''saving= lambda amount, time : amount+(amount*4.5/100)
current= lambda amount, time : amount+(amount*2.5/100)
insurance= lambda amount, time : amount+(amount*5.5/100)
fixed= lambda amount, time : amount+(amount*6.5/100)
other= lambda amount, time : amount+(amount*3.5/100)

if __name__=='__main__':
  no=0
  while True:
    print('1 for saving:')
    print('2 for current:')
    print('3 for insurance:')
    print('4 for fixed:')
    print('5 for other:')
    option=str(input('enter the option:'))
    if option=='1':
      print('saving option:')
      amount=float(input('enter the amount:'))
      time=float(input('enter the time:'))
      result=saving(amount,time)
      print(f'Amount: {amount}, Time: {time}, Interest: {result - amount}, Balance: {result}')
    elif option=='2':
      print('current option:')
      amount=float(input('enter the amount:'))
      time=float(input('enter the time:'))
      result=current(amount,time)
      print(f'Amount: {amount}, Time: {time}, Interest: {result - amount}, Balance: {result}')
    elif option=='3':
      print('insurance option:')
      amount=float(input('enter the amount:'))
      time=float(input('enter the time:'))
      result=insurance(amount,time)
      print(f'Amount: {amount}, Time: {time}, Interest: {result - amount}, Balance: {result}')
    elif option=='4':
      print('fixed option:')
      amount=float(input('enter the amount:'))
      time=float(input('enter the time:'))
      result=fixed(amount,time)
      print(f'Amount: {amount}, Time: {time}, Interest: {result - amount}, Balance: {result}')
    elif option=='5':
      print('other option:')
      amount=float(input('enter the amount:'))
      time=float(input('enter the time:'))
      result=other(amount,time)
      print(f'Amount: {amount}, Time: {time}, Interest: {result - amount}, Balance: {result}')
    else:
      print('enter valid option')
    choice = input('Do you want to continue (y/n)? ')
    if choice.lower() == 'n':
        break
print('Thank you')'''


#lambda with str function
'''
import math
def fact(x):
  if x==1:
    return 1
  else:
    return x*fact(x-1)
result=fact(int(input('enter number :')))
print(result)

res= lambda no: fact(no) if (no%2==0) else no
for x in range(1,20,1):
  print('  ',res(x))'''

'''gst_rates = {
    'Elect': lambda amount: amount * (7 / 100),
    'Food': lambda amount: amount * (5 / 100),
    'Other': lambda amount: amount * (3 / 100)
}

def calculate_gst(category, amount):
    if category in gst_rates:
        return gst_rates[category](amount)
    else:
        return 0  

category = input("Enter category (Elect/Food/Other): ")
bill_amount = float(input("Enter bill amount: $"))

gst_amount = calculate_gst(category, bill_amount)
total_amount = bill_amount + gst_amount

print(f"Bill Amount: ${bill_amount}")
print(f"Category: {category}")
print(f"GST Amount: ${gst_amount}")
print(f"Total Amount (including GST): ${total_amount}")
'''

'''gst_rates = {
    '1': lambda amount: amount + (amount * 7 / 100),  # Electronic: 7%
    '2': lambda amount: amount + (amount * 5 / 100),  # Food: 5%
    '3': lambda amount: amount + (amount * 3 / 100)  # Other: 3%
}

def calculate_gst(category, amount):
    if category in gst_rates:
        result = gst_rates[category](amount)
        gst_amount = result - amount
        return result, gst_amount
    else:
        return None, None

if __name__ == '__main__':
    while True:
        print('1 for Electronic (7% GST)')
        print('2 for Food (5% GST)')
        print('3 for Other (3% GST)')
        category = input('Enter the category (1/2/3): ')

        if category not in ['1', '2', '3']:
            print('Please enter a valid category')
            continue

        amount = float(input('Enter the amount: $'))

        result, gst_amount = calculate_gst(category, amount)

        if result is not None and gst_amount is not None:
            print(f'Amount: {amount}')
            print(f'Category: {category}')
            print(f'GST Amount: {gst_amount}')
            print(f'Total Amount (including GST): {result}')

        choice = input('Do you want to continue (y/n)? ')
        if choice.lower() == 'n':
            break

    print('Thank you')'''


'''def gst(ptype,cost):
  if ptype== 'elect':
    return cost*10/100
  elif ptype== 'food':
    return cost*10/100
  else :
    return cost*3/100
gst_= lambda ptype,cost: gst(ptype,cost)
if __name__ == '__main__':
  print('----------------------')
  ptype=input('enter the product type:')
  cost=float(input('enter the cost:'))
  gst_amount=gst(ptype,cost)
  result='ptype {0} cost {1} gst{2} \n total {3}'.format(ptype,cost,gst_amount,cost+gst_amount)
  print('-------------------------')
  print(result)
  '''
    


'''s=[x for x in range(65,96,1)]
print(s)
for x in s :
  print('ascii value',x, 'char :', chr(x))'''


'''s=[chr(x) for x in range(65,96,1)]
print(s)
for x in s :
  print( 'char :', x,'ascii value',ord(x))'''

'''s = [chr(x) for x in range(65, 96, 1)]
print(s)

for x in s:
  ascii_value = ord(x)
  if ascii_value % 2 == 0:
      print('char:', x, 'ascii value:', ascii_value)'''

'''s = [x for x in range(65, 96, 1)]
print(s)
for x in s:
    if x % 2 == 0:
        print('ASCII value:', x, 'char:', chr(x))'''

'''s = [x for x in range(65, 96, 1) if x%2==0]
print(s)

for x in s:
   print('ASCII value:', x, 'char:', chr(x))
'''


'''s='abacus'
print(s.center(20))
print(s.center(20,'*'))

s=['abacus','rakesh','sai','bibek','ank']
for x in range(0,len(s)):
  print(s[x].center(20))'''

'''s= 'a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm'
print(s.expandtabs(1))
print(s.expandtabs(2))
print(s.expandtabs(3))
print(s.expandtabs(4))
print('--------------------')
for x in range (0,len(s),1):
  print(s.expandtabs(x))'''

'''s='abacus, atos, accenture'
search= input('enter name')
if s.find(search)==-1:
  print('not found')
else:
  print('found')
  
s='abacus, atos, accenture'
search= input('enter name')
print(s.index(search))
'''

'''s='http://www.google.com'
if(s.startswith('http')==True):
  print('yes')
else:
  print('no')'''

