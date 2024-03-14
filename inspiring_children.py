from datetime import datetime
import random

# Function to calculate age
def calculate_age(birth_year, current_year):
    return current_year - birth_year

# List to store children's information
children = []

# Messages for individuals over 21
messages_over_21 = [
    "You are never too old to learn.",
    "You are only as old as your heart feels."
]

# Input for each child's name and year of birth
for _ in range(6):  # Assuming there are six children
    name = input("Enter the child's name: ").capitalize()
    birth_year = int(input("Enter the year of birth: "))
    age = calculate_age(birth_year, datetime.now().year)
    
    # Print corresponding message based on age
    if age < 12:
        print(f"{name}, Dream big, young one.")
    elif 12 <= age < 18:
        print(f"{name}, It takes courage to grow up and become who you really are.")
    elif 18 <= age <= 21:
        print(f"{name}, No matter what anybody tells you, words and ideas can change the world.")
    else:
        # Select a random message for individuals over 21
        random_message = random.choice(messages_over_21)
        print(f"{name}, {random_message}")

    # Append child's information to the list, including those over 21 with the new logic
    children.append((name, age))

# Sort children based on age from older to younger
sorted_children = sorted(children, key=lambda x: x[1], reverse=True)

# Print sorted list of children and their ages
print("\nChildren and their ages (from older to younger):")
for child, age in sorted_children:
    print(f"{child}: {age} years old")
