guess = 0
tries = 0

while guess != 6 and tries < 3:
  guess = int(input("Guess the number. You have 3 tries:  "))
  tries += 1

if tries == 3 and guess != 6:
   print("Game over")
else:
   print("You got it!")