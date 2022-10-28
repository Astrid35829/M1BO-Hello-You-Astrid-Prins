from time import sleep

# def intro
def intro():
    sleep(1)
    print("Welkom bij de Module 1 opdracht Hello You van de opleiding Software Developer aan het Mediacollege Amsterdam.")
    sleep(3)
    print("De opdracht was om een textbased applicatie te maken met Python.")
    sleep(3)
    print("Dit moest doormiddel van een zelfverzonnen verhaal of een verhaal gebaseerd op waargebeurde verhalen.")
    sleep(3)
    print("In deze opdracht is er een verhaal gemaakt die gebaseerd is op ervaringen van vluchtelingen uit Oekraïne.")
    sleep(3)
    print("Wilt u het verhaal volgen?")
    sleep(3)
    volgverhaal = input("Voer in j of n ").lower()

    #continue
    if volgverhaal == "j" or volgverhaal == "ja" or volgverhaal == "y" or volgverhaal == "yes":
        sleep(1)
        print("Hier volgt her verhaal")
    elif volgverhaal == "n" or volgverhaal == "nee" or volgverhaal == "no":
        sleep(1)
        print("Bedankt voor uw aandacht, tot ziens!")
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        intro()
    
    # Begin verhaal
    if volgverhaal == "j" or volgverhaal == "ja" or volgverhaal == "y" or volgverhaal == "yes":
        start()
        



# def Start
def start():
    sleep(1)
    print("Je bent een student aan de Universiteit van Charkov in Oekraïne waar je Computer Science studeert. ")
    sleep(3)
    print("Je woont bij een oudere vrouw in huis waar je een hechte band mee hebt geschept.")
    sleep(3)
    print("Eerder in de week was op het nieuws al te horen dat de Russen Oekraïne waren binnen gevallen, je besloot om in de stad te blijven tot het niet meer kan. ")
    sleep(4)
    print("Tijdens het studeren achter je computer in je kamer gaan het luchtalarm af en de radio switcht naar het noodbericht: ")
    sleep(3)
    print("Rusland heeft de aanval gericht op de stad, de troepen zijn een paar dagen verwijdert van de stad.")
    sleep(3)
    print("Ga naar de schuilkelder of pak de laatste kans om te vluchten. ")
    sleep(4)
    print("Moldavië, Hongarije, Roemenië en Polen hebben hun grenzen open gezet voor vluchtelingen. ")
    sleep(3)
    print("Wees voorzichtig en God bless you all")
    sleep(3)
    room()


# (28, 30, 33, 34b, 45)[Stukje 1]
def room():
    sleep(1)    
    print("Je kijkt je kamer rondt en denkt na over je volgende plan. Wat doe je?")
    sleep(1)
    print("A. Je gaat spullen in een rugzak pakken") # 24
    print("B. Je raakt in paniek en rent de deur uit") # 25

    answer = input("A of B ").lower()

    if answer == "a":
        pack()
    elif answer == "b":
        outsidedoor()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        room()

# (25)[Stukje 15]
def outsidedoor():
    sleep(1)
    print("Je komt de deur uit. Welke kant ga je op?")
    sleep(1)
    print("A. Je gaat links naar de trein ") # 26
    print("B. Je gaat rechts naar de schuilkelder ") # 25

    answer = input("A of B ").lower()

    if answer == "a":
        running()
    elif answer == "b":
        bombshelter()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        outsidedoor()


# (26) [Stukje 16]
def running():
    sleep(1)
    print("Tijdens het rennen raak je moe en begin je met lopen." )
    sleep(1)
    print("Je raapt je gedachtens bij elkaar. ")
    sleep(1)
    print("Je maakt een beslissing. ")
    sleep(1)
    print("A. Je gaat terug naar je kamer") # 28
    print("B. Je gaat verder naar het treinstation ") # 29
    
    answer = input("A of B ").lower()

    if answer == "a":
        room()
    elif answer == "b":
        tv()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        running()

