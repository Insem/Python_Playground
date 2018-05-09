import platform
import os

#Value for main while loop
exit_val = 0

#List for elements
rps_list = ("Rock", "Paper", "Scissors")

#Function for clearing the screen depending on system type
def clear_screen(sysver):
    if(sysver == "Windows"):
        return os.system("cls")
    else:
        return os.system("clear")

#__Main loop__
while exit_val == 0:

    #Value for player1 loop, used to exit the loop
    player1_val = 0
    
    print("Type Rock, Paper, Scissors.")

    #This loops is eliminating any further issues if user would input wrong value
    while player1_val == 0:
        player1 = input("Player 1: ")

        if(player1 not in rps_list):
            print("Incorrect value. Use Rock, Paper or Scissors")
        else:
            #Exit player2 loop
            player1_val = 1
            #Clearing the screen, so player 2 is unable to peek
            clear_screen(platform.system())
    
    #Value for player2 loop, used to exit the loop
    player2_val = 0

    print("Type Rock, Paper, Scissors.")

    #This loops is eliminating any further issues if user would input wrong value
    while player2_val == 0:
        player2 = input("Player 2: ")

        if(player2 not in rps_list):
            print("Incorrect value. Use Rock, Paper or Scissors")
        else:
            #Exit player2 loop
            player2_val = 1
    
    # Since the whole logic of Rock, Paper, Scissors is resambling the triangle
    # I used index numbers insted. To minimalize the error, it is checking which
    # player choose the biggest value, and is setting it as the main
    if(rps_list.index(player1) > rps_list.index(player2)):
        sum_test = rps_list.index(player1) - rps_list.index(player2)
        display1 = "Player 1"
        display2 = "Player 2"

    else:
        sum_test = rps_list.index(player2) - rps_list.index(player1)
        display1 = "Player 2"
        display2 = "Player 1"
    
    # This part is testing the resault of previous equasion.
    # Since the values for a Rock, Paper and Scissors are:
    # 0, 1, 2
    # If Player 1 picks ROCK
    # Player 2 picks SCISSORS
    # SCISSORS has the biggest value.
    # This configuration will alwayes yeld value 2
    # Which means Defeat for the player picking ROCK
    # If value = 0 it means that both players picked the same
    # There is no much options left, value 1 means that other
    # Player won
    if(sum_test == 2):
            print("\n## "+display2+" WINS! ##\n")
    elif(sum_test == 0):
            print("\n## DRAW ##\n")
    else:
            print("\n## "+display1+" WINS! ##\n")

    exit_int = input("Want another round? (Y/N): ")

    # Checks if user want to continue. 
    # Case insensitive
    if(exit_int.lower() in ("y", "yes")):
        # If yes, clears screen and goes back to beggining
        clear_screen(platform.system())
        continue
    else:
        # If not, changing the value end the loop
        exit_val = 1
