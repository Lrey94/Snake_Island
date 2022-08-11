def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide}

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")

num2 = float(input("What's the next number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

carry_on = input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit:")

carry_on_calculating = True

while carry_on == 'y':
    operation_symbol = input("Pick an operation: ")
    num3 = float(input("What's the next number?:"))
    calculation_function = operations[operation_symbol]
    answer2 = calculation_function(answer, num3)
    print(f"{answer} {operation_symbol} {num3} = {answer2}")
    answer = float(answer2)
    carry_on = input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit:")
