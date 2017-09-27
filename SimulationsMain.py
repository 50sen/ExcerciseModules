import Simulations.Fridge_Simulator
import Simulations.Hangman_Simulator
import sys

while(True):
    access_or_no = input("Do you wanna access fridge stocks (Yes/No)?")
    if (access_or_no=="Yes"):
        if Simulations.Hangman_Simulator.hangman_simulator() == True:
            Simulations.Fridge_Simulator.fridge()
        else:
            print("Wrong answer!!!")
    else:
        sys.exit()

