# Function to check if number is Prime
def is_prime(num):

    # Check if number equals or below 1 
    if(num <= 1):
        return False        # Not Prime
    
    # Check if number equals 2
    if(num == 2):
        return True         # Prime Number
    
    # Check if number is even
    if(num %2 == 0):
        return False        # Not Prime
    
    # Iterate through odd numbers from 3 to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):

        if num % i == 0:    # If divisible
            return False    # Not Prime
        
    return True             # Prime Number

# List to store prime numbers
prime_numbers = []

# Check for prime numbers between 1 and 100
for number in range(1, 101):

    # If number is prime, add to list
    if is_prime(number):
        prime_numbers.append(number)        

# Print the list of prime numbers
print("Prime numbers between 1 and 100 are:", prime_numbers)
