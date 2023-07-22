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

# This is a recursive function named 'go' that computes Fibonacci numbers.
def go(a):
    # Base case: If 'a' is 0 or 1, the function returns 'a'.
    if a <= 1:
        return a
    else:
        # Recursive call: This function calls itself twice.
        # One call is for the previous Fibonacci number (a-1) and the other call is for the Fibonacci number before that (a-2).
        # The function then returns the sum of those two Fibonacci numbers to produce the 'a'th Fibonacci number.
        return go(a-1) + go(a-2)
a = 10
fibs = go(a)
print(fibs)
#go(10)
#= go(9) + go(8)
#= (go(8) + go(7)) + (go(7) + go(6))
#= ((go(7) + go(6)) + (go(6) + go(5))) + ((go(6) + go(5)) + (go(5) + go(4)))+ (this continues expanding until reaching base cases)


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
