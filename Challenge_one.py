# Create a function in Python that accepts one parameter: a string that’s a sentence. 
# This function should return True if any word in that sentence contains duplicate letters 
# and False if not.

def check_word(word):
    """Checks to see if a letter in submitted word is used more than once"""
    checked_letters = []
    Repeat = False
    for letter in word:
        if letter in checked_letters:
            Repeat = True
            break
        else:
            checked_letters += letter
    return Repeat

Run_Program = True

while Run_Program:
    # Get Input
    user_input = input("Input a string. ").lower()

    #Check Word for Duplicate letters
    Result = check_word(user_input)

    #Return Results
    if Result == True:
        print("There were multiple of the same letter in the given word.")
    else:
        print("There were no duplicate letters in the submitted word.")
    
    restart = input("Would you like to restart? y/n : ")
    
    if restart == "n":
        Run_Program = False
    else:
        pass


