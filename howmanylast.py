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
import random    

def checkletter(userinput):
    letter_count = {} 
    for letter in userinput: 
        if letter in letter_count:
            letter_count[letter] += 1 #add 1 to lettercount
        else:
            letter_count[letter] = 1 #set lettercount = 1
    return letter_count
def word_count(userinput):
    words = userinput.split()
    inventory = {}
    for word in words:
        inventory.setdefault(word, 0) #check if word is a key in inventory if its not in the dictoinary add it with the value of 0
        inventory[word] += 1
    print('Inventory updated!')
    return inventory
def Sixth(userinput):
    sixth_character = userinput[5] # userinput = input creates a string value and it prints the 6th string vlaue
    return sixth_character

def repeat(userinput):
    lastcharacter = userinput[-1]
    ranlist = lastcharacter * (random.randint(1,10)) 
    howmanylast = len(ranlist)
    return howmanylast
    
 

userinput = input('Input a sentence: ')



sixth_word = Sixth(userinput)
print("Sixth word:", sixth_word)
print("Uppercase string:", userinput.upper())
letter_counts = checkletter(userinput)
print("Letter count dictionary:", letter_counts)
print(Sixth)  # Output: ",
print("last letter random amount of times",repeat(userinput))


