from time import sleep

# Introduction

sleep(1)
print("Welkom bij de module 1 opdracht Hello You van de opleiding Software Developer aan het Mediacollege Amsterdam")

sleep(2)
print("De opdracht was om een textbased applicatie te maken met Python.")
sleep(2)
print("Dit moest doormiddel van een zelfverzonnen verhaal of een verhaal gebaseerd op waargebeurde verhalen.")
sleep(2)
print("In deze opdracht is er een verhaal gemaakt die gebaseerd is op ervaringen van vluchtelingen uit Oekraïne.")

sleep(2)
print("Wilt u het verhaal volgen?")
volgverhaal = input("Voer in y of n ")

if volgverhaal == "y" or volgverhaal == "Y" or volgverhaal == "ja" or volgverhaal == "Ja" or volgverhaal == "JA":
    print("Hier volgt her verhaal")
else: 
    print("Bedankt voor uw aandacht, tot ziens!")