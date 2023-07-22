# Data Structures and Representation
names = ["Alice", "Bob", "Charlie"]  # List
person = ("Alice", 25)  # Tuple
age_mapping = {"Alice": 25, "Bob": 30, "Charlie": 28}  # Dictionary

# Complex Problem Solving
def average_age(ages):
    return sum(ages) / len(ages)

# Procedural Abstraction
def display_person(p):
    print(f"Name: {p[0]}, Age: {p[1]}")

# Complex Arrays with Structured Elements
matrix = [
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9]  #2
]
print(matrix[2][1])  # prints 8

# Object Oriented Programming
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Employee Name: {self.name}, Age: {self.age}")

alice = Employee("Alice", 25)
alice.display()

# Exception Handling
try:
    print(age_mapping["David"])
except KeyError:
    print("David is not in the mapping.")

# File Input and Output
with open('names.txt', 'w') as f:
    for name in names:
        f.write(name + "\n")

with open('names.txt', 'r') as f:
    read_names = [line.strip() for line in f.readlines()]
print(read_names)

# Debugging and Testing
assert average_age([25, 30, 28]) == 27.666666666666668, "Average age calculation is incorrect"
