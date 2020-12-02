import pygame
import pygame.locals

board_size = 19

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
TEAL = (0,128,128)
RED = (255, 0 , 0)

def draw_board(width, height):
	print(width, height)
	side = width
	if height < width:
		side = height
	step = side/41
	r1 = pygame.Rect((step, step, side-step*2, side-step*2))
	pygame.draw.rect(screen, WHITE, r1, 3)
	z = step*2
	b_step = (side - (step+z)*2) / board_size
	x1 = step + z
	y1 = step + z
	x2 = side - (step+z)
	
	for i in range(board_size + 1):
		pygame.draw.line(screen, WHITE, [x1, y1], [x2, y1], 1)
		y1 += b_step
	y1 = step + z
	y2 = side - (step + z)
	for i in range(board_size + 1):
		pygame.draw.line(screen, WHITE, [x1, y1], [x1, y2], 1)
		x1 += b_step
	coord_list = []
		
	pygame.draw.circle(screen, WHITE, [x2, y2], z*0.45)
	pygame.display.update()


if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode()
    surface = pygame.display.get_surface() 
    x,y = size = surface.get_width(), surface.get_height()
    screen.fill(BLACK)
    draw_board(x, y)

  
    pygame.display.flip()	
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass