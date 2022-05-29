import random

#When you die this 0 turns into 1
dead = 0
print("You enter a maze..")
print("On your left is a dark path probably leading to more darkness.. straight before you is a path filled with light.. and on your right you see a path leading to some kind of yellow light..")
direction = input("Which direction do you want to go? (left = l, right = r, straight = s)")
#left
if direction == "l":
    print("You enter the dark path, you start to hear weird noises")
    print("At the end of the path you see a man standing before you")
    action = input("Do you want to talk to him? y/n ")
    if action == "y":
        print("You interact with the mysterios man and when he touches you.. you teleport out of the maze.")
    else:
        print("You decide not to talk with the mysterios man and continue in the maze")
        print("You continue exploring the dark path and end up lost and die due to hunger..")
#straight
elif direction == "s":
    print("You decided to go straight.. after going for few minutes you realise you are being watched by some kind of entity! ")
    interaction = input("Do you want to talk to the entity? y/n ")
    if interaction == "y":    
        print("The mysterios entity was an angel that only wants to help.. it says ""At the end of this path you will find two paths.. DONT GO RIGHT ITS EVIL PATH THAT LEADS ONLY TO DEATH, on the left you fill find exit""")
    else:
        print("You decide to ignore the entity and continue on your path")
    print("At the end of this path you find yourself before two paths left and right.")
    directionTwo = input("Which way are you going to go? (l = left, r = right)")
    if directionTwo == "l":
        print("You go left and find an exit! ")
    else:
        print("You decide to go right and you see an evil demon.. you try to run away as fast as you could but it caught up to you and it killed you..")
#right
else:
    print("You decide to go rigth to the glowy yellow light.. as you come close to the light you start to see Treasure Chest! ")
    open = input("Open the weird looking chest? y/n ")
    if open == "y":
        #random chance
        trap = random.randint(1,2)
        if trap == (1):
            print("In the chest you find an ancient holy grail you take it and continue.. ")
        if trap == (2):
            print("In turns out the chest was just a mimic! And it was hungry for a very long time.. It ate you..")
            dead = 1
    else:
        print("You decide not to open the chest")
    if dead == 0:
        print("As you continue you finally see an exit out of this maze! ")

 