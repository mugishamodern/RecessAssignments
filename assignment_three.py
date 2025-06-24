# Assignment 3: find the factorial of the number 5 (five), 5!
# Name: ______________________
# Date: ______________________

# Calculate factorial of 5
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}") 