# (27)[Stukje 17]
def bombshelter():
    sleep(1)
    print("Je komt aan bij de schuilkelder en je komt tot rust. ")
    sleep(1)
    print("Je maakt een beslissing ")
    sleep()
    print("A. Je gaat terug naar je kamer ") # 30
    print("B. Je blijft in de schuilkelder ") # 31

    answer = input("A of B ").lower()

    if answer == "a":
        room()
    elif answer == "b":
        staybombshelter()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        bombshelter()


# (34a)[Stukje 18]
def noticket():
    sleep(1)
    print("Je komt aan bij het treinstation, maar je hebt geen geld voor een kaartje. ")
    sleep(1)
    print("Je besluit weer terug te gaan naar je kamer ") # 34b
    
    room()

# (31)[Stukje 19]
def staybombshelter():
    sleep(1)
    print("Je besluit te blijven.")
    sleep(1)
    print("Een dag gaat voorbij, de radio zegt dat de Russen een dag of twee van de stad verwijderd zijn.")
    sleep(1)
    print("Het is je laatste kans om te vluchten ")
    sleep(1)
    print("Wat ga je doen?")
    sleep(1)
    print("A. Je blijft nog langer") # 32
    print("B. Je gaat terug naar je kamer")

    answer = input("A of B ").lower()

    if answer == "a":
        ending1()
    elif answer == "b":
        room()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        staybombshelter()


# (29)[Stukje 20]
def tv():
    sleep(1)
    print("Je komt langs een winkel met tv's in het raam die het nieuws afspelen.")
    sleep(1)
    print("Je gaat staan luisteren")
    sleep(1)
    print("Er wordt gezegd om je goed voor te bereiden op je vlucht uit de stad. ")
    sleep(1)
    print("Wat ga je doen")
    sleep()
    print("A. Je gaat verder naar het trein station") # 34
    print("B. Je gaat terug naar je kamer") # 35

    answer = input("A of B ").lower()

    if answer == "a":
        noticket()
    elif answer == "b":
        room()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        tv()


# (24)[Stukje 14]
def pack():
    sleep(1)
    print("Je begint met het pakken van je spullen.")
    sleep(1)
    print("Wat neem je mee?")
    sleep(1)
    print("A. Je pakt essentiële spullen in") # 1
    print("B. Je pakt spullen in met emotionele waarde") # 2

    answer = input("A of B ").lower()

    if answer == "a":
        essential()
    elif answer == "b":
        emotional()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        pack()

# (1)[Stukje 2]
def essential():
    sleep(1)
    print("Uit welke tas met spullen kies je? ")
    sleep(1)
    print("A. De rugzak bevat: Geld, je paspoort, een waterfes en een aantal mueslirepen") # 3
    print("B. De rugzak bevat: Geld, je paspoort, een paar pakjes sap en de overgebleven aardappelen van vorige avond") # 4

    answer = input("A of B ").lower()

    if answer == "a":
        confirmEs()
    elif answer == "b":
        confirmEs()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        essential()

# (2)[Stukje 3]
def emotional():
    sleep(1)
    print("Uit welke tas met spullen kies je?")
    sleep(1)
    print("A. De rugzak bevat: Geld, je paspoort, een teddy beer en een boek") # 21
    print("B. De rugzal bevat: Geld, je paspoort, de handgemaakte deken van je huisbaas en een foto album") # 22

    answer = input("A of B ").lower()

    if answer == "a":
        confirmEm()
    elif answer == "b":
        confirmEm()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        emotional()

# (3, 4)[Stukje 4]
def confirmEs():
    sleep(1)
    print("Bevestig je keuze.")
    sleep(1)
    print("A. Bevestig") # 23
    print("B. Cancel") # 1

    answer = input("A of B ").lower()

    if answer == "a":
        where()
    elif answer == "b":
        essential()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        confirmEs()

# (21, 22)[Stukje 5]
def confirmEm():
    sleep(1)
    print("Bevestig je keuze.")
    sleep(1)
    print("A. Bevestig") # 23
    print("B. Cancel") # 2

    answer = input("A of B ").lower()

    if answer == "a":
        where()
    elif answer == "b":
        emotional()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        confirmEm()


