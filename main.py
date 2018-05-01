import sys
import pygame

from pygame.locals import *
from setting import *
from ourplane import OurPlane
from enemy import Enemy
from bullet import Bullet

#设置窗口及背景
bg_size=(480,852)
screen=pygame.display.set_mode(bg_size)
font=pygame.font.SysFont('skaiti',20)
pygame.display.set_caption("飞机大战")
background=pygame.image.load("Data/image/background.png")

ourplane=OurPlane(bg_size)
#生成的敌机加入组
def add_small_enemy(group1,group2,num):
    for i in range(num):
        small_enemy=Enemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)

def main():
    #BGM，运行，自机显示切换，delay用于控制事件延迟
    pygame.mixer.music.play(-1)
    running=True
    switch_image=False
    delay=60
    score=0

    #生成敌人组
    enemies=pygame.sprite.Group()
    small_enemys=pygame.sprite.Group()
    add_small_enemy(small_enemys,enemies,4)

    #记录当前操作到第几个
    bullet_index=0
    el_destroy_index=0
    me_destroy_index=0

    #生成指定个子弹
    bullet1=[]
    bullet_num=8
    for i in range(bullet_num):
        bullet1.append(Bullet(ourplane.rect.midtop))

    while running:
        screen.blit(background, (0, 0))
        score_surface = font.render(str(score), True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))

        clock=pygame.time.Clock()
        clock.tick(60)

        if not (delay % 3):
            switch_image=not switch_image

        #显示敌机
        for each in small_enemys:
            if each.active:
                for e in small_enemys:
                    e.move()
                    screen.blit(e.image,e.rect)

            #击坠处理
            else:
                if el_destroy_index:
                    enemy1_down_sound.play()
                screen.blit(each.destroy_images[el_destroy_index],each.rect)
                el_destroy_index=(el_destroy_index+1)%4
                if el_destroy_index==0:
                    each.reset()

        if ourplane.active:
            #动态效果
            if switch_image:
                screen.blit(ourplane.image_one,ourplane.rect)
            else:
                screen.blit(ourplane.image_two,ourplane.rect)

            #发射子弹
            if not (delay % 10):
                bullet_sound.play()
                bullets=bullet1
                bullets[bullet_index].reset(ourplane.rect.midtop)
                bullet_index=(bullet_index+1)%bullet_num

            #显示子弹及碰撞处理
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemies_hit=pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                    if enemies_hit:
                        b.active=False
                        for e in enemies_hit:
                            e.active=False
                            score+=1

        #自机爆炸效果
        else:
            if not (delay % 3):
                screen.blit(ourplane.destroy_images[me_destroy_index],ourplane.rect)
                me_destroy_index=(me_destroy_index+1)%4
                if me_destroy_index==0:
                    me_down_sound.play()
                    ourplane.reset()

        #自机与敌机碰撞

        enemies_down=pygame.sprite.spritecollide(ourplane,enemies,False,pygame.sprite.collide_mask)
        if enemies_down:
            ourplane.active=False
            score=0
            for row in enemies:
                row.active=False
                row.reset()

        if delay==0:
            delay=60
        delay-=1

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            ourplane.move_up()
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            ourplane.move_left()
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            ourplane.move_down()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            ourplane.move_right()

        for event in pygame.event.get():
            if event.type == 12:
                pygame.quit()
                sys.exit()

        pygame.display.flip()