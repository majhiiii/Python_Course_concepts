'''li=['a', 'b', 'c', 'd', 'e', 'q']
li1=(li[1:-2])
search_elements = ['b']

desired_element = [element for element in search_elements if element in li1]

print("Desired elements:", desired_element)

li=['a','b','c','d','e']
# Copy elements from index 2 to index 4 using list comprehension
copied_elements = [li[i] for i in range(2, 5)]

print("Copied elements:", copied_elements)


class emp:
  id_=1
  name_='Myself'
  sal_=23000
ob=emp()
ob1=emp()
ob1.id_=2
ob1.name_='rani'
ob1.sal_=45000
ob2=emp()
ob2.id_=3
ob2.name_='sai'
ob2.sal_=83000
ob3=emp()
ob3.id_=4
ob3.name_='rakesh'
ob3.sal_=93000
ds=[ob,ob1,ob2,ob3]

below_standard = [x for x in ds if x.sal_ < 40000]
normal_standard = [x for x in ds if x.sal_ < 50000]
taxable_standard = [x for x in ds if x.sal_ > 50000]
 
print("Below Standard:")
for x in below_standard:
  print(x.id_,x.name_,x.sal_)
print('-----------------')
print("Normal Standard:")
for x in normal_standard:
  print(x.id_,x.name_,x.sal_)
print('-----------------')
print("Taxable Standard:")
for x in taxable_standard:
  print(x.id_,x.name_,x.sal_)




tu=('a','b','c','d')
#add x at the first of the tuple
tu=('x',)+tu
#add y at the end of the tuple
tu=tu+('y',)
#add m in the middle of the tuple
tu=tu[:2]+('m',)+tu[2:]
print(tu)

tu=('a','b','c','d')
tu1=copy.deep(tu)
print(tu1)
'''
#crud in list for product{pid,pname,pcost,ptype}

products = [
    {"pid": 1, "pname": "Product A", "pcost": 50, "ptype": "Type1"},
    {"pid": 2, "pname": "Product B", "pcost": 30, "ptype": "Type2"},
    {"pid": 3, "pname": "Product C", "pcost": 70, "ptype": "Type1"}
]

# Create :
def create_product():
    pid = int(input("Enter product ID: "))
    pname = input("Enter product name: ")
    pcost = float(input("Enter product cost: "))
    ptype = input("Enter product type: ")
    new_product = {"pid": pid, "pname": pname, "pcost": pcost, "ptype": ptype}
    products.append(new_product)
    print("Product added successfully.")

# Read :
def read_products():
    print("List of products:")
    for product in products:
        print(f"ID: {product['pid']}, Name: {product['pname']}, Cost: {product['pcost']}, Type: {product['ptype']}")

# Update :
def update_product():
    update_pid = int(input("Enter product ID to update: "))
    for product in products:
        if product["pid"] == update_pid:
            product["pname"] = input("Enter updated product name: ")
            product["pcost"] = float(input("Enter updated product cost: "))
            product["ptype"] = input("Enter updated product type: ")
            print("Product updated successfully.")
            return
    print("Product not found")

# Delete
def delete_product():
    delete_pid = int(input("Enter product ID to delete: "))
    global products
    products = [product for product in products if product["pid"] != delete_pid]
    print("Product deleted successfully")

while True:
    print("\nOptions:")
    print("1. Create Product")
    print("2. Read Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_product()
    elif choice == "2":
        read_products()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid input")



