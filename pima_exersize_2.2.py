age = int(input("Please enter your age: "))
max_heart_rate = 220 - age
target_heart_rate_low = max_heart_rate * 0.5
target_heart_rate_high = max_heart_rate * 0.85

print("Your maximum heart rate is: {:.2f} beats per minute".format(max_heart_rate))
print("Your target heart rate range is between: {:.2f} and {:.2f} beats per minute".format(target_heart_rate_low, target_heart_rate_high))
