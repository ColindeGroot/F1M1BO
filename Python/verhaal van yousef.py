import os             # Dit zorgt ervoor dat de vorige stukjes tekst verdwijnen (Dit werkt niet in Idle maar wel in cmd)
os.system("cls")
introductie = False
keuzeverhaal = False  #Dit zijn de introductie en keuzeverhaal (het spel zelf). Zodra het keuzeverhaal True is begint het spel.
stuk_1 = False
stuk_2 = False
stuk_3 = False
stuk_4 = False
stuk_5 = False
stuk_6 = False
stuk_7 = False
stuk_8 = False
stuk_9 = False
stuk_10 = False       
stuk_11 = False       # De verhaallijnen zijn opgedeeld in verschillende stukken en eindes 
stuk_12 = False
stuk_13 = False       # De stukken worden hieronder verdeeld op volgorde en niet op antwoord. Dit betekend dat De volgorde op het spel er anders uit ga zien.
stuk_14 = False
stuk_15 = False
stuk_16 = False
stuk_17 = False
stuk_18 = False
stuk_19 = False
stuk_20 = False
stuk_21 = False
einde_1 = False
einde_2 = False
einde_3 = False
einde_4 = False
einde_5 = False
einde_6 = False



#Hierin wordt verteeld aan de speler hoe het spel werkt
print("Hoi daar en welkom bij het verhaal van Yousef.")
print("In dit spel bepaal jij hoe Yousef zijn toekomst eruit gaat zien.")
print("")
print("Dit gebeurt door middel van stukjes tekst waar je twee keuzes kan maken: A of B.")
print("Elk antwoord leid je naar een ander stuk verhaal toe.")
print("Het kan soms zijn dat je met verschillende antwoorden wel hetzelfde einde krijgt.")
print("Je moet jezelf dus zien als het persoon in het verhaal.")
print("")
print("Voordat we beginnen komt er nog een kleine introductie om wat over Yousef zelf te leren.")
print("druk op enter waneer je wilt beginnen. ")
print("")
start = input()
print("")

introductie = True
keuzeverhaal = True

while keuzeverhaal == True:

