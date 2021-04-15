import random
number=random.randint(1,100)
uname=input("enter your name:")
uname=uname.strip()
print(f"hello!{uname}")
print("lets start the game")
print("1].yes")
print("2].No")
option=input("select your option:")
option=int(option)
if option==1:
 guess=input("guess a number:")
 guess=int(guess)
while number!=guess:
 print
 if guess<number:
  print("your guess is lower")
  guess=input("guess a number:")
  guess=int(guess)
 elif guess>number:
  print("your guess in higher")
  guess=input("guess a number:")
  guess=int(guess)
 else :
  print("congratulations, you won")
  break
 
  
 
 
     


