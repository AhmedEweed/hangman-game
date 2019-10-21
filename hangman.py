# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lets = []
    for letter in list(secretWord):
        if letter not in lettersGuessed:
            return False
        else:
            lets.append(letter)
    if len(lets) == len(secretWord):
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = []
    for i in range(len(list(secretWord))):
        if secretWord[i] in lettersGuessed:
            word.insert(i, secretWord[i])
        else:
            word.insert(i, '*')
    return ''.join(word)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = string.ascii_lowercase
    availableLetters = []
    usedLetters = []
    for i in range(len(allLetters)):
        if allLetters[i]not in lettersGuessed:
            availableLetters.insert(i, allLetters[i])
        else:
            usedLetters.insert(i, allLetters[i])
    return sorted(''.join(availableLetters))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #print(secretWord)
    # FILL IN YOUR CODE HERE...
    guessedLetters = []
    wrongGussed = []

    print("Hello to The Hangman Game!")
    print("Our secret word is", len(secretWord), "letters long!")
    print("You should enter a letter per guess.")
    
    while len(wrongGussed) < 8 and isWordGuessed(secretWord, lettersGuessed=guessedLetters) == False:
      guess = str(input("Enter a guess letter: ")).lower()
      if len(guess) == 1:
        if guess in guessedLetters or guess in wrongGussed:
            print("You guessed that letter before! Try another one.")
            print("Now the word looks like", getGuessedWord(secretWord=secretWord, lettersGuessed=guessedLetters))

        elif guess in list(secretWord):
          guessedLetters.append(guess)
          if isWordGuessed(secretWord, guessedLetters):
            break
          else:
            print("You got that right!")
            print("Now the word looks like", getGuessedWord(secretWord=secretWord, lettersGuessed=guessedLetters))
            print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
        else:
          wrongGussed.append(guess)
          if len(wrongGussed) == 8:
            break
          
          elif len(wrongGussed) == 7:
            print("Opps! you got that wrong.")
            print("Remember! you still have", str(8-len(wrongGussed)), "guess left!")
            print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
            print("Now the word looks like", getGuessedWord(secretWord=secretWord, lettersGuessed=guessedLetters))

          
          else:
            print("Opps! you got that wrong.")
            print("Remember! you still have", str(8-len(wrongGussed)), "guesses left!")
            print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
            print("Now the word looks like", getGuessedWord(secretWord=secretWord, lettersGuessed=guessedLetters))


      else:
        print("You should enter 1 letter per guess!")
    
    
    if isWordGuessed(secretWord, guessedLetters):
      print("Whoa! you got the whole word right. Our secret word was", secretWord)
    elif len(wrongGussed) >= 8:
      print("Sorry! you ran out of guesses")
      print('Our secret word was', secretWord)
  

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
