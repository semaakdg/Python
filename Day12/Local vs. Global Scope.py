# In Python, a variable's scope determines the parts of the program where the variable is visible and accessible. The two main types of scope in Python are global scope and local scope.

# Global scope refers to variables that are defined outside of any function or class, and can be accessed from anywhere in the program. Local scope refers to variables that are defined inside a function or class, and can only be accessed from within that function or class. When you define a variable inside a function, it's considered a local variable and can only be accessed from within that function. If you try to access a local variable from outside the function, you'll get a NameError.

# On the other hand, if you define a variable outside of any function or class, it's considered a global variable and can be accessed from anywhere in the program, including inside functions and classes. However, if you try to modify a global variable inside a function, you need to use the global keyword to let Python know that you're modifying the global variable and not creating a new local variable. It's generally recommended to use local variables whenever possible, as they help prevent naming conflicts and make your code easier to understand and maintain. Global variables should be used sparingly and only when necessary, as they can make it harder to reason about the behavior of your program.

#Sure, here are some examples of using global and local scopes in Python:
#
#________________________________________________________________________________________________________________________________________________________________________
#Example 1: Modifying a global variable inside a function
x = 10  # Global variable

def my_function():
    global x  # We need to declare that we're using the global variable. Without this line of code we cannot modify something that is global within a local scope.
    x = 5  # Changing the value of the global variable
    print("my_function:", x)

print("Before:", x)  # Before: 10
my_function()
print("After:", x)  # After: 5

#In this example, we declare x as a global variable and then define a function my_function that modifies the value of x. We use the global keyword inside the function to tell Python that we're using the global variable x. When we call my_function, the value of x is changed from 10 to 5.

#________________________________________________________________________________________________________________________________________________________________________
#Example 2: Using a local variable outside a function
def my_function():
    x = 5  # Local variable
    return x

y = my_function()
print("y:", y)  # y: 5

print("x:", x)  # NameError: name 'x' is not defined

#In this example, we define a function my_function that creates a local variable x with the value of 5. When we call my_function, it returns the value of x which we then assign to the variable y. However, we cannot access the value of x outside the function and will get a NameError when trying to print its value.

#________________________________________________________________________________________________________________________________________________________________________
#Example 3: Local variable takes precedence over global variable
x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print("my_function:", x)

my_function()  # my_function: 5
print("global:", x)  # global: 10

#In this example, we define a global variable x and then define a function my_function that creates a local variable x with the value of 5. When we call my_function, the value of the local variable x is printed, which is 5. The global variable x remains unchanged and still has the value of 10.

#________________________________________________________________________________________________________________________________________________________________________
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# In this example, the variable enemies is defined in the global scope and has an initial value of 1. The function increase_enemies() is then defined, and within its scope, a new variable enemies is defined with a value of 2. This new variable is local to the function and is not the same as the global variable enemies. When the increase_enemies() function is called, the value of the local variable enemies is printed, which is 2. Finally, outside the function's scope, the value of the global variable enemies is printed, which is still 1 since the local variable enemies defined within the function does not affect the global variable. This illustrates the concept of variable scope in Python: variables defined within a function's scope are local to that function and do not affect variables defined outside of it. Global variables can be accessed from within a function, but if a variable is defined locally within a function, it will not affect the value of a global variable with the same name.


# THE MOST IMPORTANT THING TO REMEMBER FROM THIS IS IF YOU CREATE A VARIABLE WITHIN A FUNCTION, THEN IT'S ONLY AVAILABLE WITHIN THAT FUNCTION. BUT IF YOU CREARTE A VARIABLE WITHIN AN IF BLOCK OR A WHILE LOOP OR A FOR LOOP OR ANYTHING THAT HAS THE INDENTATION AND THE COLON, THEN THAT DOES NOT COUNT AS CREATING A SEPARETE LOCAL SCOPE.