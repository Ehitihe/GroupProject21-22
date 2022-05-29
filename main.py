#this is where all of the code will be

# option 1 - combat with a goblin
def combat(): test
  import random

  print("You have chosen option 1 \n")
  print("You enter a dark-looking cave. You walk around for a moment, something does not feel right. Suddenly, a goblin appears in front of you. \n 'Mmmmmmm... FOOD' it yells at you. 'I am not food! I am a human being!' you cry back at it. 'Food cannot beat me in combat. Therefore, if you beat me, you are not food. HOWEVER, if I beat you, I WILL EAT YOUUUU!!!'\n")
  print("To not get eaten by a goblin, win at a simple game of rock-paper-scissors-lizard-spock.\n")
  print("\t[r] - rock\n\t[s] - scissors\n\t[p] - paper\n\t[l] - lizard\n\t[S] - Spock")

  a = int(input("\nYou get to choose, how many rounds you will play: "))

  playerScore = 0
  pcScore = 0

  while True:
    for i in range (a):
      player = input("Choose wisely: ")

      if player == "r" or player == "p" or player == "s" or player == "l" or player == "S":
        print("")
      else:
        print("\nThe goblin does not understand! It feels outsmarted and eats you!")
        break

      computer = random.choice("rsplS")
      print(computer)

      if player == "r" and computer == "s":
        playerScore += 1
        print("\nYou win this round")

      elif player == "r" and computer == "l":
        playerScore += 1
        print("\nYou win this round")

      elif player == "s" and computer == "p":
        playerScore += 1
        print("\nYou win this round")

      elif player == "s" and computer == "l":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "p" and computer == "r":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "p" and computer == "S":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "l" and computer == "S":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "l" and computer == "p":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "S" and computer == "r":
        playerScore += 1
        print("\nYou win this round.")

      elif player == "S" and computer == "s":
        playerScore += 1
        print("\nYou win this round.")



      elif computer == "r" and player == "s":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "r" and player == "l":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "s" and player == "p":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "s" and player == "l":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "p" and player == "r":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "p" and player == "S":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "l" and player == "S":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "l" and player == "p":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "S" and player == "s":
        pcScore += 1
        print("Goblin wins this round.")

      elif computer == "S" and player == "n":
        pcScore += 1
        print("Goblin wins this round.")


      elif computer == "r" and player == "r":
        print("It is a draw.")

      elif computer == "s" and player == "s":
        print("It is a draw.")

      elif computer == "p" and player == "p":
        print("It is a draw.")

      elif computer == "l" and player == "l":
        print("It is a draw.")

      elif computer == "S" and player == "S":
        print("It is a draw.")


    print("\n")

    print("The combat has ended.")
    print("The goblin scored " + str(pcScore) + " points.")
    print("You scored " + str(playerScore) + " points.")

    print("\n")

    if pcScore > playerScore:
      print("Goblin has won. You are now being eaten by him. Sorry.")

    elif pcScore < playerScore:
      print("You won! The goblin is mad but lets you go.")

    elif pcScore == playerScore:
      print("It is a draw. The goblin does not understand this outcome. As he tries to use his brain to understand it, you slip by him.")

    break
combat()


