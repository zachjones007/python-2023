def collatz(userinput,zero,one,two,three):
    Collatzsequence = [userinput]
    while userinput != one:
        if userinput % two == zero:
            userinput = userinput // two
        else:
            userinput = three * userinput + one
        Collatzsequence.append(userinput)
    print (Collatzsequence)

userinput = int(input("Enter a positive integer: "))
collatz(userinput,0,1,2,3)