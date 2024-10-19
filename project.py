# Create a List of Dictionaries:
# List of contacts
contacts = [
    {"name": "Alice", "phone": "123-456-7890", "email": "alice@example.com"},
    {"name": "Bob", "phone": "234-567-8901", "email": "bob@example.com"},
    {"name": "Charlie", "phone": "345-678-9012", "email": "charlie@example.com"}
]
# Print details of each contact
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
# Update Bob's phone number
for contact in contacts:
    if contact["name"] == "Bob":
        contact["phone"] = "999-999-9999"
# Add a new contact
new_contact = {"name": "Diana", "phone": "456-789-0123", "email": "diana@example.com"}
contacts.append(new_contact)

# Remove a contact by name
contacts = [contact for contact in contacts if contact["name"] != "Charlie"]
