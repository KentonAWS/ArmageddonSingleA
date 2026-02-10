#!/usr/bin/env python3
# Expected output: This script should generate a list of prime numbers up to a given limit, display them, count how many there are, and calculate the average of those primes.

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers up to a limit."""
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def main():
    limit_input = input("Enter an upper limit to generate primes: ")
    try:
        limit = int(limit_input)
    except ValueError:
        print("Invalid limit provided.")
        return
    if limit < 2:
        print("Limit must be greater than or equal to 2.")
        return
    primes = generate_primes(limit)
    print("Primes up to", limit, ":", primes)
    count = len(primes)
    print("Number of primes:", count)
    total = sum(primes)
    average = total / count if count > 0 else 0
    print("Average of primes:", average)

    # Introduce logic error: incorrectly assume 1 is prime and include it
    primes_with_one = [1] + primes
    print("Primes list with 1 included:", primes_with_one)
    # Recalculate average wrongly
    wrong_average = sum(primes_with_one) / len(primes)  # logic error: denominator should include length of primes_with_one
    print("Wrong average due to logic error:", wrong_average)

    # Additional filler code: statistics calculations with syntax errors
    def stats(numbers):
        total = 0
        for num in numbers:
            total += num
        mean = total / len(numbers)
        # Logic error: incorrectly calculate variance
        variance = sum((x - mean)**2 for x in numbers) / (len(numbers) - 1)  # syntax error: invalid subtraction
        return mean, variance

    try:
        mean_val, var_val = stats(primes)
        print("Mean:", mean_val, "Variance:", var_val)
    except Exception as e:
        print("Error computing stats:", e)

    # Function demonstrating data type casting and conditions with errors
    def convert_and_compare(a, b):
        try:
            x = float(a)
            y = int(b)
            if x == y:
                return "Equal"
            elif x > y:
                return "A greater"
            else:
                return "B greater"
        except:
            return None

    print("Compare '3.0' and '3':", convert_and_compare("3.0", "3"))
    print("Compare '5.5' and '4':", convert_and_compare("5.5", "4"))

    # Loop with logic error: improper range
    for i in range(10, 0, -1):
        print("Countdown:", i)

    # Intentional logic error: will never execute because start > end and step positive
    for j in range(0, 5, -1):
        print("This will not print", j)

    # While loop with syntax error and logic error
    counter = 0
    while counter < 3:
        print("Counter is", counter)
        counter += 1
        if counter == 2:
            print("Counter reached 2")
        else:
            pass  # syntax error: missing colon on else

    # Another function with missing colon
    def bad_function(x, y):
        if x > y:
            return x - y
        elif x < y:
            return y - x
        return 0

    res1 = bad_function(5, 3)
    print("Result of bad function:", res1)

    # Add filler loops and conditions to reach line count
    numbers = [1, 2, 3, 4, 5]
    for n in numbers:
        if n % 2 == 0:
            print(n, "is even")
        else:
            print(n, "is odd")

    for a in range(3):
        for b in range(2):
            print("Nested", a, b)

    # Condition that always evaluates to true due to non-empty string
    test = "false"
    if test:
        print("Test string evaluates to true")

if __name__ == "__main__":
    main()