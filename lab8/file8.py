import json

contacts_file = "contacts.json"

try:
    with open(contacts_file, "r") as f:
        contacts = json.load(f)
except:
    contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name + ": " + contacts[name])
    else:
        print("Contact not found.")

def update_number():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        number = input("Enter new number: ")
        contacts[name] = number
        print("Number updated successfully!")
    else:
        print("Contact not found.")

def update_name():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        new_name = input("Enter new name: ")
        number = contacts.pop(name)
        contacts[new_name] = number
        print("Name updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def save_contacts():
    with open(contacts_file, "w") as f:
        json.dump(contacts, f)

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Number")
    print("4. Update Name")
    print("5. Delete Contact")
    print("6. Save and Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_number()
    elif choice == "4":
        update_name()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        save_contacts()
        break
    else:
        print("Invalid choice.")
