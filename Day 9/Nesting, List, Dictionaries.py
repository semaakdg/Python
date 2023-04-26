#Now that we've seen lists as well as dictionaries I want to talk about a concept that you often see in both of these collection types and that's something called nesting. Now, if we imagine a list or a dictionary being something like a folder where lots of things can be stored inside it, then nesting lists and dictionaries is just a matter of putting one inside the other. For example, here;s a dictionary that is very simple, it's only got one key-value pair. Now we know that we can add multiple key-value pairs into the same dictionary by just adding a bunch of commas to separate them. 
#{
#   key: value,
#   key2: value2,
#}

# Now, what if instead of having a simple value like a string or a number, I could also put a 'list' as a value as well. 
#{
#   key: [List],
#   key2: value2,
#}
# Similarly, I could also use a dictionary as a value. 
#{
#   key: [List],
#   key2: {Dict},
#}
# In this case we've got a list as the value for key, this first one, and we've got a dictionary as the value for key2. Notice how this is a list and a dictionary nested inside another dictionary.

# The structure gets a little bit more complex, but it gives us more flexibility when we're trying to store more complex pieces of data.

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary

travel_log = {
  "France": "Paris", "Lille", "Dijon",
  "Germany": "Berlin", "Hamburg", "Stuttgart",
}
#then I would be able to represent even more complex data. For example, if I had a travel log where I was going to collect a dictionary of all the cities I had been for each of the countries I've traveled to. So for example, if I had traveled to France and I wanted to say that I've been to multiple cities, I can't simply just say Paris, and then Lille, Dijon, that doesn't really work because each key can only have one value. The only way that we can make these three pieces of data one value is by turning it into a list, like so. So now in our travel log dictionary as represented by the curly braces, we have one key value pair and it just so happens that the value in this case is a list. 
# (like this)
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionary in a List

#Now that we've seen nesting lists inside dictionaries, dictionaries inside dictionaries, the last thing I want to show you is nesting a dictionary inside a list. So we could basically have multiple dictionaries inside a single list. So remember that lists are ordered and they're accessed by the positions inside the list. So this dictionary would be the item at index zero, this one at index one and so on and so forth.

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]