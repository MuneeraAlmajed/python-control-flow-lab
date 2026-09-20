# Exercise 0
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print('Python is fun!')

print_greeting()

# Exercise 1

def check_letter():
    letter = input('Enter a letter: ')

    if letter.lower() in 'aeiou':
        print(f'The letter {letter} is a vowel')
    else:
        print(f'The letter {letter} is a consonant')

check_letter()

# Exercise 2

def check_voting_eligibility():
    age = int(input('Please enter your age: '))
    voting_age = 18

    if age < 0:
        print('Invalid age')
    elif age >= voting_age:
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')

check_voting_eligibility()