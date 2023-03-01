pH = float(input('Give a number between 1 and 14 to know the pH: '))

if pH > 7:
  print('Basic')
elif pH < 7:
  print('Acidic')
else:
  print('Neutral')