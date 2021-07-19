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

num_one = float(input("enter first number\n"))

def calculate_func(num_one, operation):
    print("select an operation")

    for symbol in operation:
        print(symbol)

    selection = input('')
    selected_func = operation[selection]

    num_two = float(input("enter another number\n"))

    answer = selected_func(num_one, num_two)

    return answer

continue_calc = True

while continue_calc:
    answer = calculate_func(num_one, operation)

    print(f"The answer is {answer}")

    num_one = answer

    prompt_continue = input('continue calculating? y or n \n')

    if not prompt_continue == 'y':
        continue_calc = False