# option 2 - look behind and find an aisle
def lookBehind():    
    from time import sleep
    from random import randint
    def coin(): # the coin function flips a coin
        if(randint(0,100)<50):
            return "l"
        else:
            return "r"
    def progress(delay, text): # the progress function prints the actual text of the game with the delay needed
        for n in range(len(text)):
            sleep(delay)
            print(text[n])
    def load(save): # the load function is for loading player's save
        if(save == "y"):
            print("Your save has just loaded\n ")
            return True
        else:
            return False
    def linSearch(answer, options): # the linSearch is searching whether the answer entered is within the correct ones
        for v in range(len(options)):
            if(answer != options[v]):
                pass
            else:
                return True    
    # INTRODUCTION
    progress(1.7, ["", "You've just looked behind you, and found stairs leading to quite odd-looking narrow aisle.","You're walking through the aisle","", "At the end of the aisle there're two doors.\nWhich of them will you enter?"])
    save = input("Would you like to save the game before you choose the door? (y/n)")
    print("")
    # THE ACTUAL GAME
    runs = True
    while(runs == True): # loop is used to make loading possible
        runs = False
        doorOpt = input("Which of them will you choose?\n A) The left one\n B) The right one\n C) Flip a coin") # CHOOSING A DOOR
        if(doorOpt =="A" or doorOpt =="a"): 
            door = "l"
            runs = False
        elif(doorOpt =="B" or doorOpt =="b"):
            door = "r"
            runs = False
        else:
            print("Flipping a coin")
            door = coin()
            runs = False

        if(door == "l"): # ENTERING THE DOOR
            ending = ["THE END."]
            print("You're entering the left door.")
            sleep(0.7)
            progress(1.7, ["As you were walking down the dark creepy aisle, you've suddenly tripped over a rock and fell into a hole.", "As you're falling, you discover that the hole itself is incredibly deep.", "", "It has to be the mythical hole of deepness.\nYou're falling into the deep of the deepness forever..."])
            runs = load(save)
            save = "n"
        else:   
            print("You're entering the right door.")
            sleep(0.7)
            progress(1.7, ["", "As you walked throuh the door, you can see a small misty room full of dust and old jumble.", "You almost think, that there's nothing to do, and that the treasure must be somewhere else.", "But suddenly you can hear...\n 'Hello adventurer! I am The Dentist..., looking for the treasure aren't you? ...'", "'I have a BIG treasure. Let's have some fum ... and play a game for it.'", ""])
            game = input("Will you accept the Dentist's offer?(y/n)")
            if(game == "n"):
                ending = ["THE END."]
                print("You're leaving empty handed. \nWHAT A SHAME!")
                runs = load(save)
                save = "n"
                break
            else:
                progress(1.4, ["You've just carefully decided to accept this wacky offer.", "'These are the rules ...' says the Dentist:\n'I'll give you a few riddles and each right answer is one point.", "If you don't know the answer you can ask for help\n, but after the advice, your answer is worth only half the point.'"])
                questions = ["What has to be broken before you can use it?", "What is always in front of you, but can't be seen?", "What goes up, but never goes down?", "What can’t talk but will reply when spoken to?"]
                answers = [["an egg", "egg", "b", "B"], ["the future", "a future", "future", "c", "C"], ["an age", "age", "the age", "your age", "a", "A"], ["an echo", "echo", "your echo", "c", "C"]]
                helps = ["\n A) a chicken\n B) an egg\n C) old radio", "\n A) the air\n B) your glasses\n C) your future", "\n A) an age\n B) a rocket\n C) a baloon", "\n A) a dog\n B) a polititian\n C) an echo"]
                print("The first question: \n ")
                points = 0.0
                for m in range(len(questions)): # guessing the riddles, the player has a possibility to ask for advice with the answer
                    answer = input(questions[m] + "(if you need some help enter 'h')")
                    if(linSearch(answer, answers[m]) == True):
                        points = points + 1
                        print("You're totally right.\n  points: " + str(points))
                    elif(answer == "h"): # gives the player a posibility to take an advice while guessing the right answer
                        answer = input(questions[m] + "\n(a/b/c) The options are: ... " + helps[m])
                        if(linSearch(answer, answers[m]) == True):
                            points = points + 0.5
                            print("You're totally right.\n  points: " + str(points))
                        else:
                            print("Ha! You missed this one.")
                    else:
                        print("Ha! You missed this one.")
                if(points >= 2.5): # evaluating the ending of the game (GOOD/BAD)
                    ending = ["CONGRATULATIONS!\nWith "+ str(points)+" points; You've just won the treasure.", "The Dentist gave you a chest.", "And the chest ... is full of golden teeth?!", "THE END."]
                    runs = False
                else:
                    ending = ["As you can see the old laughing man, when the game ended, you discover, that the treasure probably doesn't even exist", "Maybe there's a bigger probability finding some with a detector on the fields nearby.", "You're leaving the dusty room empty-handed.", "THE END."]
                    runs = False
    progress(1.4, ending)    
lookBehind()
