import random
#Inicializace
class Line:
    def __init__(self, number, stops):
        self.number = number
        self.stops = stops
class Stop:
    def __init__(self, name):
        self.name = name
        self.rarity = random.choice(["rare", "common", "very common"])
class Passenger:
    def __init__(self, destination, position):
        self.destination = destination
        self.position = position
station= ["Sídliště Havranov","George Orwella", "Náměstí 1984","Hlavní nádraží", "Hotel Intercontinental", "Obchodní centrum", "Důl Lučina", "Náměstí Jurije Gagarina", "Městská radnice", "Škola Ahepjuka"]
stops = []
lines = []
passengers = []
count = 0
#Tvroba zastávek
for x in station:
    stops.append(Stop(x))
#Tvroba linek
for i in range(len(stops)//3):
    counter = 0
    my_list = []
    skip = False
    random.shuffle(stops)
    for b in stops: 
        if skip:
            continue
        my_list.append(b)
        counter +=1
        if counter == len(stops)//1.8:
            lines.append(Line(i+2, my_list))
            counter = 0
            my_list = []
            random.shuffle(stops)
            skip = True
            continue
#Kontrola, zda nějaká linka neutekla
check = station
for x in lines:
    for y in x.stops:
        for a in check:
            if a == y.name:
                check.remove(a)
#Jestli utekla, tvorba nové linky
print("Neobsluhované zastávky: \n")
for x in check:
    print(f"Neobshluhovaná zastávka: {x}")
check_3 = station
check_2 = station
for x in check_2:
    for y in check:
        if x == y:
            check_3.append(x)
for x in check_3:
    check_2.remove(x)
for x in check_2:
    check.append(x)
lines.append(Line(1, check))    
#Vypsání
for x in lines:
    print(x.number)
    for a in x.stops:
        print (a.name)
#Init zastávek
for x in stops:
    if x.rarity == "rare":
        count += 1
    elif x.rarity == "common":
        count += 3
    elif x.rarity == "very common":
        count += 5
#Init cestujících
for x in range(count):
    destination = random.choice(station)
    position = random.choice(station)
    while position == destination:
        position = random.choice(station)
    passengers.append(Passenger(destination, position))
#Engine
print("\n")
for p in passengers:
    print(p.position,"--", p.destination)
for x in passengers:
    possible = []
    for a in lines:
        for b in a.stops:
            if x.position == b.name:
                print(f"zastávkou, kde nastupuje projízdí linka č. {a.number}")
                possible.append(a.number)
            if x.destination == b.name:
                print(f"zastávkou, kde vystupuje projízdí linka č. {a.number}")
                possible.append(a.number)
    possible.sort()
    for a in range(len(possible)-1):
        if possible[a] == possible[a+1]:
            print(f"SHODA! Přímý spoj pro {x.position} a {x.destination} - linka č. {possible[a]} tudy projíždí")
    break
