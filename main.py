# Street fighter game base
# Abigail Curiel

import random

#genInputFor<NAME_OF_CHARACTER_A>
def genInputForGUILE():
  move = random.randint(1,5)
  if move == 1:
    return "LRB"
  elif move == 2:
    return "DUA"
  elif move == 3:
    return "RB"
  elif move == 4:
    return "DLURA"
  else:
     move == "#####"

#genInputFor<NAME_OF_CHARACTER_B>
def genInputForEHONDA():
  move = random.randint(1,5)
  if move == 1:
    return "BBBBB"
  elif move == 2:
    return "LRB"
  elif move == 3:
    return "DUA"
  elif move == 4:
    return "LRLRB"
  else:
    move == "#####"

#move<NAME_OF_CHARACTER_A>
def moveGUILE(move):
  if move == "LRB":
    return "SONIC BOOM"
  elif move == "DUA":
    return "FLASH KICK"
  elif move == "RB":
    return "SPIN BACK KNUCKLE"
  elif move == "DLURA":
    return "SUPER COMBO: DOUBLE FLASH"
  else:
    return "MISS"

#move<NAME_OF_CHARACTER_B>
def moveEHONDA(move):
  if move == "BBBBB":
    return "HUNDRED HAND SLAP"
  elif move == "LRB":
    return "SUMO HEADBUTT"
  elif move == "DUA":
    return "SUMO SMASH"
  elif move == "LRLRB":
    return "SUPER COMBO: SUPER KILLER HEAD RAM"
  else:
    return "MISS"

#damage<NAME_OF_CHARACTER_A>
def damageGUILE(move):
  if move == "LRB":
    return 34
  elif move == "DUA":
    return 33
  elif move == "RB":
    return 13
  elif move == "DLURA":
    return 63
  else:
    return 0

#damage<NAME_OF_CHARACTER_B>
def damageEHONDA(move):
  if move == "BBBBB":
    return 48
  elif move == "LRB":
    return 22
  elif move == "DUA":
    return 40
  elif move == "LRLRB":
    return 66
  else:
    return 0
# OPTIONAL: CODE A FUNCTION TO PRINT THE SCORE
# def printScore(nameA, nameB, staminaA, staminaB):


# Now code the main program:
# CODE YOUR VARIABLES HERE:
staminaGUILE = 100
staminaEHONDA = 100
guileMove = genInputForGUILE()
guileName = moveGUILE(guileMove)
guileDamage = damageGUILE(guileMove)
ehondaMove = genInputForEHONDA()
ehondaName = moveEHONDA(ehondaMove)
ehondaDamage = damageEHONDA(ehondaMove)

# NOW, CODE THE LOGIC TO RUN ROUND 1:
print("ROUND ONE. FIGHT!")
print("PLAYER GUILE = ", str(staminaGUILE), ". PLAYER E. HONDA = ", str(staminaEHONDA))
#print("PLAYER GUILE. ENTER YOUR INPUT: ")
print("PLAYER GUILE ENTERED ", guileMove)
print(guileName, " = ", guileDamage, "DAMAGE")
staminaEHONDA = 100 - guileDamage
print("PLAYER GUILE = ", staminaGUILE, ". ", "PLAYER E. HONDA = ", staminaEHONDA)
print("PLAYER E. HONDA. ENTER YOUR INPUT: ")
print("PLAYER E. HONDA ENTERED ", ehondaMove)
print(ehondaName, " = ", ehondaDamage, "DAMAGE")
staminaGUILE = 100 - ehondaDamage
print("PLAYER GUILE = ", staminaGUILE, ". ", "PLAYER E. HONDA = ", staminaEHONDA)

# NOW, CODE THE LOGIC TO RUN ROUND 2:
print("ROUND TWO. FIGHT!")
print("PLAYER GUILE = ", staminaGUILE, ". PLAYER E. HONDA = ", staminaEHONDA)
print("PLAYER GUILE. ENTER YOUR INPUT: ")
print("PLAYER GUILE ENTERED ", guileMove)
print(guileName, " = ", guileDamage, "DAMAGE")
staminaEHONDA = staminaEHONDA - guileDamage
print("PLAYER GUILE = ", staminaGUILE, ". ", "PLAYER E. HONDA = ", staminaEHONDA)
print("PLAYER E. HONDA. ENTER YOUR INPUT: ")
print("PLAYER E. HONDA ENTERED ", ehondaMove)
print(ehondaName, " = ", ehondaDamage, "DAMAGE")
staminaGUILE = staminaGUILE - ehondaDamage
if staminaGUILE <= 0:
  staminaGUILE = 0
elif staminaEHONDA <= 0:
  staminaEHONDA = 0
else: 
  staminaGUILE = staminaGUILE
  staminaEHONDA = staminaEHONDA
print("PLAYER GUILE = ", staminaGUILE, ". ", "PLAYER E. HONDA = ", staminaEHONDA)

# FINALLY, CODE THE LOGIC TO SHOW THE WINNER, or print "IT'S A TIE!"
if staminaGUILE > staminaEHONDA:
  print("PLAYER GUILE WINS!")
elif staminaGUILE < staminaEHONDA:
  print("PLAYER E. HONDA WINS!")
else:
  print("IT'S A TIE!")
