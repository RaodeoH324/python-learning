a = float(input("Enter a number: "))
b = float(input("Enter second number: "))

operator = input("Enter the operator (+, -, *, /): ")

match operator:
    case "+":
        res = a + b
        print(res)
    case "-":
        res = a-b
        print(res)
    case "*":
        res = a*b
        print(res)
    case "/":
        if b!=0:
            res = a/b
            print(res)
        else:
            print("Your cannot divide a number by 0")
    case _:
        print("Invalid operator")
