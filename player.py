from mappa import mappa_bigger as mappa

from icecream import ic
from typing import Callable

#LAYER: X
#INDEX: Y

#[1, 1, 1, 1, 1, P] Y = 0
# 0  1  2  3  4  5  X = 5

class Player:
    def __init__(self, mappa:list[list[1,0]], coords:tuple[int, int], target=None, when_target_found_place_at_start=False):

        if target is None:
            raise ValueError("You have to specify a target")

        self.target_found = False
        self.moves : list[Callable] = []
        self.places : list[tuple[int, int]] = []

        self.map = mappa
        self.coords = coords
        self.target = target
        self.when_target_found_place_at_start = when_target_found_place_at_start

        self.mapLenght = len(self.map)
        self.layerLenght = len(self.map[0])
        self.directions = [self.moveUp, self.moveDown, self.moveLeft, self.moveRight]
        self.directions_inverted = {
            self.moveUp    : self.moveDown,
            self.moveDown  : self.moveUp,
            self.moveLeft  : self.moveRight,
            self.moveRight : self.moveLeft
        }

        self.playerIndex = self.coords[0]
        self.layerIndex =  self.coords[1]

        self.precedentValue = self.map[self.layerIndex][self.playerIndex]

        self.map[self.layerIndex][self.playerIndex] = self
    
    def __str__(self):
        return "P"
    
    def printMap(self):
        for layer in self.map[::]:
            print(list(map(str, layer[::])))
    
    def checkUp(self):
        return bool(self.layerIndex)
    
    def checkDown(self):
        return self.layerIndex+1 < self.mapLenght
    
    def checkLeft(self):
        return bool(self.playerIndex)
    
    def checkRight(self):
        return self.playerIndex+1 < self.layerLenght
    
    def getUp(self):
        if not self.checkUp():
            return None, None, None
        upperLayerIndex = self.layerIndex-1
        upperLayer = self.map[upperLayerIndex]
        left =   None if not(self.checkLeft())  else upperLayer[self.playerIndex-1]
        center = None if not(self.checkUp())    else upperLayer[self.playerIndex]
        right =  None if not(self.checkRight()) else upperLayer[self.playerIndex+1]
        res = left, center, right
        return res
    
    def getDown(self):
        if not self.checkDown():
            return None, None, None
        lowerLayerIndex = self.layerIndex+1
        lowerLayer = self.map[lowerLayerIndex]
        left =   None if not(self.checkLeft())  else lowerLayer[self.playerIndex-1]
        center = None if not(self.checkDown())  else lowerLayer[self.playerIndex]
        right =  None if not(self.checkRight()) else lowerLayer[self.playerIndex+1]
        res = left, center, right
        return res
    
    def getLeft(self):
        if not self.checkLeft():
            return None, None, None
        left =   None if not(self.checkLeft()) or not(self.checkUp()) else self.map[self.layerIndex-1][self.playerIndex-1]
        center = None if not(self.checkLeft()) else self.map[self.layerIndex][self.playerIndex-1]
        right =  None if not(self.checkLeft()) or not(self.checkDown()) else self.map[self.layerIndex+1][self.playerIndex-1]
        res = left, center, right
        return res
    
    def getRight(self):
        if not self.checkRight():
            return None, None, None
        left =   None if not(self.checkRight()) or not(self.checkUp()) else self.map[self.layerIndex-1][self.playerIndex+1]
        center = None if not(self.checkRight()) else self.map[self.layerIndex][self.playerIndex+1]
        right =  None if not(self.checkRight()) or not(self.checkDown()) else self.map[self.layerIndex+1][self.playerIndex+1]
        res = left, center, right
        return res
    
    def surrounding(self):
        return {
            "up"    : self.getUp(),
            "down"  : self.getDown(),
            "left"  : self.getLeft(),
            "right" : self.getRight()
        }
    
    def getCross(self):
        return self.getUp()[1], self.getDown()[1], self.getLeft()[1], self.getRight()[1]

    def getCoords(self):
        return [self.playerIndex,self.layerIndex]
    
    def calculateNextCoords(self, move):
        coords = self.getCoords()
        if move == self.moveUp:
            coords[1] -= 1
        elif move == self.moveDown:
            coords[1] += 1
        elif move == self.moveLeft:
            coords[0] -= 1
        elif move == self.moveRight:
            coords[0] += 1
        return coords
    
    def place(self, x, y, placehold=None):
        layer = x
        index = y
        if placehold is None:
            placehold = self.precedentValue
        self.map[self.layerIndex][self.playerIndex] = placehold
        self.map[layer][index] = self

        self.playerIndex = index
        self.layerIndex = layer

    def moveUp(self):
        if self.layerIndex:
            self.map[self.layerIndex][self.playerIndex] = self.precedentValue
            self.precedentValue = self.map[self.layerIndex-1][self.playerIndex]
            self.map[self.layerIndex-1][self.playerIndex] = self
            self.layerIndex-=1
            self.moves.append(self.moveUp)
            self.places.append(self.getCoords())
            return "up"

    def moveDown(self):
        if not(self.layerIndex+1 >= len(self.map)):
            self.map[self.layerIndex][self.playerIndex] = self.precedentValue
            self.precedentValue = self.map[self.layerIndex+1][self.playerIndex]
            self.map[self.layerIndex+1][self.playerIndex] = self
            self.layerIndex += 1
            self.moves.append(self.moveDown)
            self.places.append(self.getCoords())
            return "down"

    def moveRight(self):
        if not(self.playerIndex+1 >= len(self.map[self.layerIndex])):
            self.map[self.layerIndex][self.playerIndex] = self.precedentValue
            self.precedentValue = self.map[self.layerIndex][self.playerIndex+1]
            self.map[self.layerIndex][self.playerIndex+1] = self
            self.playerIndex += 1
            self.moves.append(self.moveRight)
            self.places.append(self.getCoords())
            return "right"

    def moveLeft(self):
        if self.playerIndex:
            self.map[self.layerIndex][self.playerIndex] = self.precedentValue
            self.precedentValue = self.map[self.layerIndex][self.playerIndex-1]
            self.map[self.layerIndex][self.playerIndex-1] = self
            self.playerIndex -=1
            self.moves.append(self.moveLeft)
            self.places.append(self.getCoords())
            return "left"
        
    def reverse(self):
        return [ self.directions_inverted[move] for move in self.moves]


    def nextMove(self):
        cross = self.getCross() #up, down, left, right
        zeros = cross.count(0)

        if self.precedentValue == self.target:
            self.precedentValue = 0
            self.target_found = True
            return None
        
        if self.target_found:
            if self.when_target_found_place_at_start:
                self.place(*self.coords)
            self.target_found = False
            return None

        if self.target in cross:
            move = cross.index(self.target)
            return self.directions[move]

        if not zeros:
            return None
        
        elif zeros == 1:
            move = cross.index(0)
            func = self.directions[move]
            return func
        
        elif zeros > 1:
            direction = cross.index(0)
            nextCoords = self.calculateNextCoords(self.directions[direction])
            while nextCoords in self.places:
                try:
                    direction = cross.index(0, direction+1)
                    return self.directions[direction]
                except ValueError:
                    print("Value Error")
                    return None
            else:
                return self.directions[direction]

if __name__ == "__main__":
    player = Player(mappa, (0,0))
    nm = player.nextMove()
    while not nm is None:
        nm()
        nm = player.nextMove()
        player.printMap()
        print()
    else:
        print("I'M COOKED")
        print(player.getCross())