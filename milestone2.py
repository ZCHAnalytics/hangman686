import random

word_list = ['banana', 'mango', 'cherry', 'apple', 'pear']
word = random.choice(word_list)
print(word_list)
print(word)

guess = input("Enter a single letter :")
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
