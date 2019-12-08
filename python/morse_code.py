#!/usr/bin/env python3
# updated : 15-01-2019

import re
import sys

morseAlphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "   ",
        "0" : "-----",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",

        }


def CodeWithMorse(message):
    '''
    encode  message into morse code.
    words are seperated by three spaces
    letters are seperated by one space
    '''

    # return value
    n_msg = "" 

    try: 
        for i in message:
            n_msg += morseAlphabet[i.upper()] + ' '

        return n_msg 

    except KeyError:
        print('only alphabet character and numbers are allowed !!!')


def DecodeWithMorse(message):
    '''
    decode message with morse code
    '''

    # return value
    d_msg = ''

    # split message into words (list)
    # excpet words to be seperated by three space in message
    words_list = re.split(r'\s\s\s', message, flags=0)

    # split words into letters (list)
    letters_list = [re.split(r'\s', word, flags=0) for word in words_list ] 

    #change each letter with the MorseCode from the dict above
    for word in letters_list:
        for letter in word:
            for key in morseAlphabet:
                if morseAlphabet[key] == letter:
                    letters_list[letters_list.index(word)][word.index(letter)] = key   

    # construct the d_msg
    for word in letters_list:
        for letter in word:
            d_msg += letter
        d_msg += ' '

    return d_msg


if __name__=="__main__":

    usage = "usage : python3 morse_code.py -e this is message to encode"
    usage += '\nusage : python3 morse_code.py -d this is message to decode'

    if len(sys.argv) == 2 and sys.argv in ('-h', '--help'):
        print(usage)
        exit()

    if len(sys.argv) >= 3 :
        option = sys.argv[1]
        message = sys.argv[2:]

        if option not in ('-e', '-d'):
            print(usage)
            exit()

        if option == '-e':
            message = ' '.join(message)
            print("original message : {}\nencoded message : {}".format(message, CodeWithMorse(message)))
        else:
            message = ' '.join(message)
            print("original message : {}\ndecoded message : {}".format(message, DecodeWithMorse(message).lower()))

    else :
        print(usage)
        exit()

