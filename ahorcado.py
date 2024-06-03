import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
    '''
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


def getRandomWord(wordList):
  wordIndex = random.randint(0, len(wordList) - 1)
  return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
  print(HANGMANPICS[len(missedLetters)])
  print()
  print('Missed letters:', end=' ')

  for letter in missedLetters:
    print(letter, end=' ')

  print()

  blanks = '_' * len(secretWord)
  for i in range(len(secretWord)):
    if secretWord[i] in correctLetters:
      blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

  for letter in blanks:
    print(letter, end=' ')

  print()

def getGuess(alreadyGuessed):
  while True:
    print('Choose a letter')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print('Please enter a single letter')
    elif guess in alreadyGuessed:
      print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz' :
      print('Please enter a LETTER')
    else:
      clear_screen()
      time.sleep(0.1)
      return guess


def playAgain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')
  

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar pear coyote crow deer dog donkey duck eagle ferret fox frog goat'
wordList = words.split() 
secretWord = getRandomWord(wordList) 

gameIsDone = False
attemptCounter = 0
maxAttempts = len(HANGMANPICS) - 1

while True:
  displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
  guess = getGuess(missedLetters + correctLetters)
  if guess in secretWord:
    correctLetters += guess
    foundAllLetters = True
    for letter in secretWord:
      if letter not in correctLetters:
        foundAllLetters = False
        break
    if foundAllLetters:
      print('Yes! The secret word is "' + secretWord + '"! You have won!')
      gameIsDone = True
      
  else:
    missedLetters += guess
    attemptCounter += 1
    print('Sorry, that letter is not in the word.')
    
  if len(missedLetters) == len(HANGMANPICS) - 1:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
    gameIsDone = True


  if gameIsDone:
    if playAgain():
      missedLetters = ''
      correctLetters = ''
      secretWord = getRandomWord(wordList)
      gameIsDone = False
      attemptCounter = 0
    else:
      break
