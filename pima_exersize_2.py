name = input(str("Please enter your name: "))
age = int(input("Hello,  hello {name} have you heard about russian rullet?? NO?! well ill tell you! How old are you? "))
dinner = input(" Pizza or Pasta? ")

if age >= 18:
    if dinner == "Pasta":
        print("  {name}, we are going to dinner to get {dinner} tonight")
    elif dinner == "Pizza":
        print("I know a fancy {dinner} place with a special that includes drinks and a side!")
    else:
        print("I've never made {dinner} before, lets go to the store ")
else:
    print("Sorry,  {name} , we need to ask before we can get {dinner} tonight.")

print("Thanks for dinner,  {name} !")
