def numbers (p,r,a,b,c,o):


    for n in [a,b,c]:
        a = p * (o + r)**n
        print(f"year : {n} return : ${a}")
numbers (1000,0.07,10,20,30,1)

def double_amount(amount):
    double = amount * 2
    print('Twice that amount is ' + str(double))

num = int(input('Enter a number:\n'))
double_amount(num)
