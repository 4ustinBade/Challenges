# https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

import re

def is_consec():
    
    # USer input 
    array1 = input("Enter array one.")
    array2 = input("Enter array two.")
    combined_list = []
    # removing numbers from str input
    res1 = " ".join(re.findall(r"[0-9]+", array1))
    res2 = " ".join(re.findall(r"[0-9]+", array2))
    
    # Extract input and create merged list
    for x in range(0, len(res1)): 
        if res1[x] == " ":
            pass
        else:
            num = int(res1[x])
            combined_list.append(num)
    
    for x in range(0, len(res2)): 
        if res2[x] == " ":
            pass
        else:
            num = int(res2[x])
            combined_list.append(num)

    # Remove duplicates in the input
    nodupe = []
    
    for x in range(0, len(combined_list)) :
        if combined_list[x] not in nodupe :
            nodupe.append(combined_list[x])
    
    # Create consecutive list to compare
    nl = [nodupe[0]] 
    for x in range(1, len(nodupe)) :
        num = nodupe[0] + (1 * x)
        nl.append(num)

    # Compare lists to see if consecutive  
    if nodupe == nl :
        print(f"{nodupe} is consecutive. ")
    else:
        print(f"{nodupe} is not consecutive. ")


is_consec()

