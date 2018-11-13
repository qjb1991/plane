#coding=utf-8
import pygame
import time
from pygame.locals import *
import random

class BasePlane(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)


class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 500, "./resources/hero1.png")
    
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
       self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./resources/enemy0.png")
        self.sign = 0



    def move(self):
        if self.sign == 0:
            self.x += 5
        elif self.sign == 1:
            self.x -= 5

        if self.x > 320:
            self.sign = 1
        elif self.x < 0:
            self.sign = 0

    # def move_left(self):
    #     self.x -= 5

    # def move_right(self):
    #     self.x += 5

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 30 or random_num == 50:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+40, y-20, "./resources/bullet.png")

    def move(self):
        self.y -= 8

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./resources/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()

            elif event.key == K_SPACE:
                print('space')
                hero.fire()

def main():
    screen = pygame.display.set_mode((380, 652), 0, 32)

    background = pygame.image.load("./resources/background.png")

    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.02)

if __name__ == "__main__":
    main()
