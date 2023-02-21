import random

while True:
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

    age = input("How old are you? ")
    print(f"{age}, got it.")

    while True:
        food_preference = input("Do you like pizza or pasta? ")
        if food_preference.lower() == "pizza":
            print(f"Sorry, {name}, we have to ask my parents before we can get pizza tonight.")
            break
        elif food_preference.lower() == "pasta":
            print(f"Awesome, {name}! We're going to Olive Garden and ordering pasta tonight!")
            break
        else:
            print("I'm sorry, I didn't understand that food preference.")

    num_yums = random.randint(1, 5)
    print("Yum\n" * num_yums)

    while True:
        go_to_dinner = input("Does someone else want to go to dinner? ")
        if go_to_dinner.lower() in ["no", "n","N"]:
            print(f"Thanks for dinner, {name}!")
            break
        else:
            print(f"Please enter your name:")
            break
