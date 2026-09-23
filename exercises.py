# Exercise 0
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print('Python is fun!')

print_greeting()

# Exercise 1

def check_letter():
    letter = input('Enter a letter: ')
    
    if letter.isalpha():
        if letter.lower() in 'aeiou':
            print(f'The letter {letter} is a vowel')
        else:
            print(f'The letter {letter} is a consonant')
    else:
        print('That is not a letter')

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

# Exercise 3

def calculate_dog_years():
    age = int(input("Input a dog's age: "))

    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}")

calculate_dog_years()

# Exercise 4

def weather_advice():
    cold = input('Is it cold ? (yes/no): ')
    raining = input("Is it raining? (yes/no): ")

    if cold == 'yes' and raining == 'yes':
        print('Wear a waterproof coar')
    elif cold == 'yes' and raining == 'no':
        print('Wear a warm coat')
    elif cold == 'no' and raining == 'yes':
        print('Carry an umbrella')
    elif cold == 'no' and raining == 'no':
        print('Wear light clothing')
    else:
        print('Invalid Input')

weather_advice()

# Exercise 5

def determine_season():
    month = input('Enter the month of the year (Jan - Dec): ')
    day = int(input('Enter the day of the month: '))
    
    if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print('Invalid month')
    elif day < 1 or day > 31:
        print('Invalid day')
    elif month in ['Dec', 'Jan', 'Feb'] or (month == 'Mar' and day <=19):
        season = 'Winter'
    elif month in ['Mar','Apr','May'] or (month == 'Jun' and day <=20):
        season = 'Spring'
    elif month in ['Jun', 'Jul' , 'Aug'] or (month == 'Sep' and day <=21):
        season = 'Summer'
    else:
        season = 'Fall'

    print(f'{month} {day} is in {season}')

determine_season()

# Exercise 6

def guess_number(): 
    target = 42

    for attempt in range(1,6):
        guess= int(input('Guess a number between 1 and 100: '))

        if guess == target:
            print('Congratulation, you guessed correctly')
            break
        if attempt == 5:
            print('Last chance')

        if guess < target:
            print('Guess is too low')
        elif guess > target: 
            print('Guess is too high')

    if guess != target: 
        print('Sorry, you failed to guess the number in five attempts')


guess_number()