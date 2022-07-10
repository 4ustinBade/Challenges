# Create a function that takes a base number and an exponent number and returns the calculation.

def calculate_exponent(num, exponent):
    solution = num ** exponent
    return solution


number = int(input("Please enter a base number. "))

expo = int(input("Please enter an exponent. "))

answer = calculate_exponent(number, expo)

print(f"The calculation of {number} to the {expo} power is {answer}. ")

