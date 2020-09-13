def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    a = [y for x, y in enumerate(aTup) if y % 2 != 0]
    return a

print(oddTuples((1,2,3,4,5)))