import random
from collections import Counter


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
station= ["Sídliště Havranov","George Orwella", "Náměstí 1984","Hlavní nádraží", "Hotel Intercontinental", "Obchodní centrum", "Důl Lučina", "Náměstí Jurije Gagarina", "Městská radnice", "Škola Ahepjuka", "Katalánská", "Slezská", "Moravská", "Mozartova", "VŠM", "Okruh", "MMR1 vedení", "Městský úřad", "Správní kotrola pro oblast", "Zahrady", "Zoologická zahrada", "Park Milady Horákové"]
stops = []
lines = []
passengers = []
count = 0
K_LINEK = 4
K_STANIC = 2.5
#Tvroba zastávek
for x in station:
    stops.append(Stop(x))
#Tvroba linek
for i in range(len(stops)//K_LINEK):
    counter = 0
    my_list = []
    skip = False
    random.shuffle(stops)
    for b in stops: 
        if skip:
            continue
        my_list.append(b)
        counter +=1
        if counter == len(stops)//K_STANIC:
            lines.append(Line(i+2, my_list))
            counter = 0
            my_list = []
            random.shuffle(stops)
            skip = True
            continue
#Kontrola, zda nějaká linka neutekla
check = []
check_2 = []
check_3 = []
check_total= []
for x in station:
    check.append(x)
for x in station:
    check_2.append(x)
for x in lines:
    for y in x.stops:
        for a in check:
            if a == y.name:
                check.remove(a)
#Jestli utekla, tvorba nové linky
for x in check:
    for y in check_2:
        if x == y:
            check_3.append(x)
for x in check_3:
    check_2.remove(x)
print("Neobsluhované zastávky: \n")
for x in check:
    print(f"Neobshluhovaná zastávka: {x}")
while len(check_2) > (len(stops)//K_STANIC -1):
    check_2.remove(random.choice(check_2))
for x in check_2:
    check.append(x)
for x in stops:
    for y in check:
        if x.name == y:
            check_total.append(x)
lines.append(Line(1, check_total))
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
#for p in passengers:
    #print(p.position,"--", p.destination)
matching = 0
unmatching = 0
may = []
for x in passengers:
    possible = []
    for a in lines:
        for b in a.stops:
            if x.position == b.name:
                #print(f"zastávkou, kde nastupuje projízdí linka č. {a.number}")
                possible.append(a.number)
            if x.destination == b.name:
                #print(f"zastávkou, kde vystupuje projízdí linka č. {a.number}")
                possible.append(a.number)
    possible.sort()
    match = False
    for a in range(len(possible) -1):
        if possible[a] == possible[a+1]:
            #print(f"SHODA! Přímý spoj pro {x.position} a {x.destination} - linka č. {possible[a]} tudy projíždí")
            may.append(possible[a])
            matching +=1
            match = True
    if not match:
        #print(f"NESHODA! Tudy nejezdí žádná linka pro {x.position} a {x.destination}")
        unmatching +=1
    #break
print (f"Přímý spoj má {matching}, nemá ho {unmatching}")
for i, x in enumerate(Counter(may).most_common(6),1):
    print(f"Nejpoužívanější linka č. {i}: {x}")
#Engine
