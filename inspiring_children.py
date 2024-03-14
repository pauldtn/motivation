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

# Sample book recommendations by age group
book_recommendations = {
    'child': ("'Oh, The Places You’ll Go!' by Dr. Seuss - A book full of hope and encouragement.",),
    'teen': ("'The Alchemist' by Paulo Coelho - A tale about following your dreams.",),
    'young_adult': ("'Atomic Habits' by James Clear - Insightful advice on building good habits.",),
    'adult': (
        "'Educated' by Tara Westover - A memoir about the transformative power of education.",
        "'Becoming' by Michelle Obama - A deeply personal account from a former First Lady."
    )
}

# Input for each child's name and year of birth
for _ in range(6):  # Assuming there are six children
    name = input("Enter the child's name: ").capitalize()
    birth_year = int(input("Enter the year of birth: "))
    age = calculate_age(birth_year, datetime.now().year)
    
    # Print corresponding message based on age
    if age < 12:
        print(f"{name}, Dream big, young one.")
        print(book_recommendations['child'][0])
    elif 12 <= age < 18:
        print(f"{name}, It takes courage to grow up and become who you really are.")
        print(book_recommendations['teen'][0])
    elif 18 <= age <= 21:
        print(f"{name}, No matter what anybody tells you, words and ideas can change the world.")
        print(book_recommendations['young_adult'][0])
    else:
        random_message = random.choice(messages_over_21)
        random_book = random.choice(book_recommendations['adult'])
        print(f"{name}, {random_message}")
        print(random_book)

    # Append child's information to the list, including those over 21 with the new logic
    children.append((name, age))

# Sort children based on age from older to younger
sorted_children = sorted(children, key=lambda x: x[1], reverse=True)

# Print sorted list of children and their ages
print("\nChildren and their ages (from older to younger):")
for child, age in sorted_children:
    print(f"{child}: {age} years old")
