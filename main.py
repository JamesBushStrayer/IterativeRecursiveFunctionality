# James Alan Bush
# CIS261002VA016-1236-001: Object-Oriented Computer Prog
# Iterative and Recursive Functionality


# Iterative factorial function
def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


# Recursive factorial function
def factorial_recursive(n):
  if n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)


# Call the functions
functions = [factorial_iterative, factorial_recursive]
strings = ["Iterative factorial function", "\n\nRecursive factorial function"]
factorials = [0, 5, 10, 25, 50, 100]

for function_index in range(len(functions)):
  print(strings[function_index])
  for factorial_index in range(len(factorials)):
    result = functions[function_index](factorials[factorial_index])
    print(f"!{factorials[factorial_index]}: {result}")