# (23)[Stukje 6]
def where():
    sleep(1)
    print("Tijdens het inpakken komt je huisbaas je kamer binnen.")
    sleep(1)
    print("Ze verteld dat ze samen met de buren naar Polen gaat rijden en dat er nog een plekje voor jou is als je mee wilt.")
    sleep(1)
    print("Wat doe je?")
    sleep(1)
    print("A. Je besluit dat je met je huisbaas en de buren in de auto naar de grens van Polen gaat") # 5
    print("B. Je besluit om alleen te gaan reizen") # 6
    
    answer = input("A of B ").lower()

    if answer == "a":
        car()
    elif answer == "b":
        alone()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        where()

# (5)[Stukje 7]
def car():
    sleep(1)
    print("Het is druk op de weg, massa's mensen verplaatsen zich.")
    sleep(1)
    print("Maar uiteindelijk komt jullie auto aan bij de grens.")
    sleep(1)
    print("Daar krijg je informatie over mogelijke opties, je maakt samen met je gezelschap een besluit.")
    sleep(1)
    print("A. Je blijft bij je huisbaas die naar familie gaat in Polen") # 9
    print("B. Je gaat met de buren mee naar Nederland") # 10

    answer = input("A of B ").lower()

    if answer == "a":
        ending1()
    elif answer == "b":
        nl()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        car()


# (6)[Stukje 8]
def alone():
    sleep(1)
    print("Je hebt besloten om alleen te gaan.")
    sleep(1)
    print("Wat ga je doen?")
    sleep(1)
    print("A. Je gaat naar de boederij van een kennis van je huisbaas") # 7
    print("B. Je gaat naar de dichtsbijzijnde publieke schuilkelder") # 8

    answer = input("A of B ").lower()

    if answer == "a":
        farm()
    elif answer == "b":
        nofood()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        alone()

# (10)[Stukje 9]
def nl():
    sleep(1)
    print("Je bereikt Nederland met je buren, je kan twee dingen doen.")
    sleep(1)
    print("A. Je krijgt een vluchtelingen verblijfvergunning en blijft bij je buren") # 11
    print("B. Je gaat naar een vluchtelingenverblijf en wacht op een verblijfvergunning") # 12

    answer = input("A of B ").lower()

    if answer == "a":
        ending2()
    elif answer == "b":
        ending3()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        nl()


# (7)[Stukje 10]
def farm():
    sleep(1)
    print("Je bent op de boerderij aangekomen en er is wat tijd voorbij gegaan. ")
    sleep(1)
    print("Je hebt 2 opties.")
    sleep(1)
    print("A. Je blijft op de boerderij") # 19
    print("B. Je besluit om naar de grens te gaan") # 20

    answer = input("A of B ").lower()

    if answer == "a":
        ending4()
    elif answer == "b":
        toborder()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        farm()


# (8)[Stukje 11]
def nofood():
    sleep(1)
    print("Je verblijft een tijdje in de schuilkelder, maar uiteindelijk raakt je eten op en de Russen komen dichterbij de stad.")
    sleep(1)
    print("Wat doe je?")
    sleep(1)
    print("A. Je blijft in de schuilkelder") # 13
    print("B. Je vlucht de stad uit") # 14

    answer = input("A of B ").lower()

    if answer == "a":
        ending5()
    elif answer == "b":
        outcity()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        nofood()


# (20)[Stukje 21]
def toborder():
    sleep(1)
    print("Hoe ga je naar de grens?")
    sleep(1)
    print("A. Je lift mee met wat vrienden an de boer waar je verbleef") # 36
    print("B. Je gaat met de trein") # 37

    answer = input("A of B ").lower()

    if answer == "a":
        atborder()
    elif answer == "b":
        atborder()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        toborder()


# (16, 36, 37)[Stukje 12]
def atborder():
    sleep(1)
    print("Je komt aan bij de grens van Polen.")
    sleep(1)
    print("Wat ga je doen?")
    sleep(1)
    print("A. Je gaat naar Nederland") # 17
    print("B. Je gaat zoeken naar je huisbaas in Polen") # 18

    answer = input("A of B ").lower()

    if answer == "a":
        ending3()
    elif answer == "b":
        ending1()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        atborder()


