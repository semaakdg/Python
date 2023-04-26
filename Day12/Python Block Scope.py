#Python does NOT have block scope, unlike some other programming languages like C or Java. In Python, variable scope is determined by functions and modules. When a variable is defined within a block, such as an if statement or a for loop, it is still accessible outside of that block, as long as it is defined within the same function or module. This is because in Python, the block itself does not create a new scope.

#For example:
def some_function():
    x = 10
    if x > 5:
        y = 20
    print(y)

some_function()

#In this code, the variable x is defined within the function some_function(). The if statement creates a new block, but the variable y defined within it is still accessible outside of the block because the block does not create a new scope. However, if the if statement had been defined within another function, the variable y would not be accessible outside of that function.

#____________________________________________________________________________________________________________________________________________
#if blocks:
x = 10

if x > 5:
    y = x * 2
    print(y)

print(y)  # y was only defined inside the if block, will raise an error here

#____________________________________________________________________________________________________________________________________________
#for loop blocks:
for i in range(3):
    message = "Hello, World!"
    print(message)

print(message)  # message was only defined inside the for loop, will raise an error here

#____________________________________________________________________________________________________________________________________________
#Functions:
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(total)  # total was only defined inside the function, will raise an error here

#____________________________________________________________________________________________________________________________________________
#with blocks:
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

print(content)  # content was only defined inside the with block, will raise an error here


#here are examples that will not raise errors due to block scope:
#Using global variables:
x = 10

def change_x():
    global x
    x = 20

print(x)  # 10
change_x()
print(x)  # 20

#____________________________________________________________________________________________________________________________________________
#Using a default argument:
def print_message(message="Hello, World!"):
    print(message)

print_message()  # Hello, World!
print_message("Goodbye!")  # Goodbye!

#____________________________________________________________________________________________________________________________________________
#Using list comprehension:
numbers = [1, 2, 3]
squares = [num ** 2 for num in numbers]

print(squares)  # [1, 4, 9]

#____________________________________________________________________________________________________________________________________________
#Using generator expressions:
numbers = [1, 2, 3]
squares = (num ** 2 for num in numbers)

print(list(squares))  # [1, 4, 9]



#In summary, while Python does not have block scope, it does have function and module scope. Variables defined within a block can still be accessed outside of it as long as they are defined within the same function or module.

