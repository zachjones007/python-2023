def numbers (p,r,a,b,c):


    for n in [a,b,c]:
        a = p * (1 + r)**n
        print(f"year : {n} return : ${a}")
numbers (1000,0.07,10,20,30)
