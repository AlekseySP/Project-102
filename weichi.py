# Load and initialize Modules here
import pygame
import random
pygame.init()

# Window Information

displayw = 700
displayh = 700

screen = pygame.display.set_mode((displayw,displayh))
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
        self.board_size = 19
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GRAY = (128, 128, 128)
        self.BROWN = (139, 69, 19)
        self.TEAL = (0,128,128)
        self.RED = (255, 0 , 0)
        self.side = self.w
        if self.h < self.w:
            self.side = self.h
        self.step = self.side/41
        self.z = self.step*2
        self.b_step = (self.side - (self.step+self.z)*2) / (self.board_size - 1)
        self.coord_list = {}
        self.move_history = []
        self.accupied_dots = []
        self.Main()


    def draw_board(self):
        r1 = pygame.Rect((self.step, self.step, self.side-self.step*2, self.side-self.step*2))
        pygame.draw.rect(screen, self.GRAY, r1, 3)
        x1 = self.step + self.z
        y1 = self.step + self.z
        x2 = self.side - (self.step+self.z)
        y2 = self.side - (self.step + self.z)
        # coord_list = {}
        
        for v in range(self.board_size):
            pygame.draw.line(screen, self.GRAY, [x1, y1], [x1, y2], 1)
            self.coord_list[str(v)] = [x1]
            x1 += self.b_step
        
        #coord_list[str(board_size)] = [x1]
        x1 = self.step + self.z
        
        for h in range(self.board_size):
            pygame.draw.line(screen, self.GRAY, [x1, y1], [x2, y1], 1)
            self.coord_list[str(h)].append(y1)
            y1 += self.b_step
            
        pygame.draw.circle(screen, self.GRAY, self.coord_list["3"], 5)
        pygame.draw.circle(screen, self.GRAY, self.coord_list["9"], 5)
        pygame.draw.circle(screen, self.GRAY, self.coord_list["15"], 5)
        pygame.draw.circle(screen, self.GRAY, [self.coord_list["3"][0], self.coord_list["15"][1]], 5)
        pygame.draw.circle(screen, self.GRAY, [self.coord_list["15"][0], self.coord_list["3"][1]], 5)
            

    def make_move(self):
        color = random.random()
        rx = self.coord_list[str(random.randrange(self.board_size))][0]
        ry = self.coord_list[str(random.randrange(self.board_size))][1]
        coords = [rx, ry]
        if coords in self.accupied_dots:
            pass
        else:
            if color >= 0.5:
                col = self.WHITE
            else:
                col = self.BLACK
            self.accupied_dots.append([rx, ry])
            self.move_history.append([col, [rx, ry]])

    def draw_moves(self):
        if self.accupied_dots:
            for i in self.move_history:
                pygame.draw.circle(screen, i[0], i[1], self.b_step*0.45)
                pygame.draw.circle(screen, self.GRAY, i[1], self.b_step*0.45, 1)

    def Main(self):
        #Put all variables up here
        stopped = False

        while stopped == False:
            screen.fill(self.BLACK) #Tuple for filling display... Current is white
            self.draw_board()

            #Event Tasking
            #Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.make_move()
                elif event.type == pygame.KEYDOWN:
                    stopped = True


            #Add things like player updates here
            # self.make_move()
            self.draw_moves()
            #Also things like score updates or drawing additional items
            # Remember things on top get done first so they will update in the order yours is set at

            # Remember to update your clock and display at the end
            pygame.display.update()
            windowclock.tick(20)

        # If you need to reset variables here
        # This includes things like score resets

    # After your main loop throw in extra things such as a main menu or a pause menu
    # Make sure you throw them in your main loop somewhere where they can be activated by the user

# All player classes and object classes should be made outside of the main class and called inside the class
#The end of your code should look something like this
if __name__ == "__main__":
	MainRun(W, H)