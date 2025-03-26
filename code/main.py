import pygame

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pygame window")
clock = pygame.time.Clock()
running = True

while running:
    # event loop to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # draw the game

    display_surface.fill(('red'))  # RGB values for red

    pygame.display.set_caption('Space Cadet')
    
    pygame.display.flip()  # apparently more efficient than update()
    
    clock.tick(60)  # Limiting to 60 FPS

