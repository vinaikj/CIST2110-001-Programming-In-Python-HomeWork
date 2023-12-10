# HW9.py
# Author: Jayant Vinaik
from tabulate import tabulate
# This homework will expand upon the code for Lab11.py. If you did not complete Lab11.py, you should do so before attempting this homework.

# Copy the code from Lab11.py into this file 1-11. I'll add some comments to help you out.


# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)
class Product:
    """Class representing a product."""
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

  # 2. Create a method called __str__ that returns a string with the following format:
  # Product: <name>, Price: <price>, ID: <product_id>
  # Hint: use f-strings to format the string.
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"


# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.
class Customer:
  """Class representing a customer."""
  def __init__(self, name, customer_id):
      self.name = name
      self.customer_id = customer_id
      self.cart = []

  # also create a __str__ method that returns a string with the following format:
  # Customer: <name>, ID: <customer_id>
  # Hint: use f-strings to format the string.
  def __str__(self):
      return f"Customer: {self.name}, ID: {self.customer_id}"

  # 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was      added and the customer's name.
  def add_to_cart(self, product):
      self.cart.append(product)
      print(f"Product '{product.name}' added to the cart for customer '{self.name}'.")

  # 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.
  def remove_from_cart(self, product):
      if product in self.cart:
          self.cart.remove(product)
          print(f"Product '{product.name}' removed from the cart for customer '{self.name}'.")
      else:
          print(f"Product '{product.name}' not found in the cart for customer '{self.name}'.")

  # 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After        # printing out the total, empty the cart.
  # Hint: you will need to loop through the cart and add up the prices.
  def checkout(self):
      total_price = sum(product.price for product in self.cart)
      print(f"Total Price for customer '{self.name}': ${total_price:.2f}")
      self.cart = []

  # 7. Create a method called display_products that prints out all the products in the cart list. (use the __str__ method from the   Product class)
  # 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
  # Make a nice table table using the tabulate library.
  def display_products(self):
      print(tabulate([str(product).split(', ') for product in self.cart], headers=["Product", "Price", "ID"]))



# 7. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.
class Store:
  """Class representing a store."""
  def __init__(self):
      self.products = []
      self.customers = []

  # 8. Create a method called add_product that takes in a Product object and adds it to the products list.
  def add_product(self, product):
      self.products.append(product)
      print(f"Product '{product.name}' added to the store.")

  # 9. Create a method called add_customer that takes in a Customer object and adds it to the customers list.
  def add_customer(self, customer):
      self.customers.append(customer)
      print(f"Customer '{customer.name}' added to the store.")

  # 10. Create a method called display_products that prints out all the products in the products list.
  def display_products(self):
      print("Products in the store:")
      for product in self.products:
          print(product)

  # 11. Create a method called display_customers that prints out all the customers in the customers list.
  def display_customers(self):
      print("Customers in the store:")
      for customer in self.customers:
          print(customer)



# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 12. Create a store object called store.
store = Store()

# 13. Create a product object called product1 with the following attributes:
# name: "iPhone 12"
# price: 799.99
# product_id: 1
product1 = Product("iPhone 12", 799.99, 1)

# 14. Create a product object called product2 with the following attributes:
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2
product2 = Product("iPhone 12 Pro", 999.99, 2)

# 15. Create a product object called product3 with the following attributes:
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3
product3 = Product("iPhone 12 Pro Max", 1099.99, 3)

# 16. Create a customer object called customer1 with the following attributes:
# name: "John"
# customer_id: 1
customer1 = Customer("John", 1)

# 17. Create a customer object called customer2 with the following attributes:
# name: "Jane"
# customer_id: 2
customer2 = Customer("Jane", 2)


# 18. Add product1 to the store using the add_product method.
store.add_product(product1)

# 19. Add product2 to the store using the add_product method.
store.add_product(product2)

# 20. Add product3 to the store using the add_product method.
store.add_product(product3)

# 21. Add customer1 to the store using the add_customer method.
store.add_customer(customer1)

# 22. Add customer2 to the store using the add_customer method.
store.add_customer(customer2)

# 23. Add product1 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product1)

# 24. Add product2 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product2)

# 25. Add product3 to customer2's cart using the add_to_cart method.
customer2.add_to_cart(product3)

# 26. Display current products in customer1's cart using the display_products method.
print("\nProducts in Customer1's Cart:")
customer1.display_products()

# 27. Display current products in customer2's cart using the display_products method.
print("\nProducts in Customer2's Cart:")
customer2.display_products()

# 28. Checkout customer1's cart using the checkout method.
customer1.checkout()

# 29. Checkout customer2's cart using the checkout method.
customer2.checkout()

# 30. Display current products in customer1's cart using the display_products method. (should be empty)
print("\nProducts in Customer1's Cart (after checkout):")
customer1.display_products()


# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def add_product_to_customer_cart(customer, product):
  customer.add_to_cart(product)
  print(f"Product '{product.name}' added to the cart for customer '{customer.name}'.")

# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer, product):
  customer.remove_from_cart(product)
  print(f"Product '{product.name}' removed from the cart for customer '{customer.name}'.")


def menu():
  print("Menu:")
  print("1. Add Product")
  print("2. Add Customer")
  print("3. Add Product to Customer's Cart")
  print("4. Remove Product from Customer's Cart")
  print("5. Display Products")
  print("6. Display Customers")
  print("7. Display Customer's Cart")
  print("8. Checkout")
  print("9. Exit")
  choice = int(input("Enter your choice (1-9): "))
  return choice


def main():
  store = Store()

  while True:
      choice = menu()

      if choice == 1:
          name = input("Enter product name: ")
          price = float(input("Enter product price: "))
          product_id = int(input("Enter product ID: "))
          product = Product(name, price, product_id)
          store.add_product(product)
      elif choice == 2:
          name = input("Enter customer name: ")
          customer_id = int(input("Enter customer ID: "))
          customer = Customer(name, customer_id)
          store.add_customer(customer)
      elif choice == 3:
          customer_id = int(input("Enter customer ID: "))
          product_id = int(input("Enter product ID: "))
          customer = next((c for c in store.customers if c.customer_id == customer_id), None)
          product = next((p for p in store.products if p.product_id == product_id), None)
          if customer and product:
              add_product_to_customer_cart(customer, product)
          else:
              print("Customer or product not found.")
      elif choice == 4:
          customer_id = int(input("Enter customer ID: "))
          product_id = int(input("Enter product ID: "))
          customer = next((c for c in store.customers if c.customer_id == customer_id), None)
          product = next((p for p in store.products if p.product_id == product_id), None)
          if customer and product:
              remove_product_from_customer_cart(customer, product)
          else:
              print("Customer or product not found.")
      elif choice == 5:
          store.display_products()
      elif choice == 6:
          store.display_customers()
      elif choice == 7:
          customer_id = int(input("Enter customer ID: "))
          customer = next((c for c in store.customers if c.customer_id == customer_id), None)
          if customer:
              customer.display_products()
          else:
              print("Customer not found.")
      elif choice == 8:
          customer_id = int(input("Enter customer ID: "))
          customer = next((c for c in store.customers if c.customer_id == customer_id), None)
          if customer:
              customer.checkout()
          else:
              print("Customer not found.")
      elif choice == 9:
          print("Exiting the program. Goodbye!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()