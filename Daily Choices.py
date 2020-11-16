#import
import time

#uitleg
print("hallo, jij gaat vandaag je dag starten vanuit mijn ogen. je moet keuzes maken beantwoord deze keuzes door 1 of 2 te typen. klik op enter om door te gaan.")

input()

time.sleep(1)

#keuze1
keuzeaa = input("je word wakker door je wekker, slaap je door tot je echt wakker moet worden (1) of ga je optijd wakker worden zodat je nog genoeg tijd heb om klaar te maken (2) ?")

time.sleep(1)

if (keuzeaa == "1"):
    print("je bent te laat om nog te kunnen ontbijten.")
elif (keuzeaa == "2"):
    print("je bent optijd en fris.")
else:
    print(keuzeaa, " is geen mogelijke keuze.")
time.sleep(1)

#keuze2
keuzeba = input("je zit in de bus ga je anime kijken (1) of ga je muziek luisteren en naar buiten kijken (2) ?")
time.sleep(1)

if (keuzeba == "1"):
    print("je bent anime aan het kijken.")
elif (keuzeba == "2"):
    print("je bent aan het viben op goede muziek.")
else:
    print(keuzeba, " is geen mogelijke keuze.")
time.sleep(1)

#keuze3
keuzeca = input("je hebt pauze op school, ga je youtube (1) of anime (2) kijken?")
time.sleep(1)

if (keuzeca == "1"):
    print("je bent anime aan het kijken.")
elif (keuzeca == "2"):
    print("je bent youtube aan het kijken.")
else:
    print(keuzeca, " is geen mogelijke keuze.")
time.sleep(1)

#keuze4
keuzeda= input("je bent klaar met je lessen ga je nu naar huis (1) of ga je nog wat huiswerk afmaken (2) ?")
time.sleep(1)

if (keuzeda == "1"):
    print("je bent naar huis gegaan maar heb nog geen huiswerk afgemaakt, dit moet dus thuis gedaan worden.")
elif (keuzeda == "2"):
    print("je hebt je huiswerk af en kan nu zonder zorgen naar huis.")
else:
    print(keuzeda, " is geen mogelijke keuze.")
time.sleep(1)

#keuze5
keuzeea= input("je bent thuis ga je gamen (1) of ga je naar de sportschool (2) ?")
time.sleep(1)

if (keuzeea == "1"):
    print("je bent nu aan het gamen en gaat vanavond nog naar de sportschool.")
elif (keuzeea == "2"):
    print("je gaat naar de sportschool, het is lekker rustig.")
else:
    print(keuzeea, " is geen mogelijke keuze.")
