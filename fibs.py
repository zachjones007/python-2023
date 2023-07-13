def go (a):
    if a <= 1:
        return a
    else:
        return go(a-1) + go(a-2)
a = 10 
fibs = go(a)
print(fibs)
