import random, string

WORDLIST_FILENAME = "UnitedStates.txt"


def core_logic(wrongGussed, secretState, guessedLetters):
  while len(wrongGussed) < 8 and isWordGuessed(secretState, guessedLetters) == False:
    guess = str(input("Enter a guess letter: ")).lower()
    if len(guess) == 1:
      if guess in guessedLetters or guess in wrongGussed:
        print("You guessed that letter before! Try another one.")
        print("Now the word looks like", getGuessedWord(secretWord=secretState, lettersGuessed=guessedLetters))

      elif guess in list(secretState):
        guessedLetters.append(guess)
        if isWordGuessed(secretState, guessedLetters):
          break
        else:
          print("You got that right!")
          print("Now the word looks like", getGuessedWord(secretWord=secretState, lettersGuessed=guessedLetters))
          print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
      else:
        wrongGussed.append(guess)
        if len(wrongGussed) == 8:
          break
              
        elif len(wrongGussed) == 7:
          print("Opps! you got that wrong.")
          print("Remember! you still have", str(8-len(wrongGussed)), "guess left!")
          print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
          print("Now the word looks like", getGuessedWord(secretWord=secretState, lettersGuessed=guessedLetters))

              
        else:
          print("Opps! you got that wrong.")
          print("Remember! you still have", str(8-len(wrongGussed)), "guesses left!")
          print("You still have letters", getAvailableLetters((guessedLetters+wrongGussed)), "to guess from!")
          print("Now the word looks like", getGuessedWord(secretWord=secretState, lettersGuessed=guessedLetters))


    else:
      print("You should enter 1 letter per guess!")

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

def gameStart(secretWord):
        print("Hello to Guess state name Game!")
        print("Our secret state name is", len(secretWord), "letters long!")
        print("You should enter a letter per guess.")

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
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
    allLetters = string.ascii_lowercase
    availableLetters = []
    usedLetters = []
    for i in range(len(allLetters)):
        if allLetters[i]not in lettersGuessed:
            availableLetters.insert(i, allLetters[i])
        else:
            usedLetters.insert(i, allLetters[i])
    return sorted(''.join(availableLetters))

def stateGame():
    '''
    secretState: string, the secret word to guess.
    '''
    while True:
      secretState = chooseWord(wordlist).lower()
      guessedLetters = []
      wrongGussed = []
      gameStart(secretState)
      core_logic(wrongGussed, secretState, guessedLetters)
      
      
      if isWordGuessed(secretState, guessedLetters):
        print("Whoa! you got the whole state name right. Our state name was", str(secretState).capitalize())
        res = str(input("Would you like to play again? [y]/n: ").lower())
        if res == 'y' or res == 'yes':
          True
        elif res == 'n' or res == 'no':
          print("Good bye!")
          break
        else:
          print("I will take this as a No! Good bye!")
          break

      elif len(wrongGussed) >= 8:
        print("Sorry! you ran out of guesses")
        print('Our state name was', str(secretState).capitalize())
        res = str(input("Would you like to play again? [y]/n: ").lower())
        if res == 'y' or res == 'yes':
          True
        elif res == 'n' or res == 'no':
          print("Good bye!")
          break
        else:
          print("I will take this as a No! Good bye!")
          break

wordlist = loadWords()
stateGame()