from tkinter import *

import time

import random



number = random.randint(1,10)

print(number)

root = 0

p1num = 0

p2num = 0

p1maxguesses = 0

p2maxguesses = 0

p1guesses = 0

p2guesses = 0

p1entry = 0

p2entry = 0

p1entrylist = list()

p2entrylist = list()



def gamesetup():

    global p1maxguesses

    global p2maxguesses

    print('How many guesses should Player 1 have?')

    p1maxguesses = int(input())

    print('How many guesses should Player 2 have?')

    p2maxguesses = int(input())



    print('Setup Complete. Game starting...')

    createwindow()

    

def createwindow():

    global root

    global p1entry

    global p2entry

    root = Tk()

    root.title('Guessing Game')

    p1label = Label(root, text = 'P1 Guess')

    p1label.pack()

    p1entry = Entry(root)

    p1entry.pack()

    p1enter = Button(root, text='Guess!', command = p1go)

    p1enter.pack()



    p2label = Label(root, text = 'P2 Guess')

    p2label.pack()

    p2entry = Entry(root)

    p2entry.pack()

    p2enter = Button(root, text='Guess!', command = p2go)

    p2enter.pack()



    setuplabel = Label(root, text='Setup the game in the CMD')

    setuplabel.pack()

    root.geometry('500x500')



def p2go():

    global p2guesses

    global p2maxguesses

    global p2num

    global number

    global p2entrylist

    

    print('P2 Guess: ')

    p2num = int(p2entry.get())

    if p2num == number:

        print('Player 2 guessed the correct number. They have WON')

        print('Player 2 guessed: '+str(p1entrylist))



        time.sleep(3)

        exit()

    else:

        print('Player 2 guessed the wrong number. Player 1 turn')

        if p2num > number:

            print('That number is too high')

        else:

            print('That number is too low')

        p2guesses = p2guesses+1

        p2entrylist.append(p2num)

        print('Player 1 has used: '+str(p2guesses)+' out of: '+str(p2maxguesses)+' guesses')



        if p2guesses > p2maxguesses:

            print('Player 1 has WON. Player 2 ran out of guesses')

            time.sleep(3)

            exit()

        else:

            pass

        

        

def p1go():

    global p1guesses

    global p1maxguesses

    global p1num

    global number

    global p1entrylist

    

    print('P1 Guess: ')

    p1num = int(p1entry.get())

    if p1num == number:

        print('Player 1 guessed the correct number. They have WON')

        print('Player 1 guessed: '+str(p1entrylist))

        time.sleep(3)

        exit()

    else:

        print('Player 1 guessed the wrong number. Player 2 turn')

        if p1num > number:

            print('That number is too high')

        else:

            print('That number is too low')

        p1guesses = p1guesses + 1

        p1entrylist.append(p1num)

        print('Player 1 has used: '+str(p1guesses)+' out of: '+str(p1maxguesses)+' guesses')

        if p1guesses > p1maxguesses:

            print('Player 2 has WON. Player 1 ran out of guesses')

            time.sleep(3)

            exit()

        else:

            pass

        



def startgame():

    gamesetup()



gamesetup()        

root.mainloop()
