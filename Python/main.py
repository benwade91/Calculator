def add(n1, n2):
  """Adds two inputs"""
  return n1 + n2

def subtract(n1, n2):
  """Subtracts two inputs"""
  return n1 * n2

def multiply(n1, n2):
  """Multiplies two inputs"""
  return n1 * n2

def divide(n1, n2):
  """Divides two inputs"""
  return n1 / n2

operation = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide,
}

num_one = int(input("enter first number\n"))

print("select an operation")
for symbol in operation:
  print(symbol)

selection = input('')
selected_func = operation[selection]

num_two = int(input("enter second number\n"))

answer = selected_func(num_one, num_two)

print(f"{num_one} {selection} {num_two} = {answer}")