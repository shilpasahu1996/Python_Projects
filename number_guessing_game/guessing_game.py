import random

print("You have maximum 7 chances to guess!")
low = int(input('Enter Lower Bound:'))
high = int(input('Enter Upper Bound:'))

ch = 7
counter = 0
num = random.randint(low,high)
print(f'Guess the number between {low} and {high}!')

while counter<ch:
    counter+=1
    guess = int(input(f'Guess the number between {low} and {high} '))
    if num == guess:
        print(f'Correct! The number is {num}. You guessed it in {counter} attempts.')
        break
    elif guess > num:
        print('Too high! Try a lower number.')
    elif guess < num:
        print('Too low! Try a higher number.')

if counter >= ch and guess != num:
    print(f'Sorry! The number was {num}. Better luck next time.')






