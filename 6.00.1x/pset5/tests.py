from ps6 import *
import random
import string


# unit tests for Message class
def test_build_shift_dict():
    """
    unit test for build_shift_dict function
    instance - instance of Message class
    """
    instance = Message('123')
    shift = [0, 1, 10, random.randint(1, 25)]
    for item in shift:
        ret = instance.build_shift_dict(item)
        assert type(ret) == dict, 'build_shift_dict: {} is not a dictionary'.format(ret)
        assert len(ret.keys()) == 52, 'build_shift_dict: {} is not 52 character length'.format(ret)
        assert ''.join(ret.keys()).isalpha(), 'build_shift_dict: {} keys in this dictionary are not ' \
                                              'chars'.format(ret.keys())
    return '-' * 25 + '\ntest_build_shift_dict PASS\n' + '-' * 25


def test_apply_shift():
    """
    unit test for apply_shift() function
    instance - instance of Message class
    """
    allowed_text = string.digits + string.punctuation + string.ascii_letters
    text = ['I am a boy!', '123alpha', ''.join([allowed_text[random.randint(0, len(allowed_text) - 1)] for x
                                                in range(random.randint(1, 25))])]
    for item in text:
        shift = random.randint(0, 25)
        instance = Message(item)
        result = instance.apply_shift(shift)
        assert len(result) == len(item), 'apply_shift: lens of test text {} and result {} ' \
                                         'are different'.format(item, result)
        for letter in result:
            assert letter.isalpha() or \
                   letter.isdigit() or \
                   letter in string.punctuation or \
                   letter == ' ', 'apply_shift: {} in result message with error'.format(letter)
        print(item)
        print(result)
        print('-' * 25)
    return '-' * 25 + '\ntest_apply_shift PASS\n' + '-' * 25


print(test_build_shift_dict())
print(test_apply_shift())


# unit tests for PlaintextMessage(Message)
def test_get_shift():
    """
    unit test for get_shift() function
    instance - instance of PlaintextMessage(Message)
    """
    shift = [3, 10, 11, random.randint(1, 25)]
    text = 'test message to encrypt'

    for item in shift:
        instance = PlaintextMessage(text, item)
        result = instance.get_shift()
        assert result == item, 'get_shift: There is an error in get_shift function. {} != {}'.format(item, result)
    return '-' * 25 + '\ntest_get_shift PASS\n' + '-' * 25


def test_get_encrypting_dict():
    """
    unit test for get_encrypting_dict function
    instance - instance of PlaintextMessage(Message)
    """
    text = 'test message for encryption'
    shift = random.randint(1, 25)
    instance = PlaintextMessage(text, shift)
    result = instance.get_encrypting_dict()
    #print(result)
    assert type(result) == dict, 'get_encrypting_dict: result({}) is not dictionary'.format(type(result))
    assert result == instance.build_shift_dict(shift), 'get_encrypting_dict: dreturn dictionary and interanal are ' \
                                                       'different'

    result[list(result.keys())[5]] = 'ZZZ'  # copy control

    assert result != instance.encrypting_dict, 'get_encrypting_dict: you output is not save, ' \
                                                       'Changes in return dictionary affects internal dictionary.'
    return '-' * 25 + '\nget_encrypting_dict PASS\n' + '-' * 25

print(test_get_shift())
print(test_get_encrypting_dict())

# unit tests for CiphertextMessage(Message)

def test_decrypt_message():
    """
    unit test for decrypt_message function
    instance - instance of CiphertextMessage(Message)
    """
    text = 'some text with commas, for example!'
    shift = [random.randint(1, 24)]*10
    shift.extend([0, 25])
    #print(f'shift={shift}')
    for key in shift:
        instance = PlaintextMessage(text, key)
        encrypted_text = instance.apply_shift(key)
        instance = CiphertextMessage(encrypted_text)
        result = instance.decrypt_message()
        assert  type(result) == tuple, f'test_decrypt_message: type of return value({type(result)} is not tuple)'
        assert (26 - result[0]) % 26 == key, f'test_decrypt_message: key = {key} is not equal to decrypted {result[0]}'
        assert result[1] == text, 'test_decrypt_message: {} != {}'.format(result, text)
    return '-' * 25 + '\ndecrypt_message PASS\n' + '-' * 25


print(test_decrypt_message())