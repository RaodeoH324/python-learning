temp = int(input("enter temprature"))
var = input("celsius or far ")

if var == celsius:
    f = (temp * 9/5) + 32
    print("The temprature in Fahrenheit is: ", f)
else:
    c = (temp - 32) * 5/9
    print("The temprature in celsius is: ", c)
