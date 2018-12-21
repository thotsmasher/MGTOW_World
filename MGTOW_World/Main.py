import time
import os
import sqlite3
# from Alpha import Alpha
# from Beta import Beta
# from Court import Court
from Girl import Girl
# from Government import Government
from Guy import Guy
from Alpha import Alpha
from Beta import Beta
# from Hag import Hag
# from Kech import Kech
# from Single_Mother import Single_Mother
# from Unicorn import Unicorn
# from Wall import Wall
def lost():
    lost = bool(1)
    return lost

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def print_slow(str):
    for letter in str:
        print(letter, end='')
        time.sleep(.09)

# def switch_demo(argument):
#     switcher = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#     print (switcher.get(argument, "Invalid month"))

def main():
    print_slow("Welcome to MGTOW_World!""\n")
    time.sleep(1)
    #clear_screen()
    game_process = bool(0)
    # Main_Menu to give players the option to play or quit.
    while True:
        try:
            if game_process == bool(1):
                break
            choice_1 = int(input("\n""MENU:""\n""\n""[1]: Play""\n""[2]: Quit""\n"))
            if choice_1 == 1:
                print_slow("\n""Excellent... let's begin, shall we?""\n")
                game_process = bool(1)
                break
            elif choice_1 == 2:
                print_slow("\n""Goodbye... until the next time we meet again...""\n")
                quit()
            else:
                print_slow("\n""Invalid option, please try again.""\n")
        except ValueError:
            print_slow("\n""Invalid option, please try again.""\n")
    #print_slow("Choose wisely....")
    while True:
        try:
            choice_2 = int(input("\n""Options:""\n""\n""[1]: New game""\n""[2]: Load game""\n"))
            red_pill_knowledge = 0
            if choice_2 == 2:
                character = Beta
            #   <database sql code> <Create character with attributes loaded from database>
            #   break
            print_slow("Choose wisely....""\n")
            choice_3 = int(input("\n""Options:""\n""\n""[1]: Blue_pill""\n""[2]: Purple_pill""\n""[3]: Red_pill""\n"))
            if choice_3 == 1:
                print_slow("\n""You have chosen the blue_pill...""\n""Choose your character:""\n")
                choice_4 = int(input("\n""Options:""\n""\n""[1]: Ertugrul""\n""[2]: Soufian""\n""[3]: Kanye West""\n"))
                if choice_4 == 1:
                    character = Beta("Ertugrul",25,bool(1),"Arabian",85,180,bool(0),0,1200,0,"Service_desk Employee","MBO_Niveau_4_ICT")
                    print_slow("You have selected " + character.name +  " as your blue pill beta cuck main character...")
            elif choice_3 == 2:
                if red_pill_knowledge >= 50:
                    print_slow("\n""You have chosen the purple_pill...""\n""Choose your character:""\n")
                    choice_5 = int(input("\n""Options:""\n""\n""[1]: Owen Cook (Tyler)""\n""[2]: BoBo (The Ultimate Seat Pedophile Girl Destroyer)""\n""[3]: Jordan Peterson""\n"))
                    if choice_5 == 1:
                        character = Guy("Owen Cook",30,bool(0),"Caucasian",75,170,bool(0),100,3000,60,"Pick up Artist",None)
                        print_slow("You have selected " + character.name +  " as your purple pill main character...")
                else:
                    print_slow("It seems that you don't have enough red pill knowledge yet to select the purple pill...""\n""Please try again...""\n")
        except ValueError:
            print_slow("Wrong Value")

            # elif choice_3 == 2:
            #     if b.purple_pill == bool(1):
            #         print_slow("You have chosen the purple_pill...")






    # While loop to start MGTOW_World
    # Choose red/blue pill < Red pill is locked, needs to get achieved during game_play. Same with Purple_pill
    # if blue_pill:
        # ask questions regarding attributes
        # create instance Beta(Guy)
    # if red_pill:
        # ask questions regarding attributes
        # create instance Alpha(Guy)
    # if purple_pill:
        # ask questions regarding attributes
        # create instance Guy
    # Create database for saving progress

    # Losing the game: Receiving aids = close MGTOW_World, divorce_rape = close MGTOW_world
    # Winning the game: Get 7 figures income, have multiple girls you can fuck,

    # x = Girl("Ditsy",29,bool(0),1000,"A","caucasian",60,160,1000,None,["Bachelor Gender Studies", "Bachelor of Law Enforcement Studies"])
    # y = Girl("Test",18,bool(1),0,"DD","African",50,150,2000,None,"Bachelor Gender Studies")
    # swinger = Girl("Ditsy",35,bool(0),1000,"A","caucasian",60,160,1000,None,["Bachelor Gender Studies", "Bachelor of Law Enforcement Studies"])
    # x.fuck_chad("Tyrone",4)
    # print (x.diploma)
    # print (x.breast_cup)
    # print (x.hotness)
    # print (y.diploma)
    # print (x.cock_mileage)
    # print (x.SMV)
    # print (y.SMV)

    #print (x.depth)
    #print (y.depth)
    # b = Beta("Ertugrul",25,bool(1),"Arabian",85,180,bool(0),0,1200,"Service_desk Employee","MBO_Niveau_4_ICT")
    # z = Alpha("Tyrone",25,bool(0),"African",80,190,bool(1),1000,1000,"Drugs Dealer",None)
    #swinger.fuck_chad(b,10)
    # x.fuck_chad(b,10)
    # x.fuck_chad(y,10)
    # x.fuck_chad(z,10)

if __name__ == '__main__':
    while True:
        if lost == bool(1):
            quit()
        else:
            main()
