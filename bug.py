def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case to avoid ZeroDivisionError
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")