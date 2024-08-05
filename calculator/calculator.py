def plus(num1 , num2) :
    return num1 + num2


def minus(num1 , num2) :
    return num1 - num2


def multiplied(num1 , num2) :
    return num1 * num2


def divide(num1 , num2) :
    return num1 / num2


first_number = int(input("please enter the first number : "))

second_number = int(input("please enter the second number : "))

print("Please select operation -\n" 
        "1. plus\n" 
        "2. minus\n" 
        "3. multiplied\n" 
        "4. divide\n")

select = int(input("Select operations form 1, 2, 3, 4 : "))



if select == 1:
    print(first_number, "+", second_number, "=",
                    plus(first_number, second_number))
 
elif select == 2:
    print(first_number, "-", second_number, "=",
                    minus(first_number, second_number))
 
elif select == 3:
    print(first_number, "*", second_number, "=",
                    multiplied(first_number, second_number))
 
elif select == 4:
    print(first_number, "/", second_number, "=",
                    divide(first_number, second_number))
else:
    print("Invalid input")