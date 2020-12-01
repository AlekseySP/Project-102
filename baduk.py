import pygame
import pygame.locals


side = 700
screenSize = (side, side)
step = side/41

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
TEAL = (0,128,128)

def draw_board():
	r1 = pygame.Rect((step, step, side-step, side-step))
	pygame.draw.rect(screen, WHITE, r1, 3)
	z = 20
	b_step = (side - (step+z)*2) / 18
	x1 = step + z
	y1 = step + z
	x2 = side - step
	y2 = step + z
	
	for i in range(20):
		pygame.draw.line(screen, WHITE, [x1, y1], [x2, y2], 1)
		y1 += b_step
		y2 += b_step
		
	
	pygame.display.update()


if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screenSize)
    screen.fill((0, 0, 0))
    draw_board()

  
    pygame.display.flip()	
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass