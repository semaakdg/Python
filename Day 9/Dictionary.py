#dictionaries in Python work kind of similarly to dictionaries in real life, right? So if you were to look up a word in the dictionary say the word code, then you might find the definition as something along the lines of program instructions for the computer. And dictionaries are really useful because they allow us to group together and tag related pieces of information. The way I like to think about dictionaries is in the form of a table. Every dictionary has two parts to it. On the left hand side is the key, and that is the equivalent of the word in the dictionary, and then it's also got an associated value. That would be the equivalent of the actual definition of the word. Now let's say that we took this variation simple table of definitions of programming words that we've come across so far and we go ahead and we try to convert it right into a dictionary, how would we do that? Let me firstly drop the last two rows and let's just start with the first one. The first thing we want to do is we want them to create a dictionary. And to do that in Python, this is what the syntax looks like.We have a set of curly braces and everything that's inside the curly brace is the content of our dictionary. The key goes first followed by a colon and then followed by the value. In our table we've got this word bug, which is the first key, so we can replace that over here in our dictionary. And the value that's associated with this key is the definition for a bug. So an error in a program that prevents the program from running as expected, that becomes the value and can be replaced here after the colon. So now, we've created an actual dictionary using Python code. What if you wanted to have more than one entry in your dictionary? Well, you would separate each of the key value pairs using a comma, and then you can continue adding key and value pairs until you get to the end of your dictionary.
                # example:
#       key:         value:
#       bug        An error in a program...
#     function     A piece of code that you can...
#       loop       The action of doing something... 
# If we create a dictionary;
programming_dictionary = {
   "bug": "an error in a program...",
   "function": "Apiecce of code that you can...",
   "loop": "The action of doing something...",
   123: "example numbers"
}
# can write like this, and Ican call it like:
print(programming_dictionary["bug"])
print(programming_dictionary[123])

# Adding new items to  dictionary: 
# All you have to do is to tap into the dictionary, which is called programming dictionary in our case and again, using square brackets, we define the key. The key I'm going to add is our loop. And then after a equal sign, I get to assign the value. So in my case, the value is going to be the definition for a loop. And now when this line of code is executed and we go ahead and just print the programming dictionary after this has happened, then we'll see that it's actually different from what we had before.
programming_dictionary["Angela Yu"] = "My python teacher."
print(programming_dictionary)

# You can also create an empty dictionary by simply creating a set of curly braces with nothing inside. And then at a later stage, you can add to your dictionary by using this method that you saw up.
empty_dictionary = {}
empty_dictionary = []

# Wipe an existing dictionary:
programming_dictionary = {}
print(programming_dictionary)
# In here; I'm going to say programming dictionary equals empty dictionary. And now if I write print statement down here, then you can see that when it prints out, it's actually going to be completely empty. That can be really useful if you wanted to clear out a user's progress or for example, if a game restarts..

# Edit an item in a dictionary: 
# Now let's say that a bug is instead 'A moth in your computer.' Now, if I go and print my programming dictionary once more, then you can see that the definition for our bug has now just been changed.
programming_dictionary["bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary: let's say we are using a for loop. And we say for, 'thing' in programming dictionary, let's go ahead and print this thing each time.
for thing in programming_dictionary:
   print(thing)
#ıts give me just 'bug, function, loop, 123, Angela Yu' 
# All right. Is that what you expected? Because it certainly wasn't what I expected when I first learned Python. I thought it would give me each of the items in the dictionary with this key and its value. But instead this code actually just gives you the keys.

# But instead this code actually just gives you the keys. Now, of course, once you do have access to the key, instead of thing, I should actually really say for key in programming_dictionary. If I wanted to print the key, then of course I could just write print key. But if I wanted to get hold of the value, I could equally just as easily tap into my dictionary, use the square brackets and pass in that key. So now when I hit run, you can see it's giving me first the key from 'print(key) and then secondly the value based on 'print(programming_dictionary[key])'.
for key in programming_dictionary:
   print(key)
   print(programming_dictionary[key])