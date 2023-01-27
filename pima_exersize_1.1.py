p = 1000
r = 0.07

for n in [10,20,30]:
    a = p * (1 + r)**n
    print(f"year : {n} return : ${a}")
