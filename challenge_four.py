# Create a function that calculates the amount of time saved were you traveling with an average speed that is 
# above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.
# The parameter's format is as follows:
# (speed limit, avg speed, distance traveled at avg speed)
#Speed = distance/time
    #The time returned should be in minutes, not hours.
    #Round the answer to one decimal place.
    #The speed limit and average speed are both given in mi/hr

def time_saved(speed_limit, avg_speed, distance):
    """Calculates time saved speeding vs driving the speed limit"""
    limit = round((distance/speed_limit) * 60, 1)
    speeding = round((distance/avg_speed) * 60, 1)
    total_saved = (speeding - limit) * -1

    return total_saved


# Speed Limit
sl = float(input("What is the speed limit? ")) 
# Average Speed
avgs = float(input("What is the average speed above the limit? ")) 
# Distance Traveled
dt = float(input("What is the distance traveled? ")) 


saved = round(time_saved(sl, avgs, dt),1)

print(f"You have saved {saved} minutes by speeding! Congratulations!")
 