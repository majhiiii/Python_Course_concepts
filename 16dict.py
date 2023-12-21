import sys
#Dict
#what is dict
#dict is a collection of key-value pairs


'''emp={'id:' : 1, 'name': 'John', 'salary': 10000}
for x in emp.keys():
  print(x,emp[x])
for x in emp.values():
  print(x)

  
emp={ 'id ': 1, 'name': 'rakesh', 'city': 'bbsr'}
for x,y in emp.items():
  print('keys :', x, 'values : ',y)
emp.update({'info': 'good'})
print(emp)
for x,y in emp.items():
  print('keys :', x, 'values : ',y)
emp.pop('id ')
print(emp)
emp.clear()
print(emp)
emp.popitem()
print(emp)
if 'id ' in emp:
  print('present')
else: 
  print('no such item')


#collection in dict

emp={'names': ['rakesh', 'john', 'mike'], 'age': ['25', '30', '35'], 'city': ['bbsr', 'bbsr', 'bbsr']}
print(emp)
print(emp.get('names'))
print(emp.get('age'))
print(emp.get('city'))


emp={ 'id':1, 'name': 'rakesh', 'city': 'bbsr'}
emp['state']= 'odisha'
print(emp)
items=emp.items()
print(items)
for x,y in items:
  print(x,y)

keys=emp.keys()
print(keys)
values=emp.values()
print(values)

key=input('enter key : ')
if key in keys:
  print('found')
else: 
  print('not found')
  

#dic with scalar type or user defined type

class product:
  def __init__(self, id, name, price):
    self.id=id
    self.name=name
    self.price=price
ob=product(1, 'book', 500)
ob1=product(2, 'pen', 20)
ob2=product(3, 'pencil', 10)
product_dict={'book':ob, 'pen':ob1, 'pencil':ob2}
info1=product_dict.get('book')
print(info1.id, info1.name, info1.price)
info2=product_dict.get('pen')
print(info2.id, info2.name, info2.price)
info3=product_dict.get('pencil')
print(info3.id, info3.name, info3.price)


class Product:
  def __init__(self, id, name, price):
      self.id = id
      self.name = name
      self.price = price

def add_product(products, new_product):
  products.append(new_product)
  return products

def edit_product(products, product_id, new_name, new_price):
  for product in products:
      if product.id == product_id:
          product.name = new_name
          product.price = new_price
          break
  return products

def delete_product(products, product_id):
  products = [product for product in products if product.id != product_id]
  return products

def search_product(products, product_id):
  for product in products:
      if product.id == product_id:
          return product
  return None

ob = Product(1, 'book', 500)
ob1 = Product(2, 'pen', 20)
ob2 = Product(3, 'pencil', 10)

dept_products = [ob, ob1, ob2]
product_dict = {'products': dept_products}

print('Initial Product Details:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

new_product = Product(4, 'notebook', 250)
product_dict['products'] = add_product(product_dict['products'], new_product)

print('\nAfter Adding a new product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

product_dict['products'] = edit_product(product_dict['products'], 2, 'red pen', 25)

print('\nAfter Editing a product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

product_dict['products'] = delete_product(product_dict['products'], 1)

print('\nAfter Deleting a product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

searched_product = search_product(product_dict['products'], 3)
if searched_product:
  print(f"\nFound: {searched_product.id}, {searched_product.name}, {searched_product.price}")
else:
  print("\nProduct not found.")'''

class Product:
  def __init__(self, id, name, price):
      self.id = id
      self.name = name
      self.price = price

def add_product(products, new_product):
  products.append(new_product)
  return products

def edit_product(products, product_id, new_name, new_price):
  for product in products:
      if product.id == product_id:
          product.name = new_name
          product.price = new_price
          break
  return products

def delete_product(products, product_id):
  products = [product for product in products if product.id != product_id]
  return products

def search_product(products, product_id):
  for product in products:
      if product.id == product_id:
          return product
  return None


ob = Product(1, 'book', 500)
ob1 = Product(2, 'pen', 20)
ob2 = Product(3, 'pencil', 10)

dept_products = [ob, ob1, ob2]
product_dict = {'products': dept_products}

print('Initial Product Details:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

# adding a new product
new_id = int(input("\nEnter ID for the new product: "))
new_name = input("Enter name for the new product: ")
new_price = float(input("Enter price for the new product: "))

new_product = Product(new_id, new_name, new_price)
product_dict['products'] = add_product(product_dict['products'], new_product)

print('\nAfter Adding a new product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

# editing a product
edit_id = int(input("\nEnter ID of the product to edit: "))
new_name = input("Enter new name for the product: ")
new_price = float(input("Enter new price for the product: "))

product_dict['products'] = edit_product(product_dict['products'], edit_id, new_name, new_price)

print('\nAfter Editing a product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

# deleting a product
delete_id = int(input("\nEnter ID of the product to delete: "))

product_dict['products'] = delete_product(product_dict['products'], delete_id)

print('\nAfter Deleting a product:')
for product in product_dict['products']:
  print(f"{product.id}, {product.name}, {product.price}")

#  searching a product
search_id = int(input("\nEnter ID of the product to search: "))

searched_product = search_product(product_dict['products'], search_id)
if searched_product:
  print(f"\nFound: {searched_product.id}, {searched_product.name}, {searched_product.price}")
else:
  print("\nProduct not found.")
