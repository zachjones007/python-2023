username = input("Please enter your name: ")
user_age = int(input("Hello, " + username + "! How old are you? "))
dinner = input("Do you like pizza or pasta? ")

if user_age >= 18:
    if dinner == "pasta":
        print("Awesome, " + username + "! We're going to Olive Garden and ordering " + dinner + " tonight!")
    elif dinner == "pizza":
        print("I know a fancy " + dinner + " place with a special that includes drinks and a side!")
    else:
        print("I've never made " + dinner + " before but we can go get groceries and make it!")
else:
    print("Sorry, " + username + ", we have to ask my parents before we can get " + dinner + " tonight.")

print("Thanks for dinner, " + username + "!")
