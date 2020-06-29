# This is a cell in a Futoshiki, consisting of x, y coordinates (column and row) and a value. 
# All parameters are integers between 1..5, values can also be 0 indicating that the value is still unknown.

class cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.possibles = [1,2,3,4,5]
        self.chain=0
    
    def __str__(self):
        return str(self.val)+" "+str(self.possibles)

    def __repr__(self):
        return self.__str__()

    def setPossibles(self,pos):
        self.possibles=pos

    def getPossibles(self):
        return self.possibles

    def getPossiblesLen(self):
        return len(self.possibles)

    def getRow(self):
        return self.row
    
    def setRow(self, row):
        self.row = row
        
    def getCol(self):
        return self.col
    
    def setCol(self, col):
        self.col = col
        
    def getVal(self):
        return self.val
    
    def setVal(self, val):
        self.val = val  
        
    def clone(self): 
        return cell(self.row, self.col, self.val, self.possibles)
