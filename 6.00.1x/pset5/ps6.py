import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    №>>> is_word(word_list, 'bat') returns
    True
    №>>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0 <= shift < 26, '{} is not in range(0,26)'.format(shift)
        alpha_lower = {chr(key + 97): chr(((key + shift) % 26) + 97) for key in range(26)}
        alpha_caps = {chr(key + 65): chr(((key + shift) % 26) + 65) for key in range(26)}
        alpha_lower.update(alpha_caps)
        return alpha_lower

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # TODO what about empty text?
        for letter in self.message_text:
            #print('letter={}'.format(letter))
            assert letter.isalpha() or \
                   letter.isdigit() or \
                   letter in string.punctuation or \
                   letter == ' ', '{} in text message with error'.format(letter)
        key = self.build_shift_dict(shift)
        answer = []
        for letter in self.message_text:
            if letter.isalpha():
                answer.append(key[letter])
            else:
                answer.append(letter)
        return ''.join(answer)


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.text = text
        self.shift = shift
        assert type(shift) == int, 'typeerror of shift={} is no integer, is {}'.format(shift, type(shift))
        assert 0 <= shift < 26, 'shift={} is not in valid range'.format(shift)
        self.encrypting_dict = self.build_shift_dict(self.shift)
        Message.__init__(self, self.text)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''

        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert type(shift) == int, 'type error of shift - assert intger, get - {}'.format(type(shift))
        assert 0 <= shift < 26, 'you give wrong shift={}'.format(shift)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        assert type(text) == str, 'CiphertextMessage.__init__: {}, {} is not str type'.format(text, type(text))
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)       on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        current_key_legal_words = [0, 0]
        for shift in range(0, 26):
            #print(f'shift={shift}')
            decrypted_text = self.apply_shift((26 - shift) % 26)
            clear_list = [x.strip(string.punctuation) for x in decrypted_text.split()]
            legal_words_count = 0
            for item in clear_list:
                #print(f'item={item}')
                if is_word(self.valid_words, item):
                    legal_words_count += 1
                    if current_key_legal_words[1] <= legal_words_count:
                        current_key_legal_words[0] = shift
                        current_key_legal_words[1] = legal_words_count
                        break
        return (26 - current_key_legal_words[0]) % 26, self.apply_shift((26 - current_key_legal_words[0]) % 26)


def decrypt_story():
    """
    decrypt text by using CiphertextMessage.decrypt_message function
    text: string - encrypted string from file
    return: result of  CiphertextMessage.decrypt_message() - tuple (key, decrypted text)
    """
    text = get_story_string()
    instance = CiphertextMessage(text)
    return instance.decrypt_message()


# Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

# Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
