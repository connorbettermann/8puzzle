import math

def printGoalBoard():
    print("-----Goal Board-----")
    print("\t", goalBoard[0], goalBoard[1], goalBoard[2])
    print("\t", goalBoard[3], goalBoard[4], goalBoard[5])
    print("\t", goalBoard[6], goalBoard[7], goalBoard[8])

def checkBoard(inBoard):
    for x in range(len(inBoard)):
        if(inBoard[x] != goalBoard[x]):
            return 1
    return 0

class Board:

    def __init__(self, inBoard, hScore):
        self.leftChild = None
        self.rightChild = None
        self.upChild = None
        self.downChild = None
        self.currentBoard = inBoard.copy()
        self.hScore = hScore
        self.gScore = self.checkDistG()
        self.manDist = self.checkMan()
        self.eucDist = self.checkEuc()
        self.flag = None                #0 = up, 1 = down, 2 = left, 3 = right

    def shuffleBoard(self):
        temp = [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
        print("Shuffling Board...")
        random.shuffle(temp)
        for x in range(len(temp)):
            val = temp[x]
            if(val == 0):
                self.moveLeft()
            elif(val == 1):
                self.moveUp()
            elif(val == 2):
                self.moveRight()
            elif(val == 3):
                self.moveDown()
    def printBoard(self):
        print("-----Current Board-----")
        print("\t", self.currentBoard[0], self.currentBoard[1], self.currentBoard[2])
        print("\t", self.currentBoard[3], self.currentBoard[4], self.currentBoard[5])
        print("\t", self.currentBoard[6], self.currentBoard[7], self.currentBoard[8])


    def moveRight(self):
        for x in range (8):
            if(self.currentBoard[x] == 0):
                if (x == 2 or x == 5 or x == 8):
                    #print("Move Right: Invalid move")
                    return 1
                else:
                    self.currentBoard[x] = self.currentBoard[x+1]
                    self.currentBoard[x+1] = 0
                    #print("Move Right")
                    return 0

    def moveLeft(self):
        for x in range (len(self.currentBoard)):
            if(self.currentBoard[x] == 0):
                if(x == 0 or x == 3 or x == 6):
                    #print("Move Left: Invalid move")
                    return 1
                else:
                    self.currentBoard[x] = self.currentBoard[x-1]
                    self.currentBoard[x-1] = 0
                    #print("Move Left")
                    return 0

    def moveDown(self):
        for x in range (len(self.currentBoard)):
            if(self.currentBoard[x] == 0):
                if (x == 6 or x == 7 or x == 8):
                    #print("Move Down: Invalid move")
                    return 1
                else:
                    self.currentBoard[x] = self.currentBoard[x+3]
                    self.currentBoard[x+3] = 0
                    #print("Move Down")
                    return 0

    def moveUp(self):
        for x in range (len(self.currentBoard)):
            if(self.currentBoard[x] == 0):
                if (x == 0 or x == 1 or x == 2):
                    #print("Move Up: Invalid move")
                    return 1
                else:
                    self.currentBoard[x] = self.currentBoard[x-3]
                    self.currentBoard[x-3] = 0
                    #print("Move Up")
                    return 0

    def checkDistH(self):
        return self.hScore

    def checkMan(self):
        n = 0
        val = 0
        for x in range(len(self.currentBoard)):
            if (self.currentBoard[x] != goalBoard[x]):
                if(self.currentBoard[x] == 0):
                    blank = 8 - x
                    if(blank > 2):
                        blank = blank - 2
                    if(blank > 3):
                        blank = blank - 2
                    n = n + blank
                elif(goalBoard[x] == 0):
                    temp = 9 - self.currentBoard[x]
                    if (temp > 2):
                        temp = temp - 2
                    if (temp > 3):
                        temp = temp - 2
                    n = n + temp
                else:
                    val = (abs(self.currentBoard[x] - goalBoard[x]))
                    if(val > 2):
                        val = val - 2
                    if(val > 3):
                        val = val - 2
                    if(goalBoard[x] == 7 and self.currentBoard[x] == 6): # if 6 is in the 7 position
                        val = val + 2
                    if(goalBoard[x] == 6 and self.currentBoard[x] == 7): # if 7 is in the 6 position
                        val = val + 2
                    if(goalBoard[x] == 4 and self.currentBoard[x] == 3): # if 3 is in the 4 position
                        val = val + 2
                    if(goalBoard[x] == 3 and self.currentBoard[x] == 4): # if 4 is in the 3 position
                        val = val + 2
                    n = n + val

        return n

    def checkEuc(self):
        n = 0
        for x in range(len(self.currentBoard)):
            if(self.currentBoard[x] != goalBoard[x]):
                if(self.currentBoard[x] == 0):
                    val = 8 - x
                    if(val == 1):
                        n = n + 1
                    elif(val == 2):
                        n = n + 2
                    elif(val == 3):
                        n = n + 1
                    elif(val == 4):
                        n = n + (math.sqrt(2))
                    elif(val == 5):
                        n = n + (math.sqrt(5))
                    elif(val == 6):
                        n = n + 2
                    elif(val == 7):
                        n = n + (math.sqrt(5))
                    elif(val == 8):
                        n = n + (math.sqrt(8))
                elif(self.currentBoard[x] == 1):
                    if(x == 1):
                        n = n + 1
                    elif(x == 2):
                        n = n + 2
                    elif(x == 3):
                        n = n + 1
                    elif(x == 4):
                        n = n + (math.sqrt(2))
                    elif (x == 5):
                        n = n + (math.sqrt(5))
                    elif (x == 6):
                        n = n + 2
                    elif (x == 7):
                        n = n + (math.sqrt(5))
                    elif (x == 8):
                        n = n + (math.sqrt(8))
                elif(self.currentBoard[x] == 2):
                    if (x == 0):
                        n = n + 1
                    elif (x == 2):
                        n = n + 1
                    elif (x == 3):
                        n = n + (math.sqrt(2))
                    elif (x == 4):
                        n = n + 1
                    elif (x == 5):
                        n = n + (math.sqrt(2))
                    elif (x == 6):
                        n = n + (math.sqrt(5))
                    elif (x == 7):
                        n = n + 2
                    elif (x == 8):
                        n = n + (math.sqrt(5))
                elif(self.currentBoard[x] == 3):
                    if (x == 0):
                        n = n + 2
                    elif (x == 1):
                        n = n + 1
                    elif (x == 3):
                        n = n + (math.sqrt(5))
                    elif (x == 4):
                        n = n + (math.sqrt(2))
                    elif (x == 5):
                        n = n + 1
                    elif (x == 6):
                        n = n + (math.sqrt(8))
                    elif (x == 7):
                        n = n + (math.sqrt(5))
                    elif (x == 8):
                        n = n + 2
                elif (self.currentBoard[x] == 4):
                    if (x == 0):
                        n = n + 1
                    elif (x == 1):
                        n = n + (math.sqrt(2))
                    elif (x == 2):
                        n = n + (math.sqrt(5))
                    elif (x == 4):
                        n = n + 1
                    elif (x == 5):
                        n = n + 2
                    elif (x == 6):
                        n = n + 1
                    elif (x == 7):
                        n = n + (math.sqrt(2))
                    elif (x == 8):
                        n = n + (math.sqrt(5))
                elif (self.currentBoard[x] == 5):
                    if (x == 0):
                        n = n + (math.sqrt(2))
                    elif (x == 1):
                        n = n + 1
                    elif (x == 2):
                        n = n + (math.sqrt(2))
                    elif (x == 3):
                        n = n + 1
                    elif (x == 5):
                        n = n + 1
                    elif (x == 6):
                        n = n + (math.sqrt(2))
                    elif (x == 7):
                        n = n + 1
                    elif (x == 8):
                        n = n + (math.sqrt(2))
                elif (self.currentBoard[x] == 6):
                    if (x == 0):
                        n = n + (math.sqrt(5))
                    elif (x == 1):
                        n = n + (math.sqrt(2))
                    elif (x == 2):
                        n = n + 1
                    elif (x == 3):
                        n = n + 2
                    elif (x == 4):
                        n = n + 1
                    elif (x == 6):
                        n = n + (math.sqrt(5))
                    elif (x == 7):
                        n = n + (math.sqrt(2))
                    elif (x == 8):
                        n = n + 1
                elif (self.currentBoard[x] == 7):
                    if (x == 0):
                        n = n + 2
                    elif (x == 1):
                        n = n + (math.sqrt(5))
                    elif (x == 2):
                        n = n + (math.sqrt(8))
                    elif (x == 3):
                        n = n + 1
                    elif (x == 4):
                        n = n + (math.sqrt(2))
                    elif (x == 5):
                        n = n + (math.sqrt(5))
                    elif (x == 7):
                        n = n + 1
                    elif (x == 8):
                        n = n + 2
                elif (self.currentBoard[x] == 8):
                    if (x == 0):
                        n = n + (math.sqrt(5))
                    elif (x == 1):
                        n = n + 2
                    elif (x == 2):
                        n = n + (math.sqrt(5))
                    elif (x == 3):
                        n = n + (math.sqrt(2))
                    elif (x == 4):
                        n = n + 1
                    elif (x == 5):
                        n = n + (math.sqrt(2))
                    elif (x == 6):
                        n = n + 1
                    elif (x == 8):
                        n = n + 1
        return n

    def getMan(self):
        print("Manhattan: ", self.manDist)
        return
    def getEuc(self):
        print("Euclidian: ", self.eucDist)
        return

    def checkDistG(self):
        g = 0
        for x in range (len(self.currentBoard)):
            if(self.currentBoard[x] != goalBoard[x]):
                g = g + 1
        return g

    def getDistF(self):
        val = self.checkDistG() + self.checkDistH()
        return val
    def getDistFM(self):
        return self.checkDistH() + self.checkMan()
    def getDistFE(self):
        return self.checkEuc() + self.checkDistH()

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def getUp(self):
        return self.upChild

    def getDown(self):
        return self.downChild

    def bestMis(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        right.printBoard()
        up = Board(self.currentBoard, self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", up.checkDistG(), "\nDOWN: ", down.checkDistG(), "\nLEFT: ", left.checkDistG(), "\nRIGHT: ",
              right.checkDistG())

        if (checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Misplaced Tiles: ", up.hScore, " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Misplaced Tiles: ", down.hScore, " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Misplaced Tiles: ", left.hScore, " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Misplaced Tiles: ", right.hScore, " iterations to complete")
            return 0

        if (u == 1):
            up.gScore = 999
        if (d == 1):
            down.gScore = 999
        if (l == 1):
            left.gScore = 999
        if (r == 1):
            right.gScore = 999

        if (up.checkDistG() <= down.checkDistG() and up.checkDistG() <= left.checkDistG() and up.checkDistG() <= right.checkDistG()):
            if ((self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.bestMis()
        if (down.checkDistG() <= up.checkDistG() and down.checkDistG() <= left.checkDistG()and down.checkDistG() <= right.checkDistG()):
            if ((self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.bestMis()
        if (left.checkDistG() <= down.checkDistG() and left.checkDistG() <= up.checkDistG() and left.checkDistG() <= right.checkDistG()):
            if ((self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.bestMis()
        if (right.checkDistG() <= down.checkDistG() and right.checkDistG() <= left.checkDistG() and right.checkDistG()<= up.checkDistG()):
            if ((self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.bestMis()

    def setChildren(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        #left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        #right.printBoard()
        up = Board(self.currentBoard,self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        #up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        #down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", up.getDistF(), "\nDOWN: ", down.getDistF(), "\nLEFT: ", left.getDistF(), "\nRIGHT: ", right.getDistF())


        if(checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Misplaced Tiles: ", up.getDistF(), " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Misplaced Tiles: ", down.getDistF(), " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Misplaced Tiles: ", left.getDistF(), " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Misplaced Tiles: ", right.getDistF(), " iterations to complete")
            return 0

        if(u == 1):
            up.gScore = 999
        if(d == 1):
            down.gScore = 999
        if(l == 1):
            left.gScore = 999
        if(r == 1):
            right.gScore = 999

        if(up.getDistF() <= down.getDistF() and up.getDistF() <= left.getDistF() and up.getDistF() <= right.getDistF()):
            if((u == 0) and (self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.setChildren()
        if (down.getDistF() <= up.getDistF() and down.getDistF() <= left.getDistF() and down.getDistF() <= right.getDistF()):
            if((d == 0) and (self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.setChildren()
        if (left.getDistF() <= down.getDistF() and left.getDistF() <= up.getDistF() and left.getDistF() <= right.getDistF()):
            if((l == 0) and (self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.setChildren()
        if (right.getDistF() <= down.getDistF() and right.getDistF() <= left.getDistF() and right.getDistF() <= up.getDistF()):
            if((r == 0)and (self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.setChildren()

    def bestMan(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        #left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        #right.printBoard()
        up = Board(self.currentBoard, self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        #up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        #down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", up.checkMan(), "\nDOWN: ", down.checkMan(), "\nLEFT: ", left.checkMan(), "\nRIGHT: ",
              right.checkMan())

        if (checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Manhattan: ", up.hScore, " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Manhattan: ", down.hScore, " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Manhattan: ", left.hScore, " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Manhattan: ", right.hScore, " iterations to complete")
            return 0

        if (u == 1):
            up.gScore = 999
        if (d == 1):
            down.gScore = 999
        if (l == 1):
            left.gScore = 999
        if (r == 1):
            right.gScore = 999

        if (up.checkMan() <= down.checkMan() and up.checkMan() <= left.checkMan() and up.checkMan() <= right.checkMan()):
            if ((self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.bestMan()
        if (down.checkMan() <= up.checkMan() and down.checkMan() <= left.checkMan() and down.checkMan() <= right.checkMan()):
            if ((self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.bestMan()
        if (left.checkMan() <= down.checkMan() and left.checkMan() <= up.checkMan() and left.checkMan() <= right.checkMan()):
            if ((self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.bestMan()
        if (right.checkMan() <= down.checkMan() and right.checkMan() <= left.checkMan() and right.checkMan() <= up.checkMan()):
            if ((self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.bestMan()

    def setChildrenMan(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        #left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        #right.printBoard()
        up = Board(self.currentBoard, self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        #up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        #down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", (up.checkMan() + up.hScore), "\nDOWN: ", (down.checkMan() + down.hScore), "\nLEFT: ", (left.checkMan() + left.hScore), "\nRIGHT: ",
              (right.checkMan() + right.hScore))
        if (checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Manhattan: ", up.hScore, " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Manhattan: ", down.hScore, " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Manhattan: ", left.hScore, " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Manhattan: ", right.hScore, " iterations to complete")
            return 0

        if (u == 1):
            up.manDist = 999
        if (d == 1):
            down.manDist = 999
        if (l == 1):
            left.manDist = 999
        if (r == 1):
            right.manDist = 999


        if (up.getDistFM() <= down.getDistFM() and up.getDistFM() <= left.getDistFM() and up.getDistFM() <= right.getDistFM()): #need to ignore values that are unchanged
            if ((u == 0) and (self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.getMan()
                up.setChildrenMan()
        if (down.getDistFM() <= up.getDistFM() and down.getDistFM() <= left.getDistFM() and down.getDistFM() <= right.getDistFM()):
            if ((d == 0) and (self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.getMan()
                down.setChildrenMan()
        if (left.getDistFM() <= down.getDistFM() and left.getDistFM() <= up.getDistFM() and left.getDistFM() <= right.getDistFM()):
            if ((l == 0) and (self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.getMan()
                left.setChildrenMan()
        if (right.getDistFM() <= down.getDistFM() and right.getDistFM() <= left.getDistFM() and right.getDistFM() <= up.getDistFM()):
            if ((r == 0) and (self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.getMan()
                right.setChildrenMan()

    def bestEuc(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        #left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        #right.printBoard()
        up = Board(self.currentBoard, self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        #up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        #down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", up.checkEuc(), "\nDOWN: ", down.checkEuc(), "\nLEFT: ", left.checkEuc(), "\nRIGHT: ",
              right.checkEuc())

        if (checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Euclidian: ", up.hScore, " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Euclidian: ", down.hScore, " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Euclidian: ", left.hScore, " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Euclidian: ", right.hScore, " iterations to complete")
            return 0

        if (u == 1):
            up.gScore = 999
        if (d == 1):
            down.gScore = 999
        if (l == 1):
            left.gScore = 999
        if (r == 1):
            right.gScore = 999

        if (up.checkEuc() <= down.checkEuc() and up.checkEuc() <= left.checkEuc() and up.checkEuc() <= right.checkEuc()):
            if (u == 0 and (self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.bestEuc()
        if (down.checkEuc() <= up.checkEuc() and down.checkEuc() <= left.checkEuc() and down.checkEuc() <= right.checkEuc()):
            if (d == 0 and (self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.bestEuc()
        if (left.checkEuc() <= down.checkEuc() and left.checkEuc() <= up.checkEuc() and left.checkEuc() <= right.checkEuc()):
            if (l == 0 and (self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.bestEuc()
        if (right.checkEuc() <= down.checkEuc() and right.checkEuc() <= left.checkEuc() and right.checkEuc() <= up.checkEuc()):
            if (r == 0 and (self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.bestEuc()

    def setChildrenEuc(self):
        left = Board(self.currentBoard, self.hScore + 1)
        left.flag = 2
        l = left.moveLeft()
        #left.printBoard()
        right = Board(self.currentBoard, self.hScore + 1)
        right.flag = 3
        r = right.moveRight()
        #right.printBoard()
        up = Board(self.currentBoard, self.hScore + 1)
        up.flag = 0
        u = up.moveUp()
        #up.printBoard()
        down = Board(self.currentBoard, self.hScore + 1)
        down.flag = 1
        d = down.moveDown()
        #down.printBoard()
        self.leftChild = left
        self.rightChild = right
        self.upChild = up
        self.downChild = down
        print("UP: ", (up.checkEuc() + up.hScore), "\nDOWN: ", (down.checkEuc() + down.hScore), "\nLEFT: ",
              (left.checkEuc() + left.hScore), "\nRIGHT: ",
              (right.checkEuc() + right.hScore))
        if (checkBoard(up.currentBoard) == 0):
            print("\nSolution Found!!!!!")
            up.printBoard()
            print("Euclidian: ", up.hScore, " iterations to complete")
            return 0
        if (checkBoard(down.currentBoard) == 0):
            print("Solution Found!!!!!")
            down.printBoard()
            print("Euclidian: ", down.hScore, " iterations to complete")
            return 0
        if (checkBoard(left.currentBoard) == 0):
            print("Solution Found!!!!!")
            left.printBoard()
            print("Euclidian: ", left.hScore, " iterations to complete")
            return 0
        if (checkBoard(right.currentBoard) == 0):
            print("Solution Found!!!!!")
            right.printBoard()
            print("Euclidian: ", right.hScore, " iterations to complete")
            return 0

        if (u == 1):
            up.eucDist = 999
        if (d == 1):
            down.eucDist = 999
        if (l == 1):
            left.eucDist = 999
        if (r == 1):
            right.eucDist = 999

        if (up.getDistFE() <= down.getDistFE() and up.getDistFE() <= left.getDistFE() and up.getDistFE() <= right.getDistFE()):
           if (u == 0 and (self.flag != 1)):
                print("XXXXXChild SelectedXXXXX")
                up.printBoard()
                up.getEuc()
                up.setChildrenEuc()
        if (down.getDistFE() <= up.getDistFE() and down.getDistFE() <= left.getDistFE() and down.getDistFE() <= right.getDistFE()):
           if (d == 0 and (self.flag != 0)):
                print("XXXXXChild SelectedXXXXX")
                down.printBoard()
                down.getEuc()
                down.setChildrenEuc()
        if (left.getDistFE() <= down.getDistFE() and left.getDistFE() <= up.getDistFE() and left.getDistFE() <= right.getDistFE()):
            if (l == 0 and (self.flag != 3)):
                print("XXXXXChild SelectedXXXXX")
                left.printBoard()
                left.getEuc()
                left.setChildrenEuc()
        if (right.getDistFE() <= down.getDistFE() and right.getDistFE() <= left.getDistFE() and right.getDistFE() <= up.getDistFE()):
           if (r == 0 and (self.flag != 2)):
                print("XXXXXChild SelectedXXXXX")
                right.printBoard()
                right.getEuc()
                right.setChildrenEuc()


goalBoard = [1,2,3,4,5,6,7,8,0]
myBoard = [4,1,2,5,8,3,7,0,6]

x = Board(myBoard, 0)
y = x
z = x
print("\n\nMISPLACED TILES")
x.printBoard()
x.setChildren()
print("\n\nMANHATTAN")
y.printBoard()
y.setChildrenMan()
print("\n\nEUCLIDIAN")
z.printBoard()
z.setChildrenEuc()

myBoard = [2,0,3,1,7,5,8,4,6]

x = Board(myBoard, 0)
y = x
z = x
print("\n\nMISPLACED TILES")
x.printBoard()
x.setChildren()
print("\n\nMANHATTAN")
y.printBoard()
y.setChildrenMan()
print("\n\nEUCLIDIAN")
z.printBoard()
z.setChildrenEuc()

myBoard = [1,3,6,5,2,0,4,7,8]

x = Board(myBoard, 0)
y = x
z = x
print("\n\nMISPLACED TILES")
x.printBoard()
x.setChildren()
print("\n\nMANHATTAN")
y.printBoard()
y.setChildrenMan()
print("\n\nEUCLIDIAN")
z.printBoard()
z.setChildrenEuc()

myBoard = [1,0,2,4,6,3,7,5,8]

x = Board(myBoard, 0)
y = x
z = x
print("\n\nMISPLACED TILES")
x.printBoard()
x.setChildren()
print("\n\nMANHATTAN")
y.printBoard()
y.setChildrenMan()
print("\n\nEUCLIDIAN")
z.printBoard()
z.setChildrenEuc()

myBoard = [1,2,3,4,8,5,0,7,6]

x = Board(myBoard, 0)
y = x
z = x
print("\n\nMISPLACED TILES")
x.printBoard()
x.setChildren()
print("\n\nMANHATTAN")
y.printBoard()
y.setChildrenMan()
print("\n\nEUCLIDIAN")
z.printBoard()
z.setChildrenEuc()

