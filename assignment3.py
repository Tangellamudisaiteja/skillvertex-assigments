# Read numbers from data.txt
with open("data.txt", "r") as file:
    numbers = [int(num) for num in file.read().split(',')]

# Calculate max, min, and sum
max_num = max(numbers)
min_num = min(numbers)
sum_nums = sum(numbers)

# Write results to results.txt
with open("results1.txt", "w") as result_file:
    result_file.write(f"Numbers: {numbers}\n")
    result_file.write(f"Maximum: {max_num}\n")
    result_file.write(f"Minimum: {min_num}\n")
    result_file.write(f"Sum: {sum_nums}\n")