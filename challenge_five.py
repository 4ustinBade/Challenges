#A city skyline can be represented as a 2-D list with 1s representing buildings. 
# In the example below, the height of the tallest building is 4 (second-most right column).
#Create a function that takes a skyline (2-D list of 0's and 1's) and 
# returns the height of the tallest skyscraper.

skyline = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0]]

def find_skyline_height():
    height = 0
    for row in skyline:
        print(row)
        if 1 in row:
            height += 1
        else:
            pass
    return height 

skyline_height = find_skyline_height()
print(f"The height of the skyline is {skyline_height}.") 
