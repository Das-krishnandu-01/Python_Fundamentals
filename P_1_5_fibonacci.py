# Program 1.5: Calculate the nth Fibonacci number
def fibonacci(n):
  if n <= 0:
    return "Invalid input"
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
print(f"Fibonacci number at position {n} is:", fibonacci(n))