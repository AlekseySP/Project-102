import pygame
import pygame.locals

def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    screen.fill((0, 0, 0))
    table = load_tile_table("tileset.png", 16, 16)
    sheet = pygame.image.load('tileset.png')
    pygame.transform.scale2x(sheet)
    tiles = strip_from_sheet(sheet, (0,0), (16,16), 16, 16)
    player = tiles[2]
    screen.blit(player, screen.get_rect().center)
  
    pygame.display.flip()	
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass