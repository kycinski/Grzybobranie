from pygame.locals import *

import obiekty
from character import *
from ScreenSettings import *

pygame.init()

clock = pygame.time.Clock()


def redrawGameWindow():
    screen.blit(background, (0, 0))
    for obiekt in obiekty.lista_obiektow:
        obiekt.draw(screen)
    char.draw(screen)

    pygame.display.update()


# mainloop
pygame.time.set_timer(USEREVENT, 1000)
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if char.game_over == False:
            if event.type == USEREVENT:
                obiekty.generowanieObiektu()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                obiekty.zbieranie()

    char.Sterowanie()

    redrawGameWindow()


pygame.quit()
