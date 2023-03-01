gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


q1 = int(input('''Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
    
    Write your answer: '''))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input')


q2 = int(input('''Q2) When I'm dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
    
    Write your answer: '''))

if q2 == 1:
    hufflepuff += 1
elif q2 == 2:
    slytherin += 1
elif q2 == 3:
    ravenclaw += 1
elif q2 == 4:
    gryffindor += 1
else:
    print('Wrong input')


q3 = int(input('''Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
    
    Write your answer: '''))

if q3 == 1:
    slytherin += 1
elif q3 == 2:
    hufflepuff += 1
elif q3 == 3:
    ravenclaw += 1
elif q3 == 4:
    gryffindor += 1
else:
    print('Wrong input')



if gryffindor == 3:
    print('Congrats! You\'re in Gryffindor')
elif ravenclaw == 3:
    print('Congrats! You\'re in Ravenclaw')
elif hufflepuff == 3:
    print('Congrats! You\'re in Hufflepuff')
elif slytherin == 3:
    print('Congrats! You\'re in Slytherin')
else:
    print('I\'m confused. You need to take the test again.')