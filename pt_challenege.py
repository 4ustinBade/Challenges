#Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM

def format_date(date) : 
    list = []
    final_string = ''
    # turn string into a list
    for x in range(len(date)):
        list.append(date[x])
    # Remove '/' from list
    for x in range(len(list)-2):
        if list[x] == '/' :
            list.remove(list[x])
        else:
            pass
     # Reformat date to front
    for z in range(4):
        list.append(list[0])
        list.pop(0)
    # Final format
    for i in range(len(list)):
        if i <= 3 or i >= 6:
            pass
        else:
            list.append(list[4])
            list.pop(4)
    #turn list into string
    for x in range(len(list)):
        final_string += list[x]
    
    return final_string


user_input = input("Type date in format mm/dd/yyyy.\n")
answer = format_date(user_input)
print(answer)