pi=3.141592653589793


def sphere(): #beräknar volym och area på en sfär
    radius=int(input("Ange radius"))
    volume=(4/3)*pi*radius**3
    area=4*pi*radius**2
    print("Volymen på sfären är ", volume, "och arean är ", area)
#sphere()

def pizza(): #beräknar pris/inch på en rund pizza
    price=int(input("Ange pris per pizza: "))
    diameter=int(input("Ange pizzans diameter (i inches): "))
    A=pi*(diameter/2)**2
    inchprice=price/A
    print("priset per inch är ", inchprice)
#pizza()

def carbs(): #beräknar vikt på kolhydrater
    atom=input("enter name of the carbohydrate")
    H=1.00794
    C=12.0107
    O=15.9994
    hyd, carb, oxy=eval(input("enter amount of atoms in order hydrogen, carbin, oxygen: "))
    weight=H*hyd+C*carb+O*oxy
    print("the weight of a", atom, "is", weight, "grams/mole")
#carbs()

def flash():# bestäm distansen till ett åsknedslag, i feet
    time=int(input("tid mellan nedslag och smäll: "))
    SpeedOfSound=1100 #ft/sec
    mile=5280 #ft
    dist=round(((time*SpeedOfSound)/mile), 4)
    print("Avståndet från åsknedslaget är ", dist, "miles")
#flash()

def slope():#beräknar lutningen mellan två pinkter i ett kordinatssystem
    x1, y1=eval(input("ange koordinat 1: "))
    x2, y2=eval(input("ange koordinat 2: "))
    slope=(y2-y1)/(x2-x1)
    print("lutningen mellan punkterna är", slope)
#slope()