# (14)[Stukje 13]
def outcity():
    sleep(1)
    print("Je besluit om de stad te ontvluchten.")
    sleep(1)
    print(" Waar ga je heen?")
    sleep(1)
    print("A. Je gaat naar het platteland, waar je een familie op een boederij vindt die je wilt opnemen") # 15
    print("B. Je gaat naar de Poolse grens") # 16

    answer = input("A of B ").lower()

    if answer == "a":
        ending4()
    elif answer == "b":
        atborder()
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        outcity()

    
# again after ending
def opnieuw():
    sleep(2)
    print("Je hebt een einde gevonden.")
    sleep(1)
    print("Wilt u het opnieuw proberen?")
        
    print("A. Start de applicatie opnieuw")
    print("B. Start het verhaal opnieuw")
    print("C. Verlaat de applicatie")
    antwoord = input("A, B of C ").lower()

    if antwoord == "a":
        intro()
    elif antwoord == "b":
        start()
    elif antwoord == "c":
        print("Bedankt voor het spelen! Tot ziens! :D ")
    else:
        print("Dit is geen optie, probeer het opnieuw. ")
        opnieuw() 
  

# def ending 1
def ending1():
    sleep(3)
    print("Je gaat met huisbaas mee naar haar familie, ze hebben ene kamer voor je vrij. ")
    sleep(4)
    print("Je gaat opzoek naar een baan en probeert daarnaast zelf door te studeren. ")
    sleep(4)
    print("Het enige wat je kan doen is wachten tot de oorlog voorbij is.")
    
    opnieuw()

# def ending 2
def ending2():
    sleep(3)
    print("Je besluit om bij de buren te blijven, je krijgt een vluchtelingen verblijfvergunning.")
    sleep(4)
    print("De buren hebben een huis kunnen regelen waar jij ook een verblijfplaats krijgt.")
    sleep(4)
    print("Ook hebben ze werk waar jij ook een baantje krijgt. ")
    
    sleep(3)
    opnieuw()

# def ending 3
def ending3():
    sleep(3)
    print("Je belandt op het vluchtelingen cruiseschip in Zaandam. ")
    sleep(4)
    print("Je moet wachten tot je een verblijfsvergunning krijgt. ")
    sleep(4)
    print("Tijdens het wachten probeer je mensen om je heen te helpen en je onderzoekt de omgeving van het nieuwe land waar je bent. ")
    sleep(4)
    print("Het enige wat je nu kan doen is wachten op je vergunning of tot de oorlog voorbij is.")
    
    sleep(3)
    opnieuw()

# def ending 4
def ending4():
    sleep(3)
    print("Je blijft op de boerderij, je werkt daar voor onderdak en eten.")
    sleep(3)
    print("Ook probeer je zelf je studie bij te houden. ")
    sleep(3)
    print("Je wacht tot de oorlog voorbij is en de Russen weg zijn uit je stad.")
    
    sleep(3)
    opnieuw()

# def ending 5
def ending5():
    sleep(3)
    print("Je besluit om in de schuilkelder te blijven tot het Russisch leger de stad heeft overgenomen en de bommen stoppen met vallen.")
    sleep(4)
    print("Je gaat weer terug naar je kamer die nog steeds staat.")
    sleep(4)
    print("Je zoekt naar werk. ")
    sleep(4)
    print("Leven gaat weer door maar met een Russische schaduw erover. ")
    sleep(4)
    print("Je wacht tot de oorlog voorbij gaat en de stad wordt bevrijdt. ")

    sleep(3)
    opnieuw()

# def ending 6
def ending6():
    sleep(3)
    print("Je gaat naar buiten en loopt richting je kamer.")
    sleep(4)
    print("Halverwege ontploft er een raket in het gebouw waar je naast loopt.")
    sleep(4)
    print("Je overlijdt aan je verwondingen op straat.")

    opnieuw()


# BEGIN APPLICATIE

# Introduction
intro()
