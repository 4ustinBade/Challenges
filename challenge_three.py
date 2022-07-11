# Create a function that takes two number strings and returns their sum as a string.

def add(num_one, num_two):
    final_answer = str(int(num_one) + int(num_two))
    return final_answer

input_one = input("Input first number. ")
input_two = input("Input second number. ")

answer = add(input_one, input_two)

print(f"The sum is {answer}. ")

    
