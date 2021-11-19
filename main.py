#sprite
import pygame
FPS = 60

WHITE = (255,255,255)
GREEN=(0, 255, 0)

WIDTH = 500
HEIGHT = 600

#遊戲初始化跟建立視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('射擊遊戲')
clock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center(WIDTH/2,HEIGHT/2)
    
    def update(self):
        self.rect.x +=2

all_sprites=pygame.sprite.Group()
player = Player()
all_sprites.add(player)



#寫遊戲迴圈
running = True
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():#列表輸入輸出
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    all_sprites.update()
    #畫面顯示

    screen.fill(WHITE)
    all_sprites.draw(screen) 
    pygame.display.update()
pygame.quit()
