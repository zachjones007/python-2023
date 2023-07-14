import pyinputplus as pyip
def wantdinner():
    want_food = pyip.inputYesNo('Do you want food?')
    print('Want cheese:', want_food)
    if want_food:
        foodlist = []
        # Using inputMenu() for bread type
        bread_type = pyip.inputMenu('Select a bread type:', ['wheat', 'white', 'sourdough'])
        print('Selected bread type:', bread_type)
        foodlist.append(bread_type)
        # Using inputYesNo() for meat
        want_meat = pyip.inputYesNo('Do you want meat?')
        print('Want cheese:', want_meat)

        if want_meat:
                # Using inputMenu() for meat type
            meat_type = pyip.inputMenu('Select a meat type:', ['beef', 'chicken', 'fish'])
            print('Selected cheese type:', meat_type)
            foodlist.append(meat_type)
        # Using inputYesNo() for cheese 
        want_cheese = pyip.inputYesNo('Do you want cheese?')
        print('Want cheese:', want_cheese)

        # Using inputMenu() for cheese type (if want_cheese is True)
        if want_cheese:
            cheese_type = pyip.inputMenu('Select a cheese type:', ['cheddar', 'Swiss', 'mozzarella'])
            print('Selected cheese type:', cheese_type)
            foodlist.append(cheese_type )


        # Using inputInt() for number of sandwiches
        num_sandwiches = pyip.inputInt('How many sandwiches do you want?', min=1)
        print('Number of sandwiches:', num_sandwiches)
    else: 
        print("have a nice day")
