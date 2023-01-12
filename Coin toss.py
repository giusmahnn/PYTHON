import random  # import a random module
coin = ['heads', 'tails'] # a list is used to single them out
toss = random.choice(coin) # a random.choice allows python to choose a head or tail at random
guess = input('Pick a side, head or tail?\n') # the guess is defined

# this contains the main code of the games using while and if statements.
while guess not in coin:  
    print('Guess the coin toss!')
    guess = input('head or tail: ')
if toss == guess:
    print('oshey!!')
else:
    print('nahh, try again')
    guess = input('You can do it, pick a side')
if toss == guess:
    print('win')
else:
    print('you are a failure!')