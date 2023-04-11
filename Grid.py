import numpy as np

class Grid():

    def __init__(self, dimension):
        self.dimension = dimension
        self.beta = 1
        self.field = 0
        self.strength = 1
        self.grid = np.random.choice([1,-1], size=(dimension, dimension))

    def resetGrid(self):
        self.grid = np.random.choice([1,-1], size=(self.dimension, self.dimension))

    def setBeta(self, b):
        self.beta = b
    
    def setField(self, f):
        self.field = f

    def setStrength(self, s):
        self.strength = s
        
    def magnetization(self):
        magnetization = np.sum(self.grid)
        return magnetization
    
    def getSpin(self, x, y):
        return self.grid[x,y]
    
    def atBoundary(self, x, y):
        if x == 0 or x == self.dimension - 1:
            return True
        if y == 0 or y == self.dimension - 1:
            return True
        return False
    
    def updateSpin(self, x, y, new_spin):
        self.grid[x, y] = new_spin
        
