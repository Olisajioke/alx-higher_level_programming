#!/usr/bin/python3
def multiple_returns(sentence):
    ''' Functions to print the first item and
        total lenght of the tuple
    '''
    if sentence == '':
        return (None)

    first_char = sentence[0]
    lenght = len(sentence)
    return(lenght, first_char)
