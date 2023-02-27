print("Welcome to Hall Of Fitness")
print("Lead By Example")

workouts = []
prices = []
total = 0

while True:
    workouts = input("Enter a workout to buy (q to quit):")
    if workouts == "q":
        break
    else:
        price =float(input(f"Enter the price of a {workouts}: $"))
        prices.append(price)


print(" ---** Your Cart **---")

for workouts in workouts:
    print(workouts)

for price in prices:
    total = total + price

print(f"Your workout total is: ${total}")