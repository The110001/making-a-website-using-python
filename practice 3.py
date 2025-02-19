# practice 3
# print the sum of the current number and the previous number

print("""Hello there. in order to make our program work, you need to provide two numbers to our program. 
so then we can create a range and do something interesting.""")

while True:
    print("")
    number1 = input("1/ please provide the first number here: ")
    number2 = input("2/ please provide the second number here: ")

    if number1.isdigit() and number2.isdigit():
        pass
        if int(number1) < int(number2):
            pass
            for i in range (int(number1) , int(number2) + 1):
                if i == int(number1):
                    print("")
                    print(f"the current number is {i}")
                else:
                    print(f"current number is {i} and previous number is {i - 1} and their sum is {i + (i - 1)}")
            break
        else:
            print("")
            print("** number 1 is greater than number 2. that is not acceptable by the program.\nplease try again")
    else:
        print("")
        print("** your inputs do not match our guide-lines.\nplease try again.")