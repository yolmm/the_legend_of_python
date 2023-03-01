import random

answer = random.randrange(0, 8)

question = input('Question: ')


if answer == 1:
    print('Definitely')
elif answer == 2:
    print('It is decidedly so')
elif answer == 3:
    print('Without a doubt')
elif answer == 4:
    print('Reply hazy, try again')
elif answer == 5:
    print('Ask again later')
elif answer == 6:
    print('Better not tell you now')
elif answer == 7:
    print('My sources say no')
elif answer == 8:
    print('Outlook not so good')
else:
    print('Very doubtful')