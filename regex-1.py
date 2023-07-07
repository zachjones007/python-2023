
import re

def is_strong_password(password,name,birthdate):


    if len(password) < 10:
        print ('password that uses ')
        return False

    if not re.search('[a-z]', password) or not re.search('[A-Z]', password):
        print ('password that uses lower and upper case ')
        return False


    if not re.search('[0-9]', password):
        print ('password that uses [0-9]')
        return False


    if re.search(name, password,re.IGNORECASE): #everything is the same case in name (third arugment modifies behavieor)
        print('password without your name')
        return False

    if  re.search(birthdate, password):
        print ('password that doent use your birth year')
        return False

    print('password works')
    return True

name = input(str('whats your name?'))
birthdate = input(int('what is your birth year'))
password = input(str('input a password'))

