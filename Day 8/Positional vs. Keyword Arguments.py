<<<<<<< HEAD
#Functions with more than 1 ınput
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#greet_with("Sema", "Vadi İstanbul")
#greet_with("Vadi İstanbul", "Sema")

#Functions with "keyword arguments"
greet_with(name = "Sema", location = "Vadi İstanbul")
greet_with(location = "Vadi Istanbul", name = "Sema")


# Keyword Argument : Instead of just adding the arguments into the function call like this, we can actually add each of the parameter names and an equal sign to say that the first parameter a should be equal to one, b should be equal to two and c equals to three. And now when we actually change the order around, it doesn't matter how we order it, it still going to abide by these bindings. So c will still be three and a will still be one.
#def my_function(a, b, c):      in this >> a = 1, b = 2, c = 3
    #do this with a             Now, if we switch around the order of the arguments in the function call, now what will happen is a is going to be equal to the first argument.                   (3, 1, 2)>> a = 3, b = 1, c = 2 
    #then do this with b        If I use keyword arguments instead. So now, my_function(a=1, b=2, c=3)
    #finally do this with c              If I chance locations, nothing change (c=3, a=1, b=2).. Gives the same output

=======
#Functions with more than 1 ınput
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#greet_with("Sema", "Vadi İstanbul")
#greet_with("Vadi İstanbul", "Sema")

#Functions with "keyword arguments"
greet_with(name = "Sema", location = "Vadi İstanbul")
greet_with(location = "Vadi Istanbul", name = "Sema")


# Keyword Argument : Instead of just adding the arguments into the function call like this, we can actually add each of the parameter names and an equal sign to say that the first parameter a should be equal to one, b should be equal to two and c equals to three. And now when we actually change the order around, it doesn't matter how we order it, it still going to abide by these bindings. So c will still be three and a will still be one.
#def my_function(a, b, c):      in this >> a = 1, b = 2, c = 3
    #do this with a             Now, if we switch around the order of the arguments in the function call, now what will happen is a is going to be equal to the first argument.                   (3, 1, 2)>> a = 3, b = 1, c = 2 
    #then do this with b        If I use keyword arguments instead. So now, my_function(a=1, b=2, c=3)
    #finally do this with c              If I chance locations, nothing change (c=3, a=1, b=2).. Gives the same output

>>>>>>> 6484b5d (day 82)
#my_function(123)