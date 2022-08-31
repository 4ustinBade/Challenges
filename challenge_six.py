def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    
def find_prime_one(input):    
    prime_one = 0
    for x in range(2, input):
        if is_prime(x):
            prime_one = x
    return prime_one


def find_prime_two(input):    
    prime_two = 0
    for x in range(input+1, (input * 2)):
        if is_prime(x):
            prime_two = x
            break
    return prime_two


def find_interprime(num, p1, p2): 
    diff_one = num - p1
    diff_two = p2 - num
    if diff_one == diff_two: 
        return True
    else:
        return False


user_input = int(input("Insert a number. "))

prime_one = find_prime_one(user_input)
prime_two = find_prime_two(user_input)
is_interprime = find_interprime(user_input, prime_one, prime_two)

primes = [prime_one, prime_two]

if is_prime(user_input) or not is_interprime: 
    print(f"{user_input} is not interprime. ")
elif is_interprime :
    print(f"The two prime numbers that {user_input} is interprime to is {primes[0]} and {primes[1]}. ")






        
    






    

    
