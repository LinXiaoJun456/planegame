import pygame

class OurPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        super(OurPlane, self).__init__()#super函数不重复的调用父类的函数
             # 飞机的图片，两张图片可不停切换
        self.image_one=pygame.image.load("Data/image/hero1.png")
        self.image_two=pygame.image.load("Data/image/hero2.png")
             #获取飞机位置
        self.rect=self.image_one.get_rect()
             # 本地化背景图片的尺寸
        self.width,self.height=bg_size[0],bg_size[1]
            # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.mask=pygame.mask.from_surface(self.image_one)
            # 定义飞机初始化位置，底部预留60像素
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,(self.height-self.rect.height-60)
           #设置飞机速度
        self.speed=10
          #设置飞机存活状态
        self.active=True
           #飞机毁灭效果
        self.destroy_images=[]
        self.destroy_images.extend(
            [
                pygame.image.load("Data/image/hero_blowup_n1.png"),
                pygame.image.load("Data/image/hero_blowup_n2.png"),
                pygame.image.load("Data/image/hero_blowup_n3.png"),
                pygame.image.load("Data/image/hero_blowup_n4.png")
            ]
        )

#上下左右移动
    def move_up(self):
        if self.rect.top>0:
            self.rect.top-=self.speed
        else:
            self.rect.top=0

    def move_down(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.rect.top=self.height

    def move_left(self):
        if self.rect.left>0:
            self.rect.left-=self.speed
        else:
            self.rect.left=0

    def move_right(self):
        if self.rect.left<self.width:
            self.rect.left+=self.speed
        else:
            self.rect.left=self.width

#重置
    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        self.active=True




