# Load and initialize Modules here
import pygame
import random
pygame.init()

# Window Information
board_size = 19
displayw = 800
displayh = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
TEAL = (0,128,128)
RED = (255, 0 , 0)
screen = pygame.display.set_mode()#((displayw,displayh))
surface = pygame.display.get_surface() 
W,H = size = surface.get_width(), surface.get_height()

# Clock
windowclock = pygame.time.Clock()

# Load other things such as images and sound files here
#tileset = pygame.image.load("tileset.png").convert_alpha()
# Use convert_alpha() for images with transparency

# Main Class
class MainRun(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.Main()
        
    def draw_board(self):
        side = self.w
        if self.h < self.w:
        	side = self.h
        step = side/41
        r1 = pygame.Rect((step, step, side-step*2, side-step*2))
        pygame.draw.rect(screen, (255,255,255), r1, 3)
        z = step*2
        b_step = (side - (step+z)*2) / (board_size - 1)
        x1 = step + z
        y1 = step + z
        x2 = side - (step+z)
        y2 = side - (step + z)
        coord_list = {}
        
        for v in range(board_size):
        	pygame.draw.line(screen, GRAY, [x1, y1], [x1, y2], 1)
        	coord_list[str(v)] = [x1]
        	x1 += b_step
        
        #coord_list[str(board_size)] = [x1]
        x1 = step + z
        
        for h in range(board_size):
        	pygame.draw.line(screen, GRAY, [x1, y1], [x2, y1], 1)
        	coord_list[str(h)].append(y1)
        	y1 += b_step
        	
        pygame.draw.circle(screen, GRAY, coord_list["3"], 5)
        pygame.draw.circle(screen, GRAY, coord_list["9"], 5)
        pygame.draw.circle(screen, GRAY, coord_list["15"], 5)
        pygame.draw.circle(screen, GRAY, [coord_list["3"][0], coord_list["15"][1]], 5)
        pygame.draw.circle(screen, GRAY, [coord_list["15"][0], coord_list["3"][1]], 5)
        for i in range(100):
        	color = random.random()
        	rx = coord_list[str(random.randrange(board_size))][0]
        	ry = coord_list[str(random.randrange(board_size))][1]
        	if color >= 0.5:
        		pygame.draw.circle(screen, WHITE, [rx, ry], b_step*0.45)
        		pygame.draw.circle(screen, GRAY, [rx, ry], b_step*0.45, 1)
        	else:
        		pygame.draw.circle(screen, BLACK, [rx, ry], b_step*0.45)
        		pygame.draw.circle(screen, GRAY, [rx, ry], b_step*0.45, 1)

    def Main(self):
        #Put all variables up here
        stopped = False
		
        while stopped == False:
            screen.fill(BLACK) #Tuple for filling display... Current is white
            self.draw_board()

            #Event Tasking
            #Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    stopped = True


            #Add things like player updates here
            #Also things like score updates or drawing additional items
            # Remember things on top get done first so they will update in the order yours is set at

            # Remember to update your clock and display at the end
            pygame.display.update()
            windowclock.tick(1)

        # If you need to reset variables here
        # This includes things like score resets

    # After your main loop throw in extra things such as a main menu or a pause menu
    # Make sure you throw them in your main loop somewhere where they can be activated by the user

# All player classes and object classes should be made outside of the main class and called inside the class
#The end of your code should look something like this
if __name__ == "__main__":
	MainRun(W, H)