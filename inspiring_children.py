from datetime import datetime

# Function to calculate age
def calculate_age(birth_year, current_year):
    return current_year - birth_year

# List to store children's information
children = []

# Input for each child's name and year of birth
for _ in range(6):  # Assuming there are six children
    name = input("Enter the child's name: ").capitalize()
    birth_year = int(input("Enter the year of birth: "))
    age = calculate_age(birth_year, datetime.now().year)
    
    # Print corresponding message based on age
    if age < 12:
        print(f"{name}, Dream big, young one.")
    elif 12 <= age < 18:
        print(f"{name}, It takes courage to grow up and become who you really \
are.")
    else:
        print(f"{name}, No matter what anybody tells you, words and ideas can \
change the world.")

    # Append child's information to the list
    children.append((name, age))

# Sort children based on age from older to younger
sorted_children = sorted(children, key=lambda x: x[1])

# Print sorted list of children and their ages
print("\nChildren and their ages (from older to younger):")
for child, age in sorted_children:
    print(f"{child}: {age} years old")
