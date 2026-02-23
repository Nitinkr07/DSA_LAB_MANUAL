def factorial(n):
    if n < 0:
        return "Invalid input! n must be >= 0"
    
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input("Enter n: "))

result = factorial(n)
print("Factorial:", result) 