"""The Collatz sequence is as follows:

    Start with some given integer n.
    If it is even, the next number will be n divided by 2.
    If it is odd, multiply it by 3 and add 1 to make the next number.
    The sequence stops when it reaches 1.

According to the Collatz conjecture, it will always reach 1. If that's true, you can construct a finite sequence following the aforementioned method for any given integer.

Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence.
"""

def collatz(num):
    not_one = True
    number = int(num)
    list = [num]
    while not_one != False:
        if number == 1:
            not_one = False
        elif number % 2 == 0:
            number = number / 2
            list.append(int(number))
        elif number % 2 == 1:
            number = number * 3 + 1
            list.append(int(number))
    return list


print("Welcome to the Collatz Sequence!")

user_input = int(input("Pick a number : "))
list = collatz(user_input)
highest_int = max(list)

print(f"This is the sequence of numbers generated : {list}")
print(f"The highest integer is : {highest_int}")
    