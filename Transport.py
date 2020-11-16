import os
import time

os.system('cls')

factory = ["pc"]
distribution = []
shop = []

def factory_to_distribution():
    distribution.append(factory.pop())



def distribution_to_shop():
    shop.extend(distribution)
    distribution.pop(0)

def printlist():
        print("factory = " + str(factory))
        print("distribution = "+ str(distribution))
        print("shop = "+ str(shop))

def nextprint():
    time.sleep(2.1)
    os.system('cls')

printlist()
factory_to_distribution()
nextprint()
printlist()
distribution_to_shop()
nextprint()
printlist()

time.sleep(1)

def AA():
    tryagain=input("try again? Y/N ")
    if (tryagain == "Y"):
        os.system('Transport.py')
    elif (tryagain == "N"):
        print ("gemaakt door Thijn.")
    else:
        print(tryagain, " is geen geldig antwoord")

AA()
