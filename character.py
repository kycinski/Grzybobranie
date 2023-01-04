import pygame
from ScreenSettings import screenHeight, screenWidth, font

walkRight = pygame.image.load("Grafiki/PRAWO.png")
walkLeft = pygame.image.load("Grafiki/LEWO.png")
life = pygame.image.load("Grafiki/life.png")
knife_icon = pygame.image.load("Grafiki/knife.png")
knife_icon = pygame.transform.scale(knife_icon, (32, 32))


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.koszyk = 0
        self.life = 3
        self.halucyn_mode = False
        self.knife_mode = False
        self.game_over = False

    def utrata_zycia(self):
        if self.life > 0:
            self.life -= 1
            if self.life == 0:
                self.game_over = True

    def draw(self, screen):
        if self.right:
            screen.blit(walkRight, (self.x, self.y))
        elif self.left:
            screen.blit(walkLeft, (self.x, self.y))
        else:
            screen.blit(walkRight, (self.x, self.y))
        koszyk = font.render(("Koszyk: " + str(self.koszyk)), 1, (255, 255, 255))
        screen.blit(koszyk, (5, screenHeight - 30))

        if self.life == 3:
            screen.blit(life, (screenWidth - 32, screenHeight - 32))
            screen.blit(life, (screenWidth - 2*32, screenHeight - 32))
            screen.blit(life, (screenWidth - 3*32, screenHeight - 32))
        elif self.life == 2:
            screen.blit(life, (screenWidth - 32, screenHeight - 32))
            screen.blit(life, (screenWidth - 2*32, screenHeight - 32))
        elif self.life == 1:
            screen.blit(life, (screenWidth - 32, screenHeight - 32))

        if self.knife_mode == True:
            screen.blit(knife_icon, (screenWidth - 32, screenHeight - 64))

        you_lose = font.render("GAME OVER", 1, (255, 0, 0))
        you_lose_rect = you_lose.get_rect(center=(screenWidth/2, screenHeight/2))
        if self.life == 0:
            screen.blit(you_lose, you_lose_rect)

        you_win = font.render("WYGRAŁEŚ", 1, (255, 0, 0))
        you_win_rect = you_win.get_rect(center=(screenWidth / 2, screenHeight / 2))
        if self.koszyk == 5:
            screen.blit(you_win, you_win_rect)
            self.game_over = True

    def Sterowanie(self):
        keys = pygame.key.get_pressed()

        if self.halucyn_mode == False:

            if keys[pygame.K_LEFT] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
            if keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.vel:
                self.x += self.vel
                self.left = False
                self.right = True
            if keys[pygame.K_UP] and self.y > self.vel:
                self.y -= self.vel
            if keys[pygame.K_DOWN] and self.y < screenHeight - self.height - self.vel:
                self.y += self.vel

        else:

            if keys[pygame.K_RIGHT] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
            if keys[pygame.K_LEFT] and self.x < screenWidth - self.width - self.vel:
                self.x += self.vel
                self.left = False
                self.right = True
            if keys[pygame.K_DOWN] and self.y > self.vel:
                self.y -= self.vel
            if keys[pygame.K_UP] and self.y < screenHeight - self.height - self.vel:
                self.y += self.vel


char = Player(400, 500, 47, 76)
