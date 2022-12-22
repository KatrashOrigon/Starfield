import pygame
import random

"""
	Rain.
"""


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
NUM_DROPS = 300
Z_MAX = 300


def spawn_drop():
	x = random.randint(0, SCREEN_WIDTH)
	y = random.randint(-300, 0)
	z = random.randint(30, Z_MAX)
	return [x, y, z]


def get_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True


def main():
	looping = False
	drops_list = []
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
		
	pygame.init()
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Rain")
	clock = pygame.time.Clock()
	
	for i in range(NUM_DROPS):
		drops_list.append(spawn_drop())
	# ---------- Main Loop ----------
	while not looping:
		# Get events.
		looping = get_events()
		# Update drops positions.
		screen.fill(BLACK)
		for i in range(NUM_DROPS):
			y = drops_list[i][1]
			py = y
			y = y + drops_list[i][2] / 100
			if y >= SCREEN_HEIGHT:
				drops_list[i] = spawn_drop()
			else:
				drops_list[i][1] = y
				z = drops_list[i][2]
				if z > 150: z = 150
				pygame.draw.line(screen, (z,z,z), (drops_list[i][0], drops_list[i][1]), (drops_list[i][0], py), round(drops_list[i][2]/100))
		# Update screen.
		clock.tick(60)
		pygame.display.flip()
	pygame.quit()


if __name__ == "__main__":
    main()
