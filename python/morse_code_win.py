

#global variable
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

import re
import argparse
import winsound
import time
import sys

#function to change the message into morse code
def CodeWithMorse(message):
    CodedMesssage = ""

    try:
        #change the letter to upper case and change them with those in dict above  
        for i in message:
            CodedMesssage += morseAlphabet[i.upper()]+' '
        return CodedMesssage

    except KeyError:

        print("don\'t include any carectere only numbers and letters!")
        sys.exit()



#this fonction decode your meassage
def DecodeWithMorse(message):
    dmsg = ''
    #spliting the words & putting them inside list ( three spaces as mention above )
    splitedMessage = re.split(r'\s\s\s', message, flags=0)

    #split the words into letter ( one space as mention above ) 
    letterlist = [re.split(r'\s', word, flags=0) for word in splitedMessage ]          #split the message to letter

    #change each letter with the MorseCode from the dict above
    for word in letterlist:
        for letter in word:
            for key in morseAlphabet:
                if morseAlphabet[key] == letter:
                    letterlist[letterlist.index(word)][word.index(letter)] = key   
    #getting the decodedmessage
    for word in letterlist:
        for letter in word:
            dmsg += letter
        dmsg += ' '
    return dmsg

def beepMorse(msg):
    # funtion to make beep sound with morse code
    for letter in msg :
        if letter == '.':
            winsound.Beep(1000, 400)
        if letter == '-':
            winsound.Beep(1000, 800)
        if letter == ' ':
            # the frequency is very low , it's very silent.
            # winsound.Beep(37, 100)
            time.sleep(1)
        if letter == "   ":
            time.sleep(1.5)

if __name__=="__main__":


    while True :
        try :
            choice = int(input('Do you want to enocde[1] or decode[2] or exit[3] :'))
        except:
            print("invalid number")

        if choice == 1 :
            msg = input("type your message : ")
            codedMsg = CodeWithMorse(msg)
            print('Your message :')
            print(codedMsg)

            print('\nlisten ... ')
            beepMorse(codedMsg)
        elif choice == 2 :
            msg = input("type your encoded message : ")
            decodedMsg = DecodeWithMorse(msg)
            print("Your message : ")
            print(decodedMsg)
        elif choice == 3 :
            sys.exit()
        else :
            print("Invalid number")

