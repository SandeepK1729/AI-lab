"""
Logical Agent for programming assignment 2.
"""
from random import choice

class Agent:
    def __init__(self):
        self._wumpusWorld = [
                 ['','','G',''], 
                 ['','W','',''], 
                 ['','','','P'], 
                 ['','','', ''],
                ] 
                  
        self._currentLocation = (1,1)
        self._isAlive = True
        self.actionDict = {
            'left' : (-1, 0), 
            'right' : (1, 0), 
            'top'   : (0, 1), 
            'down'  : (0, -1)
        }
        
    @property
    def _isGoldFound(self):
        x, y = self._boardlocation(self._currentLocation)
        return self._wumpusWorld[x][y] == 'G'
    
    def _boardlocation(self,loc):
        x,y = loc
        return (4 - y, x - 1)
       
    def takeAction(self, action):
           x, y = self._currentLocation
           i, j = action
           
           self._currentLocation = (x + i, y + j)
           print(f"wampus moved from {(x, y)} to {self._currentLocation}")
           
    def findPossibleWays(self) : 
        x, y = self._currentLocation
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_moves = []
        for move, ordinates in self.actionDict.items(): 
            i, j = ordinates
            new_x, new_y = x + i, y + j
            if not (1 <= new_x <= 4 and 1 <= new_y <= 4) : 
                continue
            if self._wumpusWorld[i][j] in ('P', 'W'):
                continue
            
            possible_moves.append((i, j))
        return possible_moves
    
def main():
    agent = Agent()
    
    while agent._isAlive or not agent._isGoldFound :
        actions = agent.findPossibleWays()
        print(actions)
        action = choice(agent.findPossibleWays())
        agent.takeAction(action)
    
    if agent._isGoldFound:
        print(f"Gold Found at {self._currentLocation}")
    
if __name__=='__main__':
    main()  