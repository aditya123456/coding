def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_around_number(number):
    """Find the prime number greater than and less than the given number."""
    greater_prime = number + 1
    while True:
        if is_prime(greater_prime):
            break
        greater_prime += 1

    lesser_prime = number - 1
    while True:
        if is_prime(lesser_prime):
            break
        lesser_prime -= 1

    return lesser_prime, greater_prime

# Example usage
given_number = 7
lesser_prime, greater_prime = find_prime_around_number(given_number)
print(f"The prime number less than {given_number} is {lesser_prime}")
print(f"The prime number greater than {given_number} is {greater_prime}")
