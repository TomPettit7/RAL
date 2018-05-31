import random



guesses = 0

number = random.randint(1,10)

compchoice = random.randint(1,3)

randomnum  = random.randint(1,6)

correct = False

cave1 = False

cave2 = False

cave3 = False



def guessnumbergame():

    global guesses

    global number

    global cave1

    print('Guess a number: ')

    guess = str(input())



    if int(guess) == int(number):

        print('You guessed the correct number. You can now leave the cave')

        cave1 = True



        cavechoice()

    else:

        print('That is the wrong number')

        guesses = guesses + 1

        print('You have used '+str(guesses)+' out of 5 guesses')

        if int(guess) > int(number):

            print('Your guess is too high')

        else:

            print('Your guess is too low')

        if guesses > 5:

            print('You have failed.')

            gameover()

        else:

            guessnumbergame()#



def rockpaperscissors():#

    global cave2

    global compchoice

    rock = 1

    paper = 2

    scissors = 3

    print('This is rock paper scissors')

    choice = input('Enter the choice you want. Rock = 1, Paper = 2, Scissors = 3')



    if str(choice) == '1' and str(compchoice) == '1':

        print('You drew, you both chose rock. You have to go again')

        rockpaperscissors()

    elif str(choice) == '1' and str(compchoice) == '2':

        print('You lost, the dragon chose paper. The dragon will now eat you')

        gameover()

    elif str(choice) == '1' and str(compchoice) == '3':

        print('You won, the dragon chose scissors. You can now leave the cave')

        cave2 = True

        cavechoice()

    elif str(choice) == '2' and str(compchoice) == '1':

        print('You won, the dragon chose rock. You can now leave the cave')

        cave2 = True

        cavechoice()

    elif str(choice) == '2' and str(compchoice) == '2':

        print('You drew, you both chose paper. You have to go again')

        rockpaperscissors()

    elif str(choice) == '2' and str(compchoice) == '3':

        print('You lost, the dragon chose scissors. The dragon will now eat you')

        gameover()

    elif str(choice) == '3' and str(compchoice) == '1':

        print('You lost, the dragon chose rock. The dragon will now eat you')

        gameover()

    elif str(choice) == '3' and str(compchoice) == '2':

        print('You won, the dragon chose paper. You can now leave the cave')

        cave2 = True

        cavechoice()

    elif str(choice) == '3' and str(compchoice) == '3':

        print('You drew, you both chose scissors. You have to go again')

        rockpaperscissors()



def anagramgame():

    global cave3

    global randomnum

    global correct

    anagrams = {1: 'elhlo', 2: 'lwcmeoe', 3: 'odngra', 4: 'lyprae', 5:'ecva', 6:'ssiorscs'}

    anagramchoice = anagrams[randomnum]



    print('The dragon has chosen an anagram')

    print('Time to guess the anagram')

    print(anagramchoice)

    text =str(input('What is your guess? '))

    for letters in text:

        for symbols in anagramchoice:

            if letters == symbols:

                correct = True

            else:

                correct = False

    if correct == True:

        print('That is correct')

        cave3 = True

        cavechoice()

    else:

        print('That is wrong')

        gameover()



            

    







def cavechoice():

    global cave1

    global cave2

    global cave3

    

    print('Choose a cave to enter')

    cavenum = str(input())

    if cavenum == '1' and cave1 == False:

        guessnumbergame()



    elif cavenum == '2' and cave2 == False:

        rockpaperscissors()   

    elif cavenum == '3' and cave3 == False:

        anagramgame()

    else:

        print('You have already been in that cave')

        cavechoice()





def welcome():

    print('Welcome to this adventure game')

    print('Choose a number between 1 and 5. This will be the cave you enter')

    print('If you fail the challenge in a cave, you will be eaten by the dragon. Good luck...')

    cavechoice()



def gameover():

    print('The dragon ate you. Goodbye....')

    exit()





welcome()
