def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    answer = ''
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in lettersGuessed:
            answer += letter
    return answer


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    answer = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            answer += letter
        else:
            answer += '_'
    return answer


def hangman(secretWord):
    print('Loading word list from file...')
    # print('{} words loaded.'.format(wordlist))
    print('Welcome to the game, Hangman!\nI am thinking of a word that is {} letters long.'.format(len(secretWord)))
    letterGuessed = []
    mistakesMade = 8
    while not isWordGuessed(secretWord, letterGuessed) and mistakesMade > 0:
        print(12 * '-')
        print('You have {} guesses left.'.format(mistakesMade))
        print('Available letters: {}'.format(getAvailableLetters(letterGuessed)))
        choisee = input('Please guess a letter: ').lower()
        if choisee in letterGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letterGuessed)))
            continue
        elif choisee not in secretWord:
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, letterGuessed)))
            mistakesMade -= 1
            letterGuessed.append(choisee)
            continue
        else:
            letterGuessed.append(choisee)
            print('Good guess: {}'.format(getGuessedWord(secretWord, letterGuessed)))
    if mistakesMade == 0:
        print(12 * '-' + '\n' + 'Sorry, you ran out of guesses. The word was else.')
    else:
        print(12 * '-' + '\n' + 'Congratulations, you won!')


secretWord = 'helicopter'
hangman(secretWord)
