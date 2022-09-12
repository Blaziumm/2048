#Boards are defined from the top
import random
firstboard = [0, 0, 0, 0]
secondboard = [0, 0, 0, 0]
thirdboard = [0, 0, 0, 0]
fourthboard = [0, 0, 0, 0]
nextcell = random.randint(2,17)
cell = 2
welcomemessage = 'Welcome, use w, a, s, d to control the game, try to reach 2048 without filling the board!'
print(welcomemessage)



if nextcell <= 3:
    firstboard[nextcell] = 2
if nextcell >= 3 and nextcell <= 7:
    nextcell = nextcell - 5
    secondboard[nextcell] = 2
if nextcell >= 7 and nextcell <= 11:
    nextcell = nextcell - 9
    thirdboard[nextcell] = 2
if nextcell >= 11:
    nextcell = nextcell - 14
    fourthboard[nextcell] = 2

def gameupdate():
    print(firstboard)
    print(secondboard)
    print(thirdboard)
    print(fourthboard)
    logic()


def cellcreation():
    #random cell creation
    nextcell = random.randrange(1,15)

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
           
            firstboard[nextcell] = cell
        else:
            cellcreation()
        
    if nextcell >= 4 and nextcell <= 8:
        nextcell = nextcell - 5
        if secondboard[nextcell] == 0:
            
            secondboard[nextcell] = cell
        else:
            cellcreation()

    if nextcell >= 8 and nextcell <= 12:
        nextcell = nextcell - 9
        if thirdboard[nextcell] == 0:
            
            thirdboard[nextcell] = cell
        else:
            cellcreation()

    if nextcell >= 12:
        nextcell = nextcell - 13
        if fourthboard[nextcell] == 0:
           
            fourthboard[nextcell] = cell
        else:
            cellcreation() 
    gameupdate()
def logic():
    keypressed = input()
    if keypressed != 'w' and keypressed != 'a' and keypressed != 's' and keypressed != 'd':
        print('Error, string entered is not a valid control option')
        
    if keypressed == 's':
        for i in range (4):

            #Colapse

            if secondboard[i - 1] == 0:
                secondboard[i - 1] = firstboard[i - 1]
                firstboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if fourthboard[i - 1] == 0:
                fourthboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0

            #Merge
            if secondboard[i - 1] == firstboard[i - 1] and firstboard[i - 1] != 0:
                secondboard[i - 1] = firstboard[i - 1] * 2
                firstboard[i - 1] = 0
            
            if thirdboard[i - 1] == secondboard[i - 1] and secondboard[i - 1] != 0:
                thirdboard[i - 1] = secondboard[i - 1] * 2
                secondboard[i - 1] = 0 

            if fourthboard[i - 1] == thirdboard[i - 1] and thirdboard[i - 1] != 0:
                fourthboard[i - 1] = thirdboard[i - 1] * 2
                thirdboard[i - 1] = 0


            #Colapse
            if secondboard[i - 1] == 0:
                secondboard[i - 1] = firstboard[i - 1]
                firstboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if fourthboard[i - 1] == 0:
                fourthboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0


    elif keypressed == 'w':
        for i in range (4):

            #Colapse

            if firstboard[i - 1] == 0:
                firstboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if secondboard[i - 1] == 0:
                secondboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = fourthboard[i - 1]
                fourthboard[i - 1] = 0

            #Merge
            if firstboard[i - 1] == secondboard[i - 1] and firstboard[i - 1] != 0:
                firstboard[i - 1] = secondboard[i - 1] * 2
                secondboard[i - 1] = 0
            
            if secondboard[i - 1] == thirdboard[i - 1] and secondboard[i - 1] != 0:
                secondboard[i - 1] = thirdboard[i - 1] * 2
                thirdboard[i - 1] = 0

            if thirdboard[i - 1] == fourthboard[i - 1] and secondboard[i - 1] != 0:
                thirdboard[i - 1] = fourthboard[i - 1] * 2
                fourthboard[i - 1] = 0


            #Colapse
            if firstboard[i - 1] == 0:
                firstboard[i - 1] = secondboard[i - 1]
                secondboard[i - 1] = 0

            if secondboard[i - 1] == 0:
                secondboard[i - 1] = thirdboard[i - 1]
                thirdboard[i - 1] = 0

            if thirdboard[i - 1] == 0:
                thirdboard[i - 1] = fourthboard[i - 1]
                fourthboard[i - 1] = 0
    elif keypressed == 'a':
