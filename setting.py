import pygame

pygame.init()
pygame.mixer.init()

#bgm
pygame.mixer.music.load("Data/sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)

#子弹音效
bullet_sound=pygame.mixer.Sound("Data/sound/bullet.wav")
bullet_sound.set_volume(0.2)

#玩家死亡
me_down_sound=pygame.mixer.Sound("Data/sound/game_over.wav")
me_down_sound.set_volume(0.2)

#敌方死亡
enemy1_down_sound=pygame.mixer.Sound("Data/sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)