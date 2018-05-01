import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Bullet,self).__init__()
        #图像及判定
        self.image=pygame.image.load("Data/image/bullet1.png")
        self.mask = pygame.mask.from_surface(self.image)
        #位置处理
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        #速度和活动状态
        self.speed=10
        self.active=True
#移动
    def move(self):
        if self.rect.top<0:
            self.active=False
        else:
            self.rect.top-=self.speed
#重置
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True