__author__ = 'Man Parvesh'
import random

hangSteps = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def randomWord(words):
    index = random.randint(0, len(words) - 1)
    return words[index]


def board(hangSteps, missed, correct, secret):
    print hangSteps[len(missed)]
    print()

    print "Missed letters:",
    for letter in missed:
        print letter,
    print()

    blanks = '_' * len(secret)

    for i in xrange(len(secret)):
        if secret[i] in correct:
            blanks = blanks[:i] + secret[i] + blanks[i + 1:]

    for letter in blanks:
        print letter,
    print()


def getGuesses(guessed):
    while True:
        print "Guess a letter!"
        guess = raw_input().lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = randomWord(words)
gameIsDone = False

while True:
    board(hangSteps, missedLetters, correctLetters, secretWord)

    guess = getGuesses(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # checking if all letters have been found
        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

            if foundAllLetters:
                print('Correct! The answer is "' + secretWord + '"! You win!')
                gameIsDone = True

    else:
        missedLetters += guess

    # checking if player used too many words and lost

    if len(missedLetters) == len(hangSteps) - 1:
        board(hangSteps, missedLetters, correctLetters, secretWord)

        print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and '
              + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

        gameIsDone = True

        #Ask to play again!
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone = False
            secretWord = randomWord(words)
        else:
            print("Good bye!")
            break