print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
a = input('You are at a cross road. Where do you want to go? Type "left" or "right"?\n').lower()
if a == "left":
    b = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across.\n').lower()
    if b == "wait":
        c = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if c == "yellow":
            print("YOU FOUND THE TREASURE! YOU WİN!")
        else:
            print("You chose a wrong door. Game Over!")
    else:
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")

#  a = input('You are at a cross road. Where do you want to go? Type "left" or "right"?\n')
#  b = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across.\n')
#  c = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')