#Colapse (1st Section)
        if firstboard[2] == 0:
                firstboard[2] = firstboard[3]
                firstboard[3] = 0

        if firstboard[1] == 0:
                firstboard[1] = firstboard[2]
                firstboard[2] = 0

        if firstboard[0] == 0:
                firstboard[0] = firstboard[1]
                firstboard[1] = 0
#Second Section
        if secondboard[2] == 0:
                secondboard[2] = secondboard[3]
                secondboard[3] = 0

        if secondboard[1] == 0:
                secondboard[1] = secondboard[2]
                secondboard[2] = 0

        if secondboard[0] == 0:
                secondboard[0] = secondboard[1]
                secondboard[1] = 0

#third
        if thirdboard[2] == 0:
                thirdboard[2] = thirdboard[3]
                thirdboard[3] = 0

        if thirdboard[1] == 0:
                thirdboard[1] = thirdboard[2]
                thirdboard[2] = 0

        if thirdboard[0] == 0:
                thirdboard[0] = thirdboard[1]
                thirdboard[1] = 0

#fourth
        if fourthboard[2] == 0:
                fourthboard[2] = fourthboard[3]
                fourthboard[3] = 0

        if fourthboard[1] == 0:
                fourthboard[1] = fourthboard[2]
                fourthboard[2] = 0

        if fourthboard[0] == 0:
                fourthboard[0] = fourthboard[1]
                fourthboard[1] = 0

#Merge (1st
        if firstboard[2] == firstboard[3] and firstboard[2] != 0:
                firstboard[2] = firstboard[3] * 2
                firstboard[3] = 0
            
        if firstboard[1] == firstboard[2] and firstboard[2] != 0:
                firstboard[1] = firstboard[2] * 2
                firstboard[2] = 0

        if firstboard[0] == firstboard[1] and firstboard[1] != 0:
                firstboard[0] = firstboard[1] * 2
                firstboard[1] = 0

#Second Section
        if secondboard[2] == secondboard[3] and secondboard[2] != 0:
                secondboard[2] = secondboard[3] * 2
                secondboard[3] = 0
            
        if secondboard[1] == secondboard[2] and secondboard[2] != 0:
                secondboard[1] = secondboard[2] * 2
                secondboard[2] = 0

        if [0] == secondboard[1] and secondboard[1] != 0:
                secondboard[0] = secondboard[1] * 2
                secondboard[1] = 0
#Third Section
        if thirdboard[2] == thirdboard[3] and thirdboard[2] != 0:
                thirdboard[2] = thirdboard[3] * 2
                thirdboard[3] = 0
            
        if thirdboard[1] == thirdboard[2] and thirdboard[2] != 0:
                thirdboard[1] = thirdboard[2] * 2
                thirdboard[2] = 0

        if thirdboard[0] == thirdboard[1] and thirdboard[1] != 0:
                thirdboard[0] = thirdboard[1] * 2
                thirdboard[1] = 0


