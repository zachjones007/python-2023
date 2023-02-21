with open("grades.txt", "a") as file:
    while True:
        grade = input("Enter a grade or type quit: ")
        if grade in ['q', 'Q', 'd','D']:
            break
        try:
            grade = float(grade)
            if grade <= 100.00:
                file.write("{:.2f}\n".format(grade))
            else:
                print("must be lessthen or equal too 100.00")
        except ValueError:
            print("ValueError")
    
with open("grades.txt", "r") as file:
    grades = [float(line.strip()) for line in file]
    class_average = sum(grades) / len(grades)
    print("Class average: {:.2f}".format(class_average))