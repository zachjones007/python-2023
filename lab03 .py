 
def collatz(userinput):
    if userinput % 2 == 0:
        result = userinput // 2 
    else: 
        result = 3 * userinput + 1 
    print(result) 
    return result 

print("Welcome to the Collatz Sequence calculator.")


Numbers = int(input("Please enter a positive number: "))


while Numbers != 1:
    Numbers = collatz(Numbers) # Calculate the next number in the sequence
print("The Collatz sequence has reached 1.")
