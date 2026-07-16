foods = []
prices = []
total = 0

while True:
    a = input("Enter food to buy (press q to quit):  ")
    if a.lower() == "q":
        break
    else:
        cost = int(input(f"Enter the price of {a} (press q to quit):  "))

        foods.append(a)
        prices.append(cost)

print("-----YOUR CART-----")
for i in foods:
    print(i, end = " ")
print()

for j in prices:
    total+=j

print(f"Your total is: {total}")