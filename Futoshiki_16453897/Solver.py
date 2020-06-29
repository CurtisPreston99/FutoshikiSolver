# Template for the algorithm to solve a Futoshiki. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Snapshot, Cell, Futoshiki_IO
import random

count = 0


def updateCellPossibles(snapshot):
    constrants = snapshot.getConstraints()
    less = {}
    greater = {}
    for x in constrants:
        if (str(x[1][0]) + str(x[1][1]) in greater.keys()):
            greater[str(x[1][0]) + str(x[1][1])].append(x[0])
        else:
            greater[str(x[1][0]) + str(x[1][1])] = [x[0]]

        if (str(x[0][0]) + str(x[0][1]) in less.keys()):
            less[str(x[0][0]) + str(x[0][1])].append(x[1])
        else:
            less[str(x[0][0]) + str(x[0][1])] = [x[1]]

    # go over all cells and get possibilities
    cells = snapshot.getCells()
    for i in cells:
        for e in i:
            row = snapshot.cellsByRow(e.row)
            col = snapshot.cellsByCol(e.col)

            # get row and col numbers
            cant = []
            for cell in row:
                if not (cell.val == 0):
                    cant.append(cell.val)

            for cell in col:
                if not (cell.val == 0):
                    cant.append(cell.val)
            # remove duplicates
            cant = list(set(cant))
            # print(cant)
            # get all possibles 
            possibles = [num for num in range(1, 6) if num not in cant]
            # print(possibles)
            # constants
            pos = (e.row, e.col)

            # get max and min based on constants
            min = minVal(snapshot, e.row, e.col, greater)
            max = maxVal(snapshot, e.row, e.col, less)

            # remove the possibles values that don't fit inbetween min and max
            possiblesContrant = [p for p in possibles if p > min and p < max]
            possibles = possiblesContrant

            # getting chain lengths for greater and less
            chains = chaincheck(snapshot, e.row, e.col, less, greater)
            # print(chains)

            # remove all possibilities that are greater than the length of < chain and greater than the length of > chains
            possiblesContrant = [p for p in possibles if p >= chains[1] and p<= snapshot.rows-chains[0]]
            possibles = possiblesContrant

            # set cell possibles
            e.possibles = possibles
    return less, greater


# returns lenth of chain of < that the cell is in
def chainlen(snapshop, x, y, constraint):
    if (str(x) + str(y) in constraint.keys()):
        links = constraint[str(x) + str(y)]
        lenths = []
        for i in links:
            lenths.append(chainlen(snapshop, i[0], i[1], constraint))
        m = max(lenths)
        return m + 1
    return 0


def chaincheck(snapshop, x, y, less, greater):
    greaterLen = chainlen(snapshop, x, y, greater)
    lessLen = chainlen(snapshop, x, y, less)
    return [lessLen, greaterLen]


# get max value for a cell bassed on constraints
def maxVal(snapshot, x, y, less):
    # print(less.keys())
    # print(str(x) + str(y))
    if (str(x) + str(y) in less.keys()):
        les = less[str(x) + str(y)]
        # print("-- maxs")
        vals = []
        for i in les:
            val = snapshot.getCellVal(i[0], i[1])
            if (val > 0):
                vals.append(snapshot.getCellVal(i[0], i[1]))
        # print(vals)
        # print(min(vals))
        if (len(vals) != 0):
            men = min(vals)
            return men
    return 6


# get min value for a cell bassed on constraints
def minVal(snapshot, x, y, greater):
    # print(greater.keys())
    # print(str(x) + str(y))
    if (str(x) + str(y) in greater.keys()):
        gr8 = greater[str(x) + str(y)]
        vals = []
        # print("-- mins")
        for i in gr8:
            # print(x)
            val = snapshot.getCellVal(i[0], i[1])
            # print(val)
            vals.append(snapshot.getCellVal(i[0], i[1]))
            # print(grid[x[0]][x[1]])
        # print(vals)
        m = max(vals)
        if (m == 0):
            return 1
        else:
            return m
        # return (max(vals))

    else:
        return 0


def solve(snapshot, screen):
    # display current snapshot

    # print(snapshot)
    less, greater = updateCellPossibles(snapshot)

    pygame.time.delay(20)
    Futoshiki_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()

    if not (checkPosible(snapshot)):
        return False

    # print("check consitency")
    # checkConsistency(snapshot)
    # print("check consitency end")

    if (isComplete(snapshot, less, greater) and checkConsistency(snapshot)):
        # print(count)
        return True
    elif (isComplete(snapshot, less, greater)):
        return False
    # if current snapshot is complete ... return a value

    # if isComplete(snapshot) and checkConsistency(snapshot):
    #    return True
    # else:
    #    return False

    # if current snapshot not complete ...

    # get next empty cell
    cellsTODO = snapshot.getCellsPoss()

    # getting all cells with 1 possibility and setting them
    cells1pos = [c for c in cellsTODO if c.getPossiblesLen() == 1]
    if len(cells1pos):
        newsnapshot = snapshot.clone()
        for c in cells1pos:
            newsnapshot.setCellVal(c.row, c.col, c.getPossibles()[0])
        if (solve(newsnapshot, screen)):
            return True
        else:
            return False

    for cell in cellsTODO:
        possibles = cell.getPossibles()
        for num in cell.getPossibles():
            newsnapshot = snapshot.clone()
            newsnapshot.setCellVal(cell.row, cell.col, num)
            x = solve(newsnapshot, screen)
            if (x):
                return True
        # w=input()
        return False
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
    return False


def checkPosible(snapshot):
    cells = snapshot.getCells()
    for i in cells:
        for c in i:
            if c.val == 0:
                if (c.getPossiblesLen() == 0):
                    return False
    return True


def checkConsistency(snapshot):
    # checking rows

    for i in range(snapshot.rows):
        row=snapshot.cellsByRow(i)
        rowVal=[e.val for e in row]
        rowVal.sort()
        if not(rowVal==[1,2,3,4,5]):
            return False
    # checking colums
    for i in range(snapshot.columns):
        col=snapshot.cellsByRow(i)
        colVal=[e.val for e in col]
        colVal.sort()
        if not(colVal==[1,2,3,4,5]):
            return False

    # cheking Constraints
    #
    for i in snapshot.getConstraints():
        lowerCell=snapshot.getCell(i[0][0],i[0][1])
        upperCell=snapshot.getCell(i[1][0],i[1][1])
        # print(lowerCell,upperCell)
        if not(lowerCell==0 or upperCell==0):
            if(lowerCell.val>upperCell.val):
                return False
    return True
    # Check whether a puzzle is solved.
    # return true if the Futoshiki is solved, false otherwise


def isComplete(snapshot, less, greater):
    # check all cells are used
    cells = snapshot.getCells()
    for i in cells:
        for e in i:
            # print(e)
            if e.val == 0:
                return False

    # check snapshot is consistent
    if not(checkConsistency(snapshot)):
        return False

    return True
