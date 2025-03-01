#Martha Moreno Gonzalez
#02/28/2025
#Problem 2: will check if number in with the range 

def checkNumberInRange(num):
    if num in range (1, 10):
        print("It is within the range!")
    else:
        print("It is not within the range.")

number = int(input("Enter the number you want to check: "))
checkNumberInRange(number)