#Fourth Section

        if fourthboard[2] == fourthboard[3] and fourthboard[2] != 0:
                fourthboard[2] = fourthboard[3] * 2
                fourthboard[3] = 0
            
        if fourthboard[1] == fourthboard[2] and fourthboard[2] != 0:
                fourthboard[1] = fourthboard[2] * 2
                fourthboard[2] = 0

        if fourthboard[0] == fourthboard[1] and fourthboard[1] != 0:
                fourthboard[0] = fourthboard[1] * 2
                fourthboard[1] = 0
    if keypressed == 'd':
         #Colapse (1st Section)
        if firstboard[1] == 0:
                firstboard[1] = firstboard[0]
                firstboard[0] = 0
                
        if firstboard[2] == 0:
                firstboard[2] = firstboard[1]
                firstboard[1] = 0
                
        if firstboard[3] == 0:
                firstboard[3] = firstboard[2]
                firstboard[2] = 0

    #Second Section
        if secondboard[1] == 0:
                secondboard[1] = secondboard[0]
                secondboard[0] = 0
                
        if secondboard[2] == 0:
                secondboard[2] = secondboard[1]
                secondboard[1] = 0
                
        if secondboard[3] == 0:
                secondboard[3] = secondboard[2]
                secondboard[2] = 0
               


    #third
        if thirdboard[1] == 0:
                thirdboard[1] = thirdboard[0]
                thirdboard[0] = 0
                
        if thirdboard[2] == 0:
                thirdboard[2] = thirdboard[1]
                thirdboard[1] = 0
                
        if thirdboard[3] == 0:
                thirdboard[3] = thirdboard[2]
                thirdboard[2] = 0

    #fourth
        if fourthboard[1] == 0:
                fourthboard[1] = fourthboard[0]
                fourthboard[0] = 0
                
        if fourthboard[2] == 0:
                fourthboard[2] = fourthboard[1]
                fourthboard[1] = 0
                
        if fourthboard[3] == 0:
                fourthboard[3] = fourthboard[2]
                fourthboard[2] = 0

    #Merge (1st
        if firstboard[3] == firstboard[2] and firstboard[2] != 0:
                firstboard[3] = firstboard[2] * 2
                firstboard[2] = 0
            
        if firstboard[2] == firstboard[1] and firstboard[2] != 0:
                firstboard[2] = firstboard[1] * 2
                firstboard[1] = 0

        if firstboard[1] == firstboard[0] and firstboard[1] != 0:
                firstboard[1] = firstboard[0] * 2
                firstboard[0] = 0

    #Second Section
        if secondboard[3] == secondboard[2] and secondboard[2] != 0:
                secondboard[3] = secondboard[2] * 2
                secondboard[2] = 0
            
        if secondboard[2] == secondboard[1] and secondboard[2] != 0:
                secondboard[2] = secondboard[1] * 2
                secondboard[1] = 0

        if secondboard[1] == secondboard[0] and secondboard[1] != 0:
                secondboard[1] = secondboard[0] * 2
                secondboard[0] = 0
    #Third Section
        if thirdboard[3] == thirdboard[2] and thirdboard[2] != 0:
                thirdboard[3] = thirdboard[2] * 2
                thirdboard[2] = 0
            
        if thirdboard[2] == thirdboard[1] and thirdboard[2] != 0:
                thirdboard[2] = thirdboard[1] * 2
                thirdboard[1] = 0

        if thirdboard[1] == thirdboard[0] and thirdboard[1] != 0:
                thirdboard[1] = thirdboard[0] * 2
                thirdboard[0] = 0


    #Fourth Section

        if fourthboard[3] == fourthboard[2] and fourthboard[2] != 0:
                fourthboard[3] = fourthboard[2] * 2
                fourthboard[2] = 0
            
        if fourthboard[2] == fourthboard[1] and fourthboard[2] != 0:
                fourthboard[2] = fourthboard[1] * 2
                fourthboard[1] = 0

        if fourthboard[1] == fourthboard[0] and fourthboard[1] != 0:
                fourthboard[1] = fourthboard[0] * 2
                fourthboard[0] = 0

    #Colapse (1st Section)
        if firstboard[1] == 0:
                firstboard[1] = firstboard[0]
                firstboard[0] = 0
                
        if firstboard[2] == 0:
                firstboard[2] = firstboard[1]
                firstboard[1] = 0
                
        if firstboard[3] == 0:
                firstboard[3] = firstboard[2]
                firstboard[2] = 0

    #Second Section
        if secondboard[1] == 0:
                secondboard[1] = secondboard[0]
                secondboard[0] = 0
                
        if secondboard[2] == 0:
                secondboard[2] = secondboard[1]
                secondboard[1] = 0
                
        if secondboard[3] == 0:
                secondboard[3] = secondboard[2]
                secondboard[2] = 0
               


    #third
        if thirdboard[1] == 0:
                thirdboard[1] = thirdboard[0]
                thirdboard[0] = 0
                
        if thirdboard[2] == 0:
                thirdboard[2] = thirdboard[1]
                thirdboard[1] = 0
                
        if thirdboard[3] == 0:
                thirdboard[3] = thirdboard[2]
                thirdboard[2] = 0

    
    #fourth
        if fourthboard[1] == 0:
                fourthboard[1] = fourthboard[0]
                fourthboard[0] = 0
                
        if fourthboard[2] == 0:
                fourthboard[2] = fourthboard[1]
                fourthboard[1] = 0
                
        if fourthboard[3] == 0:
                fourthboard[3] = fourthboard[2]
                fourthboard[2] = 0
    cellcreation()
    


gameupdate()

