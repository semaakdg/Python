"""
In Python, 'return' and 'print' are used for different purposes.

'print' is used to display a message or value on the screen while the program is running. For example, if we want to see a value that the user entered in a program, we can use 'print' to display it on the screen. However, 'print' only displays the value and we cannot use it later in the program. Therefore, 'print' is generally used to provide information about how the program is running.

'return' is used to make a function return a value. Functions are blocks of code that perform a specific task and return a result. The 'return' statement returns the result of the function, which we can use later in the program. For example, when a function needs to perform a calculation and return the result, we use the 'return' statement.

In addition, 'print' and 'return' return different types of values. 'print' only displays a message or value on the screen and does not return any value. 'return', on the other hand, returns a value that is passed back to the place where the function was called. Therefore, when we need to use the result of a function, we use 'return'.

In summary, 'print' is used to display a message or value on the screen, while 'return' is used to return a result from a function.
"""
# Calculator
#Add
def add(n1,  n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")


operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")



