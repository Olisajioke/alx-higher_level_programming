#!/usr/bin/python3

def multiple_returns(sentence):
    ''' Functions to print the first item and
        total lenght
    '''
    if sentence == '':
        return (0, None)

    lenght = len(sentence)
    first_char = sentence[0]
    return(lenght, first_char)
