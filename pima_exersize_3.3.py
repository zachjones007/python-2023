keypad = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PRS',
    '8': 'TUV',
    '9': 'WXY',
}

def generate_words(phone_number):
    words = []
    #generate all possible nunbers
    for digit1 in keypad[phone_number[0]]:
        for digit2 in keypad[phone_number[1]]:
            for digit3 in keypad[phone_number[2]]:
                for digit4 in keypad[phone_number[3]]:
                    for digit5 in keypad[phone_number[4]]:
                        for digit6 in keypad[phone_number[5]]:
                            for digit7 in keypad[phone_number[6]]:
                                word = digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7
                                words.append(word)
    return words

while True:
    phone_number = input("Enter a sevendigit phone number: ")
    words = generate_words(phone_number)
#write to phonewords.txt
    with open("phonewords.txt", "w") as file:
        file.write(f"There are {len(words)} ] combinations for the number")
        # get everything on a seprate line 
        file.write("\n".join(words) + "\n\n")

    print(f"There are {len(words)} combinations for {phone_number}")

    while True:
        option = input('Would you like to continue? (yes or quit) ')
        if option in ["n", "q","N",'Q']:
            break
        elif option in ["y", "Y","c",'C']:
            with open("phonewords.txt", "r") as file:
                print(file.read())
        else:
            print(" Please enter 'yes' or 'quit'.")

    if option in  ["n", "q","N",'Q']:
        break
