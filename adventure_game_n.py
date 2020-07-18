import time
import random


def print_s(msg_print):
    print(msg_print)
    time.sleep(2)


def begining():
    print_s("Welcome to the wrestling circuit.")
    print_s("I'm Nura, the referee of this game.")
    print_s("I will explain for you  how to play the game.")
    print_s("There are three wrestlers: Hulk Hogan, John Cena, The Rock.")
    print_s("To win, you have to punch the wrestler "
            " with a certain number of punches.")
    print_s("For notice, the number of punches "
            " will be randomly chosen for you.")
    print_s("Are you ready? .. ")


def choose(punches):
    chos = input("\nPlease choose the wrestler number to face him: "
                 "\n1. Hulk Hogan."
                 "\n2. John Cena.\n"
                 "3. The Rock\n")
    if chos == '1':
        hulk_hogan(punches)
    elif chos == '2':
        john_cena(punches)
    elif chos == '3':
        the_rock(punches)
    else:
        choose(punches)


def hulk_hogan(punches):
    print_s("\nOh you choose the veteran Hulk Hogan,")
    print_s("If you want to defeat him, you have to punch him three punches.\n"
            "Your punches number " + punches + " !")
    if punches == '3':
        print_s("You relly strong. You have won.")
    else:
        print_s("\nDo not be sad for your loss, this's Hulk Hogan.")
    play_again(punches)


def john_cena(punches):
    print_s("You will encounter John Cena, who only "
            "needs one overwhelming punch.\n"
            "Your punches number " + punches + " !")
    if punches == '1':
        print_s("You saw that with one punch, you won.")
    else:
        print_s("\nIt looks like you need more power.")
    play_again(punches)


def the_rock(punches):
    print_s("You choose one of the Hollywood stars to face it.")
    print_s("You must hit him two focused punches to crush on this star.\n"
            "Your punches number " + punches + " !")
    if punches == '2':
        print_s("You are the star here, you won .")
    else:
        print_s("\nDo not worry, the Super Star defeated you.")
    play_again(punches)


def play_again(punches):
    again = input("\nHey hero, do you want to wrestle again? "
                  " 'yes' , 'no' \n").lower()
    if 'no' in again:
        exit(print_s("Be fine, see you soon."))
    elif 'yes' in again:
        print_s("You really are not afraid because you are a hero.")
        start_game()
    else:
        print_s("Please, enter 'yes' OR 'no'")
        play_again(punches)


def start_game():
    begining()
    punches = str(random.randint(1, 3))
    choose(punches)
    play_again(punches)


start_game()
