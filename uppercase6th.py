#Determine and return the number of 
# characters in the given string,
#  not including spaces.

#Determine and return what 
# character is in the 6th position
#  of the given string

#Return the given string in all uppercase.

#Determine and return the last word in 
# the given string, repeated a random number of times.


#reate and return a dictionary 
# that contains key pair values where each 
# word in the given string is the key and the 
# count of how often that word appears is the value.
    

def checkletter(create):
    letter_count = {}
    for letter in create:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def word_count(create):
    words = create.split()
    inventory = {}
    for word in words:
        inventory.setdefault(word, 0)
        inventory[word] += 1
    print('Inventory updated!')
    return inventory
def Sixth(create):
    sixth_character = create[5]
    return sixth_character

 

create = input('Input a sentence: ')



sixth_word = Sixth(create)
print("Sixth word:", sixth_word)
print("Uppercase string:", create.upper())
letter_counts = checkletter(create)
print("Letter count dictionary:", letter_counts)
word_counts = word_count(create)
print("Word count dictionary:", word_counts)
print(Sixth)  # Output: ",

