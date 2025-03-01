#Martha Moreno Gonzalez
#02/28/2025
#Problem 3: multiply all the numbers in a list 

def multiplyList(numbers):
    result = 1
    for num in numbers: 
        result *= num
    return result
numbers = (5, 2, 7, -1)

print("This is the result for multiplying the list: ", multiplyList(numbers))

