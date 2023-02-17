import random

# Generate some grades and write them to a file
with open("grades.txt", "w") as file:
    for i in range(10):
        grade = random.randint(50, 100)
        file.write(str(grade) + "\n")

# Read the grades from the file and calculate the class average
with open("grades.txt", "r") as file:
    grades = [int(grade) for grade in file.readlines()]

class_average = sum(grades) / len(grades)
print("Class average: {:.2f}".format(class_average))