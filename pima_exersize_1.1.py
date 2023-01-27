def numbers (p,r,a,b,c,o):


    for n in [a,b,c]:
        a = p * (o + r)**n
        print(f"year : {n} return : ${a}")
numbers (1000,0.07,10,20,30,1)
