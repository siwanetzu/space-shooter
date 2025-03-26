import pygame

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    # event loop to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    pygame.display.update()


pygame.quit()