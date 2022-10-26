from time import sleep

# def Start

def start():
    sleep(1)
    print("Je bent een student aan de Universiteit van Charkov in Oekraïne waar je Computer Science studeert. ")
    
    sleep(1)
    print("Je woont bij een oudere vrouw in huis waar je een hechte band mee hebt geschept.")
    
    sleep(1)
    print("Eerder in de week was op het nieuws al te horen dat de Russen Oekraïne waren binnen gevallen, je besloot om in de stad te blijven tot het niet meer kan. ")
    
    sleep(1)
    print("Tijdens het studeren achter je computer in je kamer gaan het luchtalarm af en de radio switcht naar het noodbericht: ")
    
    sleep(1)
    print("Rusland heeft de aanval gericht op de stad, de troepen zijn een paar dagen verwijdert van de stad.")
    
    sleep(1)
    print("Ga naar de schuilkelder of pak de laatste kans om te vluchten. ")
    
    sleep(1)
    print("Moldavië, Hongarije, Roemenië en Polen hebben hun grenzen open gezet voor vluchtelingen. ")
    
    sleep(1)
    print("Wees voorzichtig en God bless you all")
    
    # verandering

    

# def ending 1

def ending1():
    sleep(1)
    print("Je gaat met huisbaas mee naar haar familie, ze hebben ene kamer voor je vrij. ")
    sleep(2)
    print("Je gaat opzoek naar een baan en probeert daarnaast zelf door te studeren. ")
    sleep(2)
    print("Het enige wat je kan doen is wachten tot de oorlog voorbij is.")
    sleep(3)
    print("Je hebt een einde gevonden ")
    sleep(1)
    print("Om opnieuw te spelen herstart het programma")
    sleep(1)
    print("Bedankt voor het spelen! Tot ziens! :D ")

# def ending 2

def ending2():
    sleep(1)
    print("Je besluit om bij de buren te blijven, je krijgt een vluchtelingen verblijfvergunning.")
    sleep(2)
    print("De buren hebben een huis kunnen regelen waar jij ook een verblijfplaats krijgt.")
    sleep(2)
    print("Ook hebben ze werk waar jij ook een baantje krijgt. ")
    
    sleep(3)
    print("Je hebt een einde gevonden ")
    sleep(1)
    print("Om opnieuw te spelen herstart het programma")
    sleep(1)
    print("Bedankt voor het spelen! Tot ziens! :D ")

# def ending 3

def ending3():
    sleep(1)
    print("Je belandt op het vluchtelingen cruiseschip in Zaandam. ")
    sleep(2)
    print("Je moet wachten tot je een verblijfsvergunning krijgt. ")
    sleep(2)
    print("Tijdens het wachten probeer je mensen om je heen te helpen en je onderzoekt de omgeving van het nieuwe land waar je bent. ")
    sleep(2)
    print("Het enige wat je nu kan doen is wachten op je vergunning of tot de oorlog voorbij is.")
    
    sleep(3)
    print("Je hebt een einde gevonden ")
    sleep(1)
    print("Om opnieuw te spelen herstart het programma")
    sleep(1)
    print("Bedankt voor het spelen! Tot ziens! :D ")

# def ending 4

def ending4():
    sleep(1)
    print("Je blijft op de boerderij, je werkt daar voor onderdak en eten.")
    sleep(2)
    print("Ook probeer je zelf je studie bij te houden. ")
    sleep(2)
    print("Je wacht tot de oorlog voorbij is en de Russen weg zijn uit je stad.")
    
    sleep(3)
    print("Je hebt een einde gevonden ")
    sleep(1)
    print("Om opnieuw te spelen herstart het programma")
    sleep(1)
    print("Bedankt voor het spelen! Tot ziens! :D ")

# def ending 5

def ending5():
    sleep(1)
    print("Je besluit om in de schuilkelder te blijven tot het Russisch leger de stad heeft overgenomen en de bommen stoppen met vallen.")
    sleep(2)
    print("Je gaat weer terug naar je kamer die nog steeds staat.")
    sleep(2)
    print("Je zoekt naar werk. ")
    sleep(2)
    print("Leven gaat weer door maar met een Russische schaduw erover. ")
    sleep(2)
    print("Je wacht tot de oorlog voorbij gaat en de stad wordt bevrijdt. ")

    sleep(3)
    print("Je hebt een einde gevonden ")
    sleep(1)
    print("Om opnieuw te spelen herstart het programma")
    sleep(1)
    print("Bedankt voor het spelen! Tot ziens! :D ")

# def a1

def a1():
    sleep(1)
    print("Uit welke tas met spullen kies je?")
    sleep(2)
    print("A. De rugzak bevat: Geld, je paspoort, een waterfles en een aantal mueslirepen")
    print("B. De rugzak bevat: Geld, je paspoort, een paar pakjes sap en de overgebleven aardappelen van vorige avond")
    aa1 = input("A of B ")

# def b2

def b2():
    sleep(1)
    print("Uit welke tas met spullen kies je?")
    sleep(2)
    print("A. De rugzak bevat: Geld, je paspoort, een teddy beer en een boek ")
    print("B. De rugzak bevat: Geld, je paspoort, de handgemaakte deken van je huisbaas en een foto album ")
    ab2 = input("A. of B.")

def q3():
    sleep(1)

# Introduction

sleep(1)
print("Welkom bij de Module 1 opdracht Hello You van de opleiding Software Developer aan het Mediacollege Amsterdam")

sleep(2)
print("De opdracht was om een textbased applicatie te maken met Python.")

sleep(2)
print("Dit moest doormiddel van een zelfverzonnen verhaal of een verhaal gebaseerd op waargebeurde verhalen.")

sleep(2)
print("In deze opdracht is er een verhaal gemaakt die gebaseerd is op ervaringen van vluchtelingen uit Oekraïne.")

sleep(2)
print("Wilt u het verhaal volgen?")
volgverhaal = input("Voer in j of n ").lower()

if volgverhaal == "j" or volgverhaal == "ja":
    sleep(1)
    print("Hier volgt her verhaal")
elif volgverhaal == "n" or volgverhaal == "nee":
    sleep(1)
    print("Bedankt voor uw aandacht, tot ziens!")

# Begin verhaal
if volgverhaal == "j" or volgverhaal == "ja":
    start()
    awnser = input() # LET OP VERANDERING

if awnser == "a" or awnser == "A":
    a1()
elif awnser == "b" or awnser == "B":
    b2()   

