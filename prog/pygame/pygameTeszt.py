import sys
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jatek :)")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


ground_surface = pygame.image.load('pygame\img\ground.png').convert_alpha()
sky_surface = pygame.image.load('pygame/img/Sky.png').convert_alpha()
text_surface = test_font.render("MyGame", False, 'black')

snail_surface = pygame.image.load(
    'pygame\img\snail1.png', "csiga").convert_alpha()
snail_x_pos = WIDTH-30
snail_rect = snail_surface.get_rect(midbottom=(snail_x_pos, HEIGHT-100))

player_surface = pygame.image.load(
    'pygame\img\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, HEIGHT-100))
player_appearence = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, HEIGHT-100))


    snail_x_pos -= 4
    if snail_x_pos < -30:
        snail_x_pos = WIDTH-30
    screen.blit(snail_surface, (snail_x_pos, HEIGHT-130))

    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)
