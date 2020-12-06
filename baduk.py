import pygame
import pygame.locals
import random
import sys

board_size = 19

window_size = (700, 700)

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
TEAL = (0,128,128)
RED = (255, 0 , 0)

def draw_board(width, height):
	# print(width, height)
	side = width
	if height < width:
		side = height
	step = side/41
	r1 = pygame.Rect((step, step, side-step*2, side-step*2))
	pygame.draw.rect(screen, GRAY, r1, 3)
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
	
	pygame.display.update()

def draw_white_stone(pos_c):
	pygame.draw.circle(screen, WHITE, pos_c, 19)
	pygame.draw.circle(screen, GRAY, pos_c, 19, 1)

def draw_black_stone(pos_c):
	pygame.draw.circle(screen, BLACK, pos_c, 15)
	pygame.draw.circle(screen, GRAY, pos_c, 15, 1)


if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(window_size)
    surface = pygame.display.get_surface() 
    x,y = size = surface.get_width(), surface.get_height()
    screen.fill(BLACK)
    draw_board(x, y)

  
    pygame.display.flip()	
    # while pygame.event.wait().type != pygame.locals.QUIT:
    #     pass
    while 1:
	    for i in pygame.event.get():
	        if i.type == pygame.QUIT:
	            sys.exit()
	        if i.type == pygame.MOUSEBUTTONDOWN:
	            if i.button == 1:
	                draw_white_stone(i.pos)
	                pygame.display.update()
	            elif i.button == 3:
	                draw_black_stone(i.pos)
	                pygame.display.update()
	            elif i.button == 2:
	                # screen.fill(WHITE)
	                pygame.display.update()
	 
	    pygame.time.delay(20)