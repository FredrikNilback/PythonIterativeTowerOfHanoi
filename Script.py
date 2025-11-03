from Tower import Tower

print(
r""" _____                               __   _   _                   _ 
|_   _|                             / _| | | | |                 (_)
  | | _____      _____ _ __    ___ | |_  | |_| | __ _ _ __   ___  _ 
  | |/ _ \ \ /\ / / _ \ '__|  / _ \|  _| |  _  |/ _` | '_ \ / _ \| |
  | | (_) \ V  V /  __/ |    | (_) | |   | | | | (_| | | | | (_) | |
  \_/\___/ \_/\_/ \___|_|     \___/|_|   \_| |_/\__,_|_| |_|\___/|_|
      
""")

numberOfDiscs = 0
while True:
    numberOfDiscs = input("Enter number of discs: ")

    try:
        numberOfDiscs = int(numberOfDiscs)
        break
    except ValueError:
        print("Enter an integer!")
        continue

towerA = Tower("A")
towerB = Tower("B")
towerC = Tower("C")
global numberOfMoves
numberOfMoves = 0
bestPossible = 2 ** numberOfDiscs - 1

for i in range(numberOfDiscs, 0, -1):
    towerA.placeDisc(i, supressPrint=True)
print(towerA.discList, towerB.discList, towerC.discList)

def move(fromTower: Tower, toTower: Tower, supressPrint: bool = False):
    if (fromTower == toTower):
        return
    discLenghtBefore = len(toTower.discList)
    disc = fromTower.takeDisc(supressPrint=supressPrint)
    if (disc):
        toTower.placeDisc(disc, supressPrint=supressPrint)

    if (len(toTower.discList) <= discLenghtBefore) and disc:
        fromTower.placeDisc(disc, supressPrint=True)

def checkVictory():
    print(towerA.discList, towerB.discList, towerC.discList)
    if (len(towerC.discList) == numberOfDiscs):
        print("YOU WIN!")
        print("Moves:", numberOfMoves, "best possible:", bestPossible)
        raise SystemExit()

def resetTowers():
    towerA.discList = []
    towerB.discList = []
    towerC.discList = []
    for i in range(numberOfDiscs, 0, -1):
        towerA.placeDisc(i, supressPrint=True)

def bitFlipped(current, next):
    return (current ^ next).bit_length() 

def Solver():
    resetTowers()
    global numberOfMoves
    numberOfMoves = 0
    if (numberOfDiscs % 2 == 0):
        for i in range(1, bestPossible + 1):
            discToMove = bitFlipped(numberOfMoves, i)
            print("Moving disc:", discToMove)
            numberOfMoves = i
            print("Move number:", numberOfMoves)

            notFound = True
            fromTower = towerA
            while notFound:
                for j in range(len(towerA.discList)):
                    if (towerA.discList[j] == discToMove):
                        fromTower = towerA
                        notFound = False
                        break
                for j in range(len(towerB.discList)):
                    if (towerB.discList[j] == discToMove):
                        fromTower = towerB
                        notFound = False
                        break
                for j in range(len(towerC.discList)):
                    if (towerC.discList[j] == discToMove):
                        fromTower = towerC
                        notFound = False
                        break

            if (discToMove == 1 and fromTower == towerA):
                move(fromTower, towerB, supressPrint=True)
            elif (discToMove == 1 and fromTower == towerB):
                move(fromTower, towerC, supressPrint=True)
            elif (discToMove == 1 and fromTower == towerC):
                move(fromTower, towerA, supressPrint=True)
            else:
                move(fromTower, towerA, supressPrint=True)
                move(fromTower, towerB, supressPrint=True)
                move(fromTower, towerC, supressPrint=True)  
            checkVictory()        
                
    else:
        for i in range(1, bestPossible + 1):
            discToMove = bitFlipped(numberOfMoves, i)
            print("Moving disc", discToMove)
            numberOfMoves = i
            print("Move number:", numberOfMoves)

            notFound = True
            fromTower = towerA
            while notFound:
                for j in range(len(towerA.discList)):
                    if (towerA.discList[j] == discToMove):
                        fromTower = towerA
                        notFound = False
                        break
                for j in range(len(towerB.discList)):
                    if (towerB.discList[j] == discToMove):
                        fromTower = towerB
                        notFound = False
                        break
                for j in range(len(towerC.discList)):
                    if (towerC.discList[j] == discToMove):
                        fromTower = towerC
                        notFound = False
                        break

            if (discToMove == 1 and fromTower == towerA):
                move(fromTower, towerC, supressPrint=True)
            elif (discToMove == 1 and fromTower == towerB):
                move(fromTower, towerA, supressPrint=True)
            elif (discToMove == 1 and fromTower == towerC):
                move(fromTower, towerB, supressPrint=True)
            else:
                move(fromTower, towerA, supressPrint=True)
                move(fromTower, towerB, supressPrint=True)
                move(fromTower, towerC, supressPrint=True) 
            checkVictory()
            

while True:
    fromTowerString = input("Select tower to move from [A/B/C]: ")
    fromTower = 0
    match fromTowerString:
        case "A" | "a":
            fromTower = towerA
        case "B" | "b":
            fromTower = towerB
        case "C" | "c":
            fromTower = towerC
        case "IMessedUp":
            resetTowers()
            continue
        case "SolvePlz":
            Solver()
            break
        case _:
            continue

    toTowerString = input("Select tower to move to [A/B/C]: ")
    toTower = 0
    match toTowerString:
        case "A" | "a":
            toTower = towerA
        case "B" | "b":
            toTower = towerB
        case "C" | "c":
            toTower = towerC
        case "IMessedUp":
            resetTowers()
            continue
        case "SolvePlz":
            Solver()
            break
        case _:
            continue

    move(fromTower, toTower)
    numberOfMoves += 1
    checkVictory()