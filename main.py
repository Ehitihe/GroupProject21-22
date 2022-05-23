#this is where all of the code will be

# option 1 - combat with a goblin
def combat():
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
