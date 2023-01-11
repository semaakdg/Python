import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items -1)
#Pick out random person from list of names using the random number.
random_name = names[random_choice]
print(f"{random_name} is going to buy the meal today!")

