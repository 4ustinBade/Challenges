#Input number if inteprime show whic to primes its inbetween
num = int(input("Insert a number. "))

def find_prime_one(number):
    prime_one = 0
    if number > 1:
        for i in range(2, number):
            if (num % i) == 1 and i > prime_one:
                prime_one = i
    return prime_one


def find_prime_two(number, p1):
    prime_two = number + 1
    distance = number - p1
    high = distance + number
    for x in range(number , high):
        number +=1
        if (number % x) == 1 and x >= prime_two:
            prime_two = x
            break
    return prime_two

prime_one = find_prime_one(num)
prime_two = find_prime_two(num, prime_one)

print(prime_one)
print(prime_two)






    

    