#Dit is een kleine introductie dat iets over Yousef verteld
    while introductie == True:
        print("Yousef is een vluchteling uit Afghanistan")
        print("Yousef is nu veilig in gelukkig in Nederland maar dat is niet altijd zo geweest")
        print("")
        print("Hij had namelijk verschillende reden om te vluchten.")
        print("Een paar van die reden worden verteld in het verhaal.")
        print("")
        print("Druk op enter om verder te gaan.")
        print("")
        drukeenknop = input()
        print("")
        stuk_1 = True
        introductie = False
    

    #stuk 1 van het verhaal
    while stuk_1 == True:
        print("Het begin")
        print("")
        print("Yousef woont met zijn drie broers, vier zussen en ouders in Afghanistan.")
        print("Hij heeft het hier naar zijn zin todat zijn vader komt te overlijden.")
        print("Hierdoor is Yousef nu verantwoordelijk voor het gezin.")
        print("")
        print("Yousef vind dat de verantwoordelijkheid heel veel druk geeft.")
        print("")
        print("A: Blijf zorgen voor het gezin.")
        print("B: zoek een uitweg.")
        antwoord_1 = input()
    
        if antwoord_1 == "A": #Het variabel van antwoord wordt steeds hernoemt per stuk (antwoord_1 antwoord_2 etc.)
            stuk_2 = True
            stuk_1 = False
        
        elif antwoord_1 == "B":
            stuk_3 = True
            stuk_1 = False  #Dit zorgt ervoor dat het volgende stukje tekst verschijnt en het stukje hiervoor niet meer van toepassing is in de while loop.

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")
            continue

    #stuk 2 van het verhaal
    while stuk_2 == True:
        print("")
        print("Yousef kiest er voor om voor zijn gezin te blijfen zorgen.")
        print("Hij neemt een pauze van school om geld te kunnen verdienen. zodat hij het gezin kan onderhouden.")
        print("")
        print("Na een tijd besluit Yousef weer te werken en krijgt uiteindelijk een baan van de overheid als projectmanager.")
        print("Hier gaat hij naar andere dorpen om hun te informeren over ontwikkeling.")
        print("Helaas voor Yousef zijn er een hoop mensen tegen de overheid en daarmee ook tegen Yousef zelf.")
        print("Ga je A: Blijfen werken of B: Een andere baan zoeken?")
        antwoord_2 = input()

        if antwoord_2 == "A":
            stuk_6 = True
            stuk_2 = False

        elif antwoord_2 == "B":
            stuk_7 = True
            stuk_2 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("Yousef kiest ervoor om zijn gezin achter te laten.")
            continue

    #stuk 3 van het verhaal
    while stuk_3 == True:
        print("")
        print("Yousef kiest ervoor om zijn gezin achter te laten.")
        print("Zonder een plek om heen te gaan besluit Yousef een nieuw leven buiten de stad te zoeken.")
        print("Helaas komt hij al gauw tegen een probleem wanneer hij de deur uit is. Hij komt namelijk een stel overvallers tegen.")
        print("Ze willen al zijn bezittingen maar Yousef heeft een hoop achtergelaten.")
        print("De overvallers geloven Yousef niet waardoor hij nu een groot probleem heeft.")
        print("A: schreeuw om hulp")
        print("B: probeer de overvaller af te leiden.")
        antwoord_3 = input()

        if antwoord_3 == "A":
            stuk_4 = True
            stuk_3 = False

        elif antwoord_3 == "B":
            stuk_5 = True
            stuk_3 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 4 van het verhaal einde1
    while stuk_4 == True:
        print("")
        print("Yousef besluit om voor hulp te schreeuwen.")
        print("Een van de overvallers houd zijn hand voor de mond van Yousef in de hoop dat niemand hem hoort.")
        print("Gelukkig heeft een agent om de hoek de schreeuwkreet gehoord en besluit te gaan kijken wat er aan de hand is.")
        print("Wanneer de agent de overvallers tegemoet komt trekt hij zijn pistool wat de overvallers afschrikt.")
        print("")
        print("De agent vraagt aan Yousef of hij mee wilt komen naar het bureau voor zijn eigen veiligheid.")
        print("Eenmaal op het bureau legt Yousef de situatie uit waarna de agent actie besluit te ondernemen.")
        print("")
        print("Na een paar telefoontjes heeft de agent een kamer weten te regelen in een verzorgtehuis waar families in problemen ook welkom zijn.")
        print("Na het krijgen van hulp besluit Yousef zelf om in de zorg te gaan om zo andere mensen met problemen te kunnen helpen.")
        print("Hij krijgt uiteindelijk een mooie baan in het buitenland als chirurg waar hij samen met zijn familie veilig en tevreden is.")
        print("")
        print("Dit was een van de verschillende eindes van het verhaal.")
        print("Als je het wilt kan je het nog altijd opnieuw spelen.")
        print("")
        print("A. Ja")
        print("B. Nee")
        einde_1 = input()

        if einde_1 == "A":
            introductie = True
            stuk_4 = False

        elif einde_1 == "B":
            print("Tot de volgende keer!")
            keuzeverhaal = False
            stuk_4 = False

        else:
            print("Helaas! Dit is geen geldgig antwoord")
            print("")
            continue

    #stuk 5 van het verhaal einde2
    while stuk_5 == True:
        print("")
        print("Yousef probeert met een smoes de overvallers af te leiden.")
        print("Helaas kwam Yousef niet ver want de overvallers merkte het snel op toen Yousef probeerde te ontsnappen en maakte korte metten met hem.")
        print("")
        print("Dit was een van de verschillende eindes van het verhaal.")
        print("Wil je het nog een keer spelen?")
        print("")
        print("A. Ja")
        print("B. Nee")
        einde_2 = input()

        if einde_2 == "A":
            introductie = True
            stuk_5 = False

        elif einde_2 == "B":
            print("Tot de volgende keer!")
            keuzeverhaal = False
            stuk_5 = False

        else:
            print("Helaas! Dit is geen geldgig antwoord")
            print("")
            continue

    #stuk 6 van het verhaal
    while stuk_6 == True:
        print("")
        print("Yousef besluit zijn baan te behouden, maar is niet bewust dat IS optocht is en iedereen die betrokken is bij de overheid dood wil hebben.")
        print("De overheid wilt Yousef naar een andere provincie verplaatsen maar doordat IS zo groot is heeft dat weining nut.")
        print("")
        print("Nu Yousef nergens heenkan zit hij in de problemen.")
        print("Gelukkig heeft een bekende die informatie over een smokkelaar die hem naar Engeland kan brengen.")
        print("Het is alleen niet goedkoop namelijk $25.000 dollar.")
        print("")
        print("A: betaal het bedrag.")
        print("B: betaal niet.")
        antwoord_6 = input()

        if antwoord_6 == "A":
            stuk_8 = True
            stuk_6 = False

        elif antwoord_6 == "B":
            stuk_9 = True
            stuk_6 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 7 van het verhaal
    while stuk_7 == True:
        print("")
        print("Yousef wilt een andere baan zoeken maar ondanks dat willen de mensen Yousef alsnog weg hebben waardoor zijn enigste optie vluchten is.")
        print("Gelukkig heeft een bekkende van hem informatie over een smokkelaar die hem naar Engeland kan brengen.")
        print("Het is alleen niet goedkoop namelijk $25.000 dollar.")
        print("")
        print("A: betaal het bedrag.")
        print("B: betaal niet.")
        antwoord_7 = input()

        if antwoord_7 == "A":
            stuk_8 = True
            stuk_7 = False

        elif antwoord_7 == "B":
            stuk_9 = True
            stuk_7 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 8 van het verhaal
    while stuk_8 == True:
        print("")
        print("Yousef besluit het geld te betalen door middel van zwart geld.")
        print("Eenmaal betaald maakt de smokkelaar een nep paspoort aan voor Yousef.")
        print("Het plan is om via Pakistan naar Istanbul te vliegen en om vanuit daar naar Engeland te rijden.")
        print("")
        print("Eenmaal klaar voor de reis word Yousef verteld dat hij niks mee mag nemen alleen iets dat in zijn zakken past.")
        print("Wanneer Yousef is aankomt in Pakistan verblijft hij voor een tijdje in een hotel.")
        print("Vanuit daar kwamen twee andere mensen mee die ook zijn gevlucht.")
        print("")
        print("Ondanks al best ver te zijn twijfelt Yousef of hij wel wilt doorgaan het word inmiddels een spannende en gevaarlijke reis.")
        print("")
        print("A: maak de reis af")
        print("B: verlaat de smokkelaar")
        antwoord_8 = input()

        if antwoord_8 == "A":
            stuk_10 = True
            stuk_8 = False

        elif antwoord_8 == "B":
            stuk_11 = True
            stuk_8 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 9 van het verhaal
    while stuk_9 == True:
        print("")
        print("Youssef besluit om zelf te vluchten door onopgemerkt met een vrachtwagen mee liften")
        print("Wanneer niemand het merkt klimt Yousef in een container van een vrachtwagen die vervolgens naar Engeland word verzonden.")
        print("")
        print("Eenmaal bij de grens van Engeland word de vrachtwagen tegengehouden.")
        print("De douane vind het voertuig er verdacht uit zien en besluit vervolgens de vrachtwagen te doorzoeken.")
        print("")
        print("Yousef is bang dat hij in de problemen komt wanneer hij zich zelf niet aangeeft maar alsnog word gevonden.")
        print("Tegelijkertijd wilt Yousef verstopt blijven zodat hij kan genieten van de vrijheid als hij eenmaal in Engeland is.")
        print("")
        print("A: Blijf verstopt")
        print("B: Geef jezelf aan")
        antwoord_9 = input()

        if antwoord_9 == "A":
            stuk_12 = True
            stuk_9 = False

        elif antwoord_9 == "B":
            stuk_13 = True
            stuk_9 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 10 van het verhaal
    while stuk_10 == True:
        print("")
        print("Yousef besluit door te gaan met de reis.")
        print("")
        print("Eenmaal aangekomen op het vliegveld is Yousef erg nerveus want hij vertrouwt het neppe paspoort niet.")
        print("Vanuit Istanbul rijden ze naar Amsterdam.")
        print("Wanneer ze in Amsterdam zijn zegt de smokkelaar iets te moeten doen en zo terug te zijn.")
        print("Helaas verschijnt hij niet meer en beseft Yousef dat hij is afgezet door de smokkelaar.")
        print("Yousef heeft nu geen idee waar hij is of wat hij moet doen.")
        print("")
        print("A: Zoek het dichtstbij zijnde politiebureau")
        print("B: Overnacht voor een dagje op straat")
        antwoord_10 = input()

        if antwoord_10 == "A":
            stuk_14 = True
            stuk_10 = False

        elif antwoord_10 == "B":
            stuk_15 = True
            stuk_10 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")


    #stuk 11 van het verhaal
    while stuk_11 == True:
        print("")
        print("Yousef vertrouwd de smokkelaar niet en besluit de reis in zijn eentje af te maken.")
        print("Eenmaal aangekomen in Istanbul verzint Yousef een smoes om uit de groep te weten te komen.")
        print("Wanneer Yousef weet dat niemand kijkt rent hij snel weg.")
        print("")
        print("Net wanneer Yousef uit de stad denkt te zijn heeft de smokkelaar hem in zijn vizier.")
        print("Wanneer de smokkelaar vraagt waarom Yousef weg rent legt hij uit dat hij hem niet vertrouwd.")
        print("Na een lang gesprek te hebben weet de smokkelaar Yousef over te halen om de reis af te maken.")
        print("")
        print("Druk op enter om door te gaan")
        antwoord_11 = input()
        stuk_10 = True
        stuk_11 = False

    #stuk 12 van het verhaal
    while stuk_12 == True:
        print("")
        print("Yousef besluit zich te verstoppen tussen de goederen die zich in de container bevinden.")
        print("De douane besluit speurhonden te gebruiken om eventuele drugs op te sporen.")
        print("Gelukkig merken de honden niet op dat Yousef zich in de container bevindt waardoor de douane de vrachtwagen door laat gaan.")
        print("")
        print("De vrachtwagen maakt uiteindelijk een tijdelijke stop in een Engels dorpje.")
        print("Yousef heeft geen idee waar hij is maar hij weet ook niet waar hij uitkomt als hij bij de vrachtwagen blijft.")
        print("Yousef heeft uiteindelijk een tijd niet gegeten of gedronken.")
        print("")
        print("A: Neem een kijkje in het dorp")
        print("B: Blijf in de vrachtwagen")
        antwoord_12 = input()

        if antwoord_12 == "A":
            stuk_18 = True
            stuk_12 = False

        elif antwoord_12 == "B":
            stuk_19 = True
            stuk_12 = False

        else:
            print("Helaas! Dit is geen geldig antwoord.")
            print("")

    #stuk 13 van het verhaal einde 3
    while stuk_13 == True:
        print("")
        print("Yousef besluit zichzelf aan te geven in de hoop dat de situatie niet escaleert.")
        print("De agenten pakken hem op en zetten hem in een tijdelijke cel waar hij de nacht door brengt.")
        print("")
        print("De volgende dag gaat de politie in gesprek met Yousef.")
        print("Hier wordt verteld dat Yousef terug wordt gestuurd naar zijn eigen land sinds alle andere vluchtelingen kampen al vol zitten.")
        print("Yousef twee dagen na het gesprek terug gestuurd naar Afghanistan.")
        print("")
        print("Nu Yousef terug is gestuurd naar Afghanistan probeert hij weinig van zichzelf te laten merken.")
        print("Dat betekent dat hij ook niet naar zijn familie toe kan omdat hij niet wilt dat zij gevaar lopen.")
        print("Hij neemt Yousef kleine baantjes aan zoals schoonmaker en receptionist.")
        print("")
        print("Wanneer de dreiging wat minder word besluit Yousef naar zijn familie te gaan.")
        print("Eenmaal daar beidt Yousef zijn excuses aan en besluit verder voor het gezin te zorgen.")
        print("")
        print("Dit was een van de verschillende eindes van het verhaal.")
        print("Wil je het nog een keer spelen?")
        print("")
        print("A. Ja")
        print("B. Nee")
        einde_2 = input()

        if einde_2 == "A":
            introductie = True
            stuk_5 = False

        elif einde_2 == "B":
            print("Tot de volgende keer!")
            keuzeverhaal = False
            stuk_5 = False

        else:
            print("Helaas! Dit is geen geldgig antwoord")
            print("")
            continue
      

        

        
 
        
        


        




    
    
        
   


