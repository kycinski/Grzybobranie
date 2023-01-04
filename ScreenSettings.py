import pygame

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)
pygame.display.set_caption("Grzybobranie")
background = pygame.image.load("Grafiki/trawa.jpg")

pygame.font.init()
font = pygame.font.SysFont('comicsans', 30)

pygame.mixer.init()
music = pygame.mixer.music.load('Muzyka/music.mp3')
pygame.mixer.music.play(-1)
