travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 
def add_new_country (country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country) #remember that the travel log is actually at its base, a list. So instead of adding to it like we have been doing when we're using a dictionary, in order to add to lists if you remember, you should probably use the function append.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
