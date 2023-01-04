import random
from character import *
from abc import ABC, abstractmethod

grzybjadalny_img = pygame.image.load("Grafiki/grzybjadalny.png")
muchomor_img = pygame.image.load("Grafiki/muchomor.png")
halucyn_img = pygame.image.load("Grafiki/halucyn.png")
odtrutka_img = pygame.image.load("Grafiki/odtrutka_na_halucyna.png")
knife_img = pygame.image.load("Grafiki/knife.png")

zebranieSound = pygame.mixer.Sound("Muzyka/slap.wav")

lista_obiektow = []


class Obiekty(ABC):
    def __init__(self, width, height):
        self.x = random.randint(0, screenWidth - width)
        self.y = random.randint(0, screenHeight - height)
        self.width = width
        self.height = height
        self.alive = True
        self.armor = 3

    def hit(self):
        if self.alive == True:
            self.armor -= 1
            if char.knife_mode == True and self.armor > 1:
                self.armor -= 1
            if self.armor == 0:
                self.dead()
                self.funkcja()
                zebranieSound.play()

    def dead(self):
        self.alive = False

    @abstractmethod
    def funkcja(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass


class GrzybJadalny(Obiekty):
    def funkcja(self):
        char.koszyk += 1

    def draw(self, screen):
        if self.alive == True:
            screen.blit(grzybjadalny_img, (self.x, self.y))


class Muchomor(Obiekty):
    def funkcja(self):
        char.utrata_zycia()

    def draw(self, screen):
        if self.alive == True:
            screen.blit(muchomor_img, (self.x, self.y))


class Halucyn(Obiekty):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.armor = 1

    def funkcja(self):
        char.halucyn_mode = True

    def draw(self, screen):
        if self.alive == True:
            screen.blit(halucyn_img, (self.x, self.y))


class Odtrutka_na_halucyna(Obiekty):
    def funkcja(self):
        char.halucyn_mode = False

    def draw(self, screen):
        if self.alive == True:
            screen.blit(odtrutka_img, (self.x, self.y))


class Knife(Obiekty):
    def funkcja(self):
        char.knife_mode = True

    def draw(self, screen):
        if self.alive == True:
            screen.blit(knife_img, (self.x, self.y))


def generowanieObiektu():
    if len(lista_obiektow) <= 9:
        if char.knife_mode == False:
            x = random.randint(0, 4)
        else:
            x = random.randint(0, 3)
        if x == 0:
            lista_obiektow.append(GrzybJadalny(64, 64))
        elif x == 1:
            lista_obiektow.append(Muchomor(64, 64))
        elif x == 2:
            lista_obiektow.append(Halucyn(64, 64))
        elif x == 3:
            lista_obiektow.append(Odtrutka_na_halucyna(64, 64))
        elif x == 4:
            lista_obiektow.append(Knife(64, 64))
    else:
        lista_obiektow.pop(random.randint(0, 9))


def zbieranie():
    for i in range(len(lista_obiektow)):
        if ((char.x >= lista_obiektow[i].x and char.x - lista_obiektow[i].x <= 64) or (
                char.x <= lista_obiektow[i].x and lista_obiektow[i].x - char.x <= 64)) \
                and ((char.y >= lista_obiektow[i].y and char.y - lista_obiektow[i].y <= 64) or (
                char.y <= lista_obiektow[i].y and lista_obiektow[i].y - char.y <= 64)):
            lista_obiektow[i].hit()
