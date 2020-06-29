import pygame, os, random, Futoshiki_IO, Solver
from timeit import default_timer as timer

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[480,480]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Futoshiki Solver")
 
# Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()


# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                start=timer()
                if event.key == pygame.K_t:
                    # Choose a random puzzle to solve
                    trivialpuzzle = random.choice(os.listdir("trivialpuzzles")) #change dir name if necessary
                    trivialpuzzle = "trivialpuzzles/" + trivialpuzzle
                    firstSnapshot = Futoshiki_IO.loadPuzzle(trivialpuzzle) 
                    Solver.solve(firstSnapshot, screen)
                    print(trivialpuzzle)
                    print(timer()-start)

                if event.key == pygame.K_e:
                    # Choose a random puzzle to solve
                    easypuzzle = random.choice(os.listdir("easypuzzles")) #change dir name if necessary
                    easypuzzle = "easypuzzles/" + easypuzzle
                    firstSnapshot = Futoshiki_IO.loadPuzzle(easypuzzle) 
                    Solver.solve(firstSnapshot, screen)
                    print(easypuzzle)
                    print(timer()-start)

                if event.key == pygame.K_h:
                    # Choose a random puzzle to solve
                    hardpuzzle = random.choice(os.listdir("hardpuzzles")) #change dir name if necessary
                    hardpuzzle = "hardpuzzles/" + hardpuzzle
                    firstSnapshot = Futoshiki_IO.loadPuzzle(hardpuzzle)
                    Solver.solve(firstSnapshot, screen)
                    print(hardpuzzle)
                    print(timer()-start)

                if event.key == pygame.K_s:
                    testpuzzle = random.choice(os.listdir("testing"))  # change dir name if necessary
                    testpuzzle = "testing/" + testpuzzle
                    firstSnapshot = Futoshiki_IO.loadPuzzle(testpuzzle)
                    Solver.solve(firstSnapshot, screen)
                    print(testpuzzle)
                    print(timer()-start)

                if event.key == pygame.K_a:
                    trivialpuzzles = os.listdir("trivialpuzzles")
                    trivialpuzzlesavg = 0
                    for trivialpuzzle in trivialpuzzles:
                        fname = "trivialpuzzles/" + trivialpuzzle
                        firstSnapshot = Futoshiki_IO.loadPuzzle(fname)
                        start = timer()
                        x=Solver.solve(firstSnapshot, screen)
                        end = timer()
                        print(trivialpuzzle + ": " + str(end - start),x)
                        trivialpuzzlesavg += end - start
                        # print(end-start)
                    print("trivial puzzles average: " + str(trivialpuzzlesavg / 4))

                    print()
                    print()

                    easypuzzles = os.listdir("easypuzzles")
                    easypuzzleavg = 0
                    for easypuzzle in easypuzzles:
                        fname = "easypuzzles/" + easypuzzle
                        firstSnapshot = Futoshiki_IO.loadPuzzle(fname)
                        start = timer()
                        Solver.count=0
                        x=Solver.solve(firstSnapshot, screen)
                        end = timer()
                        print(easypuzzle + ": " + str(end - start),x)
                        easypuzzleavg += end - start
                        # print(end-start)
                    print("easy puzzles average: " + str(easypuzzleavg / 4))


                    print()
                    print()

                    hardpuzzles = os.listdir("hardpuzzles")
                    hardpuzzleavg = 0
                    for hardpuzzle in hardpuzzles:
                        fname = "hardpuzzles/" + hardpuzzle
                        firstSnapshot = Futoshiki_IO.loadPuzzle(fname)
                        start = timer()
                        x = Solver.solve(firstSnapshot, screen)
                        end = timer()
                        print(hardpuzzle + ": " + str(end - start),x)
                        hardpuzzleavg += end - start
                        # print(end-start)
                    print("hard puzzles average: " + str(hardpuzzleavg / 4))

                    print()
                    print()

                    selfpuzzles = os.listdir("testing")
                    selgpuzzleavg = 0
                    for selfpuz in selfpuzzles:
                        fname = "testing/" + selfpuz
                        firstSnapshot = Futoshiki_IO.loadPuzzle(fname)
                        start = timer()
                        x = Solver.solve(firstSnapshot, screen)
                        end = timer()
                        print(selfpuz + ": " + str(end - start),x)
                        selgpuzzleavg += end - start
                        # print(end-start)
                    print("testing puzzles average: " + str(selgpuzzleavg / len(selfpuzzles)))

        # Limit to 20 frames per second
        clock.tick(10)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()