guests= {}

guests['Alice'] = 28, 'alice@email.com'
guests['Bob'] = 35, 'bob@email.com'
guests['Charlie']= 30, 'charlie@email.com'

print(guests)

guests['David'] = 22, 'david@email.com'
del guests['Bob']

print (guests)

def get_guest_info(guest_name):
  if guest_name in guests:
     age, email = guests[guest_name]
     return f"{guest_name} (Age: {age}) is coming to the party! Email: {email}"
  else:
    return f"{guest_name} is not on the guest list."
def display_guest_count():
    return f"Total number of guests: {len(guests)}"

for name, info in guests.items():
    age, email = info
    print(f"- {name} (Age: {age}, Email: {email})")

# Retrieve specific guest information
print("Retrieving Guest Info:")
print(get_guest_info("Alice"))
print(get_guest_info("Bob"))

# Display total guest count
print("Guest Counter:")
print(display_guest_count())

def add_or_update_guest():
    name = input("Enter your guest name: ").strip()
    if name in guests:
        print(f"{name} is already on the guest list.")
        choice = input("Would you like to update their details? (yes/no): ").strip().lower()
        if choice == "yes":
            age = int(input(f"Enter {name}'s age: "))
            email = input(f"Enter {name}'s email: ").strip()
            guests[name] = (age, email)
            print(f"{name}'s details have been updated.")
        else:
            print(f"Skipped updating {name}.")
    else:
        age = int(input(f"Enter {name}'s age: "))
        email = input(f"Enter {name}'s email: ").strip()
        guests[name] = (age, email)
        print(f"{name} has been added to the guest list.")

sorted_guests = sorted(guests.items(), key=lambda x: x[1][0])  # Sort by age
print("\nGuests sorted by age:")
for name, (age, email) in sorted_guests:
    print(f"{name} (Age: {age}) - Email: {email}")