#make a function that uses try except

def divide(x, y):
    try:
        answer = x // y
        print(f"answer is {answer}. ")
    except ZeroDivisionError:
        print("No dividing by zero ")

 
divide(2, 0)

#basically if else but the else is triggered by a specific error




