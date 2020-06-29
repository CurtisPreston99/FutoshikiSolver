# Template for the algorithm to solve a Futoshiki. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Snapshot, Cell, Futoshiki_IO

def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(200)
    Futoshiki_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()
    # if current snapshot is complete ... return a value

    # if isComplete(snapshot) and checkConsistency(snapshot):
    #    return True
    # else:
    #    return False
    
    # if current snapshot not complete ...

    # get next empty cell

    # for each value in the cells possibles list:
    #    newsnapshot = ....clone current snapshot and update the cell with the value 
    #    if new snapshot is consistent, perform recursive call to solve
    #    if checkConsistency(newsnapshot):
    #       success = solve(newsnapshot, screen)
    #       if success: return True
    
    # if we get to here no way to solve from current snapshot
    # return False

    # Check whether a snapshot is consistent, i.e. all cell values comply 
    # with the Futoshiki rules (each number occurs only once in each row and column, 
    # no "<" constraints violated). 
     
def checkConsistency(snapshot):
    return True

    # Check whether a puzzle is solved. 
    # return true if the Futoshiki is solved, false otherwise
     
def isComplete(snapshot):
    return True


