def stats(total_miles, total_gallons):
    def numbers (trip, gallons):
        while True:
            try:
                trip = float(input("Enter miles for trip: "))
                total_miles.append(trip)
            except ValueError:
                #prints false if float is not entered 
                print("please enter a number.")
                continue

            try:
                gallons = float(input("Enter gallons consumed: "))
                total_gallons.append(gallons)
            except ValueError:
                print("please enter a number.")
                continue

            mpg = trip / gallons
            print("Miles per gallon for this tankful:", mpg)
            
            option = str(input('Would you like to continue? yes or quit '))
            if option.lower() in ["n", "q"]:
                break

        total_mpg = sum(total_miles) / sum(total_gallons)
        print("Total Miles Per Gallon:", total_mpg)

    numbers([], [])

stats([0], [0])