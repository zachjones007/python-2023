#Lab: Telephone Number Word Generator
keypad = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PRS',
    '8': 'TUV',
    '9': 'WXY'
}

def generate_words(phone_number):
    words = []
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

phone_number = input("Enter a seven-digit phone number: ")
words = generate_words(phone_number)

print(f"There are {len(words)} possible word combinations for the phone number {phone_number}:")
print(words)