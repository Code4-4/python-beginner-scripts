# simple_contact_book.py
contact_book = {}

def add_contact(name, phone):
    contact_book[name] = phone
    print(f"Contact {name} added.")

def display_contacts():
    print("Contact Book:")
    for name, phone in contact_book.items():
        print(f"{name}: {phone}")

if __name__ == "__main__":
    add_contact("Alice", "123-456-7890")
    add_contact("Bob", "987-654-3210")
    display_contacts()
