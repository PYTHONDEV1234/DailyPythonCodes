import os
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {'phone': phone, 'email': email}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

def add_contact(contacts):
    name = input("Enter contact's name: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("Contact added successfully.")

def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact removed successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--->> > > > > > Contacts < < < < <<----- \n")
        for name, info in contacts.items():
            print(f"Name: {name} ---- Phone: {info['phone']} --- Email: {info['email']}")
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. List All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            list_contacts(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
