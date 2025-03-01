#Martha Moreno Gonzalez
#02/28/2025
#Problem 4:takes a list of numbers and returns a new list with unique elements of the first list.  
#Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def uniqueElements(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [1, 3, 3, 3, 6, 2, 3, 5]

print("Unique list: ", uniqueElements(numbers))