import pygame
import pygame.locals
import sys
import random

side = 700
screenSize = (side, side)
step = 25

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

color_list = [GREEN, LIME, OLIVE]

def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames

def draw_map(tl):
    tiles_dict = {
        "empty": tl[0],
        "face": tl[1],
        "halmet": tl[2],
        "small_tree": tl[3]}
 
obj_dict = {
   	"flower": ["*", YELLOW],
   	"trunk": ["o", BROWN],
   	"berry": ["•", RED]
}
  
grass_list = ["'", ",", ".", " ", "_", "/", ";", "-"] 
  
def show_all(tile_list):
    x = 8
    y = 0
    tile_number = int(screenSize[0]/step) * int(screenSize[1]/step)
    for i in range(tile_number):
        myfont = pygame.font.SysFont('Comic Sans MS', int(step * 1.6))
        if random.random() <= 0.95:
        	textsurface = myfont.render(random.choice(grass_list), False, random.choice(color_list))
        else: 
        	textsurface = myfont.render("o", False, BROWN)

        screen.blit(textsurface, (x, y))
        x += step
        if x >= screenSize[0]:
            x = 8
            y += step


if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screenSize)
    screen.fill((0, 0, 0))
    # table = load_tile_table("tileset.png", 16, 16)
    sheet = pygame.image.load('tileset.png')
    # pygame.transform.scale2x(sheet)
    tiles = strip_from_sheet(sheet, (0,0), (16,16), 16, 16)
    # player = tiles[2]
    # screen.blit(player, screen.get_rect().center)
    show_all(tiles)

  
    pygame.display.flip()	
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass