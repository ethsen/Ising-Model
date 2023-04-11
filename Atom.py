import numpy as np
from Grid import Grid

class Atom():
    def __init__(self, grid):
        self.grid = grid
        self.x = np.random.randint(0, self.grid.dimension)
        self.y = np.random.randint(0,self.grid.dimension)
        self.spin = self.grid.getSpin(self.x, self.y)
        self.position = [self.x, self.y]

        self.neighbors  = self.getNeighbors()
        self.localHamiltonian = self.getLocalHamiltonian(self.neighbors)
        self.deltaH = self.getDeltaH()
        
    def move(self):
        self.x = np.random.randint(0, self.grid.dimension)
        self.y = np.random.randint(0,self.grid.dimension)
        self.spin = self.grid.getSpin(self.x, self.y)
        self.position = [self.x, self.y]
        self.getNeighbors()
        self.getLocalHamiltonian(self.neighbors)
        self.getDeltaH()

    def getNeighbors(self):
        neighbors = []

        if(self.grid.atBoundary(self.x, self.y) == False):
            neighbors.append(self.grid.getSpin(self.x-1, self.y))   # left neighbor
            neighbors.append(self.grid.getSpin(self.x+1, self.y))   # right neighbor
            neighbors.append(self.grid.getSpin(self.x, self.y-1))   # top neighbor
            neighbors.append(self.grid.getSpin(self.x, self.y+1))   # bottom neighbor

        else:
            if(self.x == self.grid.dimension -1 and self.y == self.grid.dimension -1):
                neighbors.append(self.grid.getSpin(0,self.y))
                neighbors.append(self.grid.getSpin(self.x,0))
                neighbors.append(self.grid.getSpin(self.x - 1, self. y))
                neighbors.append(self.grid.getSpin(self.x, self. y - 1))

            elif(self.x == 0 and self.y == self.grid.dimension -1):
                neighbors.append(self.grid.getSpin(self.x + 1, self.y))
                neighbors.append(self.grid.getSpin(self.grid.dimension -1 ,self.y))
                neighbors.append(self.grid.getSpin(self.x, 0))
                neighbors.append(self.grid.getSpin(self.x, self. y - 1))

            elif(self.x == self.grid.dimension -1 and self.y == 0):
                neighbors.append(self.grid.getSpin(0, self.y))
                neighbors.append(self.grid.getSpin(self.x - 1 ,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.y + 1 ))
                neighbors.append(self.grid.getSpin(self.x, self.grid.dimension -1))

            elif(self.x == 0 and self.y == 0):
                neighbors.append(self.grid.getSpin(self.x +1, self.y))
                neighbors.append(self.grid.getSpin(self.grid.dimension -1,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.y + 1 ))
                neighbors.append(self.grid.getSpin(self.x, self.grid.dimension -1))

            elif(self.x  == 0):
                neighbors.append(self.grid.getSpin(self.x +1, self.y))
                neighbors.append(self.grid.getSpin(self.grid.dimension -1,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.y + 1 ))
                neighbors.append(self.grid.getSpin(self.x, self.y -1))

            elif(self.x  == self.grid.dimension -1):
                neighbors.append(self.grid.getSpin(0, self.y))
                neighbors.append(self.grid.getSpin(self.x -1,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.y + 1 ))
                neighbors.append(self.grid.getSpin(self.x, self.y -1))

            elif(self.y  == 0):
                neighbors.append(self.grid.getSpin(self.x +1, self.y))
                neighbors.append(self.grid.getSpin(self.x -1,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.y + 1 ))
                neighbors.append(self.grid.getSpin(self.x, self.grid.dimension -1))

            elif(self.y  == self.grid.dimension -1):
                neighbors.append(self.grid.getSpin(self.x +1, self.y))
                neighbors.append(self.grid.getSpin(self.x -1,self.y))
                neighbors.append(self.grid.getSpin(self.x, self.grid.dimension -1))
                neighbors.append(self.grid.getSpin(self.x, self.y -1))

        self.neighbors = neighbors

        return neighbors
    
    def getLocalHamiltonian(self, neighbors):

        if(self.grid.field != 0):
            localHam = -1*self.grid.strength * self.spin * ((neighbors[0] + 
                                                       neighbors[1] + 
                                                       neighbors[2] +
                                                       neighbors[3]) - 4*self.grid.field)

        else:
            localHam = self.grid.strength * self.spin * (neighbors[0] + 
                                                        neighbors[1] + 
                                                        neighbors[2] +
                                                        neighbors[3])
                                                      

        self.localHamiltonian = localHam

        return localHam
    
    def getDeltaH(self):

        self.deltaH = 2*self.localHamiltonian 

        if(self.deltaH <= 0):
            self.grid.updateSpin(self.x, self.y, (-1)*self.spin)

        else:
            probablity = np.exp(-1*(self.deltaH)/self.grid.beta)
            nRand = np.random.random_sample()
            if(probablity > nRand):
                self.grid.updateSpin(self.x, self.y, (-1)*self.spin)
                
        return 2 * self.localHamiltonian
    
    def setPos(self,x,y):
        self.x = x
        self.y = y
        self.position = [x,y]
