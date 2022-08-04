import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
    # init()

    def input(self):
        keys = pygame.key.get_pressed() 
        print(keys[pygame.K_w])
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -1
            # print("up")
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y = 1
            print("down")
        else: 
            self.direction.y = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
            print("right")
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
            print("left")
        else: 
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            print('attack')
        if keys[pygame.K_LSHIFT]:
            print('magic')
    # input()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center 
    # move()

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left 
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right 
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top 
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
    # collision()

    def update(self):
        self.input()
        self.move(self.speed)
    # update

