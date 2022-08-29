#Boards are defined from the top
import random
firstboard = [0, 0, 0, 0]
secondboard = [0, 0, 0, 0]
thirdboard = [0, 0, 0, 0]
fourthboard = [0, 0, 0, 0]
nextcell = random.randint(2,17)
cell = 2
print(nextcell)

if nextcell <= 3:
    firstboard[nextcell] = 2
if nextcell >= 3 and nextcell <= 7:
    nextcell = nextcell - 5
    secondboard[nextcell] = 2
if nextcell >= 7 and nextcell <= 11:
    nextcell = nextcell - 9
    thirdboard[nextcell] = 2
if nextcell >= 11:
    nextcell = nextcell - 13
    fourthboard[nextcell] = 2

def gameupdate():
    print(firstboard)
    print(secondboard)
    print(thirdboard)
    print(fourthboard)


def cellcreation():
    #random cell creation
    nextcell = random.randrange(1,15)
    print(nextcell)
    counter = 0
    for i in range (16):
        if i <= 4:
            if firstboard[i - 1] == 0:
                iat = i
                counter += 1 

        if i <= 8 and i >= 4:
            converted = i - 5
            if secondboard[converted]:
                iat = i
                counter += 1 

        if i <= 12 and i >= 8:
            converted = i - 9
            if thirdboard[converted]:
                iat = i
                counter += 1 

        if i <= 16 and i >= 12:
            converted = i - 13
            if fourthboard[converted]:
                iat = i
                counter += 1
                
    if counter == 1:
        nextcell = iat



            
    if nextcell <= 4:
        nextcell = nextcell - 2
        if firstboard[nextcell] == 0:
            print(nextcell)
            firstboard[nextcell] = cell
        else:
            cellcreation()
        
    if nextcell >= 4 and nextcell <= 8:
        nextcell = nextcell - 5
        if secondboard[nextcell] == 0:
            print(nextcell)
            secondboard[nextcell] = cell
        else:
            cellcreation()

    if nextcell >= 8 and nextcell <= 12:
        nextcell = nextcell - 9
        if thirdboard[nextcell] == 0:
            print(nextcell)
            thirdboard[nextcell] = cell
        else:
            cellcreation()

    if nextcell >= 12:
        nextcell = nextcell - 13
        if fourthboard[nextcell] == 0:
            print(nextcell)
            fourthboard[nextcell] = cell
        else:
            cellcreation() 

def logic():
    keypressed = input()
    if keypressed != 'w' and keypressed != 'a' and keypressed != 's' and keypressed != 'd':
        print('error, string entered is not a valid control option')
        logic()
    if keypressed == 's':
        for i in range (4):
            if secondboard[i - 1] == 0:
                secondboard[i - 1] = firstboard[i - 1]
                firstboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if fourthboard[i - 1] == 0:
                fourthboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0

        for i in range (4):
            if secondboard[i - 1] == firstboard[i - 1]:
                secondboard[i - 1] = secondboard[i - 1] * 2
                firstboard = 0

            if thirdboard[i - 1] == secondboard[i - 1]:
                thirdboard[i - 1] = thirdboard[i - 1] * 2
                secondboard = 0

            if fourthboard[i - 1] == thirdboard[i - 1]:
                fourthboard[i - 1] = fourthboard[i - 1] * 2
                thirdboard = 0

        for i in range (4):
            if secondboard[i - 1] == 0:
                secondboard[i - 1] = firstboard[i - 1]
                firstboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if fourthboard[i - 1] == 0:
                fourthboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0
    
    cellcreation()


gameupdate()
logic()
gameupdate()

