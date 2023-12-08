def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Input range from the user
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))

    if first_num >= second_num:
        raise ValueError("Wrong range")

    # Find and print prime numbers
    print(f"Prime numbers between {first_num} and {second_num} are:")
    for num in range(first_num, second_num + 1):
        if is_prime(num):
            print(num, end=" ")

except ValueError as e:
    print(f"Error: {e}")