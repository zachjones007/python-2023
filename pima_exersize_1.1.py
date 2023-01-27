p=1000
r=0.07
a=10
b=20
c=30

for n in [a,b,c]:
    a = p * (1 + r)**n
    print(f"year : {n} return : ${a}")
