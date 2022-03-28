from pip import main


def calculator(num1,num2):
    
    choice = input("Enter your choice : ") #making choice in a string value
    print("1. Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    no1 = float(input("Enter Number 1 : ")) #Allows used to used decimal number
    no2 = float(input("Enter Number 2 : "))
    sum = num1 + num2
    sub = num1 - num2
    mux = num1 * num2
    div = num1 / num2

    if choice == "1":
        print(num1, "+", num2, "=", sum)
    elif choice == "2":
        print(num1, "-", num2, "=", sub)
    elif choice == "3":
        print(num1, "-", num2, "=", mux)
    elif choice == "4":
        if num2 == 0.0:
            print("Divide by 0 error")
        else: 
            print(num1, "-", num2, "=", div)
    else :
        print("Wrong number")
    return num1, num2

calculator(input(no1),input(no2))