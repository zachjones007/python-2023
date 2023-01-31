total_miles = 0
total_gallons = 0

def numbers (trip,gallons,empty):
    while True:
        trip = float(input("Enter miles driven (0 to quit): "))
        if trip == empty:
            break

        gallons = float(input("Enter gallons used: "))

        mpg = trip / gallons
        print("Miles per gallon for this tankful:", mpg)

        global total_miles
        global total_gallons
        total_miles += trip 
        total_gallons += gallons

        continue_input = input("Would you like to enter another tankful? (y/n)")
        if continue_input.lower() == "n":
            break

    if total_gallons > empty:
        total_mpg = total_miles / total_gallons
        print("Total miles per gallon for all tankfuls: {:.2f}".format(total_mpg))
    else:
        print("No information was entered.")

numbers(0,0,0)
