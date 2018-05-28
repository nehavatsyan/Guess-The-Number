import random
secretNumber=random.randint(1,10)
guess=0
i=0
while guess!=secretNumber:
        i=i+1
        print("Take a guess")
        guess=int(input())
        if guess < secretNumber:
                   print('Your guess is too low.')
        elif guess > secretNumber:
                   print('Your guess is too high.')
        
print('Good job! You guessed my number in ' ,i, ' guesses!')
