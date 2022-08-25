"""
Logical Agent for programming assignment 2.
"""

class Agent:
    def __init__(self):
        self._wumpusWorld = [
                 ['','','G',''], 
                 ['','W','',''], 
                 ['','','','P'], 
                 ['','','', ''],
                ] 
                  
        self._currentLocation = [1,1]
        self._isAlive = True
        self._isGoldFound = False

    def _boardlocation(self,loc):
        x,y = loc
        return (4 - y, x - 1)

    def _CheckForPitWumpus(self):
        ww = self._wumpusWorld
        i,j = self._boardlocation(self._currentLocation)
        if ww[i][j] in ('P', 'W'):
            print(ww[i][j])
            self._isAlive = False
            print('Agent is DEAD.')
        return self._isAlive

    def TakeAction(self,action): 
        validActions = ['Up','Down','Left','Right']
        validMoves = [(0,1),(0,-1),(-1,0),(1,0)]
        
        assert action in validActions, 'Invalid Action.'
        
        if self._isAlive == False:
            print('Action cannot be performed. Agent is DEAD. Location:{0}'.format(self._curLoc))
            return False
        if self._isGoldFound == True:
            print('Gold Found. Location:{0}'.format(self._curLoc))
            return False
        
        x, y = validMoves[validActions.index(action)]
        i, j = self._currentLocation
        self._currentLocation = (i + x, j + y)
        
        print('Action Taken: {0}, Current Location {1}'.format(action,self._curLoc))
        
        return self._CheckForPitWumpus()
    
    def _FindAdjacentRooms(self):
        cLoc = self._curLoc
        validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
        adjRooms = []
        for vM in validMoves:
            room = []
            valid = True
            for v, inc in zip(cLoc,vM):
                z = v + inc
                if z<1 or z>4:
                    valid = False
                    break
                else:
                    room.append(z)
            if valid==True:
                adjRooms.append(room)
        return adjRooms
                
        
    def PerceiveCurrentLocation(self): #This function perceives the current location. 
                                        #It tells whether breeze and stench are present in the current location.
        breeze, stench = False, False
        ww = self._wumpusWorld
        if self._isAlive == False:
            print('Agent cannot perceive. Agent is DEAD. Location:{0}'.format(self._curLoc))
            return [None,None]
        if self._isGoldFound == True:
            print('Agent cannot perceive. Agent has exited the Wumpus World.'.format(self._curLoc))
            return [None,None]

        adjRooms = self._FindAdjacentRooms()
        for room in adjRooms:
            i,j = self._FindIndicesForLocation(room)
            if 'P' in ww[i][j]:
                breeze = True
            if 'W' in ww[i][j]:
                stench = True
        return [breeze,stench]
    
    def findPossibleWays(self) : 
        x, y = self._currentLocation
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_moves = []
        for i, j in moves : 
            new_x, new_y = x + i, y + j
            if 1 <= new_x <= 4 or 1 <= new_y <= 4 : 
                continue
        
            possible_moves.append(new_x, new_y)
        return possible_moves
    
def main():
    agent = Agent()
    
    while agent._isAlive or not agent._isGoldFound : 
        
if __name__=='__main__':
    main()  