#from replit import clear >>>> The teacher is able to use this module because they are writing it on 'replit', but when I try to write it here, it gives an error. Therefore, I found the following code on the web, which allows me to use 'clear'.

from os import system, name
clear = lambda: system("clear" if name == "posix" else "cls") #This code uses the "os" module in Python to clear the terminal screen. First, it imports the "system" and "name" functions from the "os" module. Then, it creates a lambda function named "clear" that uses the "system" function to clear the terminal screen. The lambda function checks if the operating system is "posix" (i.e., Unix or Linux), and if so, it uses the "clear" command to clear the terminal screen. Otherwise, it uses the "cls" command to clear the terminal screen for other operating systems. Finally, the "clear()" function is called, which executes the lambda function and clears the terminal screen. This code is useful when writing command-line applications or scripts that need to clear the terminal screen to provide a better user experience or to display information in a cleaner way. By checking the operating system and using the appropriate command to clear the screen, the code is made platform-independent, and it will work on any operating system that supports Python.
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record: # bidding_record = {"sema": 123, "nur": 321} like this
        bid_amount = bidding_record[bidder]
        if  bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}\n")

while not bidding_finished:
    name = input("What's your name? ")
    price = int(input("\nWhat's your bid? $")) #You wanna to scroll all, select them all and press 'tab'..
    bids[name] = price
    should_continue = input("\nAre there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()