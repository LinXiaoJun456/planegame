import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        super(Enemy,self).__init__()
        #图像及判定处理
        self.image=pygame.image.load("Data/image/enemy1.png")
        self.mask = pygame.mask.from_surface(self.image)
        #位置处理，初始位置为屏幕上方未显示区域
        self.rect=self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, -5)
        #速度和活动状态
        self.speed=2
        self.active=True
        #爆炸效果
        self.destroy_images=[]
        self.destroy_images.extend(
                  [
                      pygame.image.load("Data/image/enemy1_down1.png"),
                      pygame.image.load("Data/image/enemy1_down2.png"),
                      pygame.image.load("Data/image/enemy1_down3.png"),
                      pygame.image.load("Data/image/enemy1_down4.png")
                  ]
              )

#向下移动
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()

#重置
    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, -5)
        self.active=True