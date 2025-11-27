# original_code.py

def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    result = 1
    
    for i in range(1, n + 1):
        result = result * i
    return result

print(f"Factorial of 5: {calculate_factorial(5)}")
