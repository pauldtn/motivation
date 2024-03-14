# motivation
This Python script is a thoughtful tool designed to input, calculate, and display personalized messages for a group of children based on their ages. Utilizing the birth year of each child, the program calculates their current age and presents an encouraging message tailored to their age group. Additionally, the script organizes and displays the list of children from the oldest to the youngest, providing a clear overview of their ages.

Features
Age Calculation: Automatically calculates the age of each child using their birth year and the current year.
Personalized Messages: Displays a unique message to each child depending on their age group.
Sorting: Sorts children by age from oldest to youngest for a clear overview.
Dynamic Input: Allows the input of multiple children's names and birth years (program currently set for six children).
Usage
Starting the Program:

Run the script in your Python environment.
Entering Child Information:

When prompted, input the name and year of birth for each child. The program is currently configured to accept information for six children but can be easily modified for more or fewer entries.
Viewing Messages and List:

After entering each child's information, a personalized message will be displayed based on the child's age.
Once all entries are completed, the program will output a sorted list of children's names alongside their ages, from the oldest to the youngest.
Requirements
Python 3.x
No external libraries are required, as the program only uses the datetime module from Python's standard library.
Implementation Details
The program uses the datetime module to obtain the current year, ensuring age calculations are always up to date.
It leverages a list to store tuples containing each child's name and calculated age.
The sorted function is used with a lambda function as the key to sort the children by age.
Conclusion
The Children's Age Message Program is a delightful way to engage with children of various ages, providing motivational messages tailored to their stage in life. It serves as an excellent example of how Python's date and time functionalities can be applied in a practical, user-friendly application. Whether for educational purposes, family activities, or developmental programs, this script offers a blend of technology and human touch.
