'''
4. Mastering Tuple Packing and Unpacking in Python
Task 1: Customer Order Processing
Refine your skills in tuple unpacking by managing customer orders.

Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, 
and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.
Write a function to iterate over the list of orders.
Unpack each tuple in the list and format the details for display.
'''

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Sam", "Mouse", 10),
    ("Kelly", "Monitor", 6),
    ("Bill", "Desk Top", 20),
    ("Angie", "Tablet", 15),
    ("Steve", "Remote", 8)
]

def print_orders(orders):
    for index, order in enumerate(orders, start=1):
        name, product, quantity = order
        print(f"Order {index}:")
        print(f"Customer Name: {name}")
        print(f"Product Ordered: {product}")
        print(f"Quantity: {quantity}")
        print()
print_orders(orders)

'''
Task 2: Sorting and Filtering Contact Information
Implement tuple packing and unpacking in sorting and filtering tasks.

Problem Statement:
You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. Your task is to:

Sort the contacts by name.
Filter and display contacts whose names start with a specific letter.
'''

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Ned", "fred@email.com", "205-907-5509"),
    ("Ben", "cgtr@email.com", "267-654-0976"),
    ("Gideon", "dsjk@email.com", "567-865-0432"),
    ("Skip", "sdkh@email.com", "890-654-2345"),
]

def sort_contacts_by_name(contacts):
    sorted_contacts = sorted(contacts)
    return sorted_contacts

def filter_contacts_by_letter(contacts, letter):
    filtered_contacts = [contact for contact in contacts if contact[0].startswith(letter)]
    return filtered_contacts

sorted_contacts = sort_contacts_by_name(contacts)
print("Contacts sorted by name:")
for contact in sorted_contacts:
    print(contact)

letter = 'B'
filtered_contacts = filter_contacts_by_letter(contacts, letter)
print(f"\nContacts whose names start with '{letter}':")
for contact in filtered_contacts:
    print(contact)
