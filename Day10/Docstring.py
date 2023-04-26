# In Python, docstring is a documentation string that immediately follows a function or class definition. The docstring explains the purpose of the function or class, its parameters, the values it returns, and other important details. This helps other programmers understand what the function or class does and improves the readability of the code.

# A docstring is defined using three double quotes (""") or three single quotes ('''). The following example demonstrates the use of a docstring for a function:
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.

    Returns:
    int: The sum of a and b.
    """
    return a + b

# In this example, a function named 'add_numbers' is defined. The docstring explains the purpose of the function, its parameters, and the value it returns. Below the docstring is the actual code for the function.

# Another benefit of using a docstring is that it can be used by the Python REPL (Read-Eval-Print Loop). The REPL is a tool used to interactively run Python code. By typing the name of a function in the REPL, you can view its docstring. For example:
# >>> help(add_numbers)
#Help on function add_numbers in module __main__:

#add_numbers(a, b)
#   This function adds two numbers and returns the result.

#   Parameters:
#   a (int): The first number to add.
#   b (int): The second number to add.

#   Returns:
#   int: The sum of a and b.


# This is the documentation output produced by the Python REPL, which shows the function's docstring.

# Docstring can also be used for class definitions and can describe the purpose of the class, its properties, and its methods. The following example demonstrates the use of a docstring for a class:
class Person:
    """
    This class represents a person with a name and age.

    Attributes:
    name (str): The person's name.
    age (int): The person's age.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        """
        This method prints a greeting message.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# In this example, a class named 'Person' is defined. The docstring explains the purpose of the class and its properties.