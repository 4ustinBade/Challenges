# https://edabit.com/challenge/iBqJcagS56wmDpe4x


pi = 3.1415916535897743

def volume_shell(r1, r2) :
    volume = (4/3)*pi*(pow(r1,3)-pow(r2,3))
    volume = round(volume,3)
    return volume

print(volume_shell(3,800))


