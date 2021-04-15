import random
human = input("Your choice? ")
comp = random.randint(1,3)
if comp==1:
  computer = "paper"
elif comp==2:
  computer = "scissors"
elif comp==3:
  computer = "stone"
print("Computer choice: " + computer)

if human== "paper" and computer  == "scissors":
  print("You lose")
elif human== "paper" and computer == "stone":
  print("You win")
elif human== "paper" and computer == "paper":
  print("Draw")
elif human== "scissors" and computer == "paper":
  print("You win")
elif human== "scissors" and computer == "stone":
  print("You lose")
elif human== "scissors" and computer == "scissors":
  print("Draw")
elif human== "stone" and computer == "scissors":
  print("You win")
elif human== "stone" and computer == "paper":
  print("You lose")
elif human== "stone" and computer == "stone":
  print("Draw")
else:
  print("Invalid input.")