#!/usr/bin/python3
def multiple_returns(sentence):
    ''' Functions to print the first item and
        total lenght of the tuple
    '''
    if sentence == '':
        return (0, None)

    return(len(sentence), sentence[0])
