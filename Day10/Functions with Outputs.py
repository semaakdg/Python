#Functions with Outputs

def format_name(f_name, l_name): # f > first  l > last
    print(f_name.title())#You might have spotted already that this 'title' function actually has an output. It returns a version of the string where each word is title cased. Instead of simply just printing this, we can also capture it inside a variable. 
    print(l_name.title())
# Let's create a new variable called formatted_f_name and also formatted_l_name. Now what's happening here is we are transforming this input f_name, turning it into title case. And then once this function executes, it has an output and that output replaces this part of the code and then it gets stored inside this variable. 
    formated_f_named = f_name.title()
    formated_l_named = l_name.title()
# Now we can go ahead and print the final version of our function which is going to use an fstring to take the formatted Fname and then add a space and then print out the formatted Lname, like this. 
    #print(f"{formated_f_named} {formated_l_named}")
# Now, if I start out with my first name but all in strange sort of casing, and then my last name in all caps, let's go ahead and hit run and see what happens. You can see that my first name gets converted to title the case, my last name gets converted to title case and then that result is stored in formatted Fname and this result becomes stored in this Lname, and then they get printed and formatted, like so

#format_name("SemA NUr", "akDaĞ")

#Now instead of printing this result out, we could also return it as well. In the same way that this title function returns the output, replaces this part of the code, we can also do the same with our format_name function. So let's delete the print function and go ahead and use 'return' instead. 
    return f"{formated_f_named} {formated_l_named}"
# Now this formatted string becomes the output and as we mentioned before, what happens with functions with outputs is this output replaces the part of thecode where the function was called. Now, if this is the string that we want to print, then all we have to do is just to save the output which replaces this part of the code inside a variable like this.
format_stinrg = format_name("seMA nUr", "akDaĞ")
#  And then
print(format_stinrg)
#  all we have to do is just go ahead and print that formatted string. As you can see, when I run the code, the same thing happens. 
# You can, and you might've alternatively, just taken this function call and put it straight inside the print statement. That works exactly the same way.
print(format_name("seMA nUr", "akDaĞ"))