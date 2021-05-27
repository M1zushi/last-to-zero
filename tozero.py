# Imports random library; need for randint
# Randint (for choosing a random integer)
import random

# Sets Constant Variables
num = 25
change = 0
cguess = 0
game = True
win = True
early = 1
late = 0
temp = late

# Prints Welcome Message + Game Intructions
print('''Welcome to the Number Game!
 + Each round you choose a value from 1-3 (ONLY) to lower the number by
 + In the same round the computer will also choose a number to lower the value with as well
 + The rounds will go on until the number reaches 0
 + Your goal is to avoid being the one that makes the number reach 0
 + Good Luck!
''')

# Starts the game loop
while game:
  # To not send uncessary stuff the first time
  if early == 0:
    # To only send when parameters are met
    if temp != late:
      temp = late
      print(f'\n\nThe computer decided to lower the number by {cguess}')
    else:
      pass

  elif early == 1:
    early -= 1

  # Sends the current value
  print(f'\nCurrent Value: {num}\n')

  # Allows player to choose their input
  change = int(input('\nHow much would you like to lower the number by: '))

  # Checks if player choice is valid
  if change <= 3:
    if change >= 1:
      num -= change

      # Checks if player lost
      if num <= 0:
        win = False
        game = False
        break

      # Computer's guess
      cguess = random.randint(1,3)
      num -= cguess

      # Checks if computer lost
      if num <= 0:
        win = True
        game = False

      # Helps check parameters above
      late += 1

    # Indirect Error Handling (if choice < 1)
    else:
      print('\n\n\n ! Please input a number that is 1 or higher !\n\n')
  # Indirect Error Handling (if choice > 3)
  else:
      print('\n\n\n ! Please input a number that is 3 or lower !\n\n')

# Win Message
if win:
    print('''

-------------------------
Congratulations! You win!
-------------------------

''')

# Loss Message
elif win == False:
    print('''

-------------------
Good Try! You lost!
-------------------

''')
