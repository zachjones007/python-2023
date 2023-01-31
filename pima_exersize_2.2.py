def numbers (twotwenty,pointfive,pointeight):
    age = int(input("Please enter your age: "))
    max = twotwenty - age
    low = max * pointfive
    high = max * pointeight

    print(f"low : {low:.1f} high : {high:.1f}")
numbers(220,0.5,0.85)
