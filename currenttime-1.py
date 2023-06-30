
#Get the current date and time and store it in variable x.
#Repeat Part (a) and store the result in variable y.
#Display each datetime object.
#Display each datetime object’s data attributes individually.
#Use the comparison operators to compare the two datetime objects.
#Calculate the difference between y and x.

from datetime import datetime
x = datetime.now()
y = datetime.now()
print(x.year, x.month, x.day, x.hour, x.minute, x.second)
print(y.year, y.month, y.day, y.hour, y.minute, y.second)

print(x,y)
if x > y:
    print(x)
if y > x: 
    print (y)
else:
     print("equal")

z = x - y 
print(z)