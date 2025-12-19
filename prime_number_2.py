import math

print("*" * 40)
print("\nwelcome to frizzbuzz prime number\n")
print("*" * 40, "\n")

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1, 6):
        if n % i == 0: 
            return False
    return True
                           
def is_prime_frizzbuzz(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} is frizzbuzz")
        elif is_prime(i):
            print(f"{i} is prime")
        elif i % 3 == 0:
            print(f"{i} is frizz")
        elif i % 5 == 0:
            print(f"{i} is buzz")
        else:
            print(i)
                            

is_prime_frizzbuzz(100)