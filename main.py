#sprite
import pygame
import random
import os
#設定數值
fps = 60  
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(102,204,255)
YELLOW=(255,255,224)
PINK=(255,182,193)
GREEN=(0,255,0)
WIDTH=500
HEIGHT=600


#遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #創建視窗
pygame.display.set_caption('大噴射戰機')         #改變標題
clock = pygame.time.Clock()
#仔入圖片
background_img=pygame.image.load(os.path.join("img","background.png")).convert()
player_img=pygame.image.load(os.path.join("img","player.png")).convert()
bullet_img=pygame.image.load(os.path.join("img","bullet.png")).convert()
rock_img=pygame.image.load(os.path.join("img","rock.png")).convert()

font_name = (os.path.join("font.ttf"))

def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface =font.render(text,True,YELLOW)  #設定字體顏色
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)   #將文字顯示在畫面上
def new_meteorite():
        r = meteorite()
        all_sprites.add(r)
        meteorites.add(r)


def draw_health(surf,hp,x,y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)   #生命條顏色
    pygame.draw.rect(surf, WHITE, outline_rect, 2)   #生命條邊框顏色與厚度

def draw_init():
    screen.fill(BLUE)
    screen.blit(background_img,(0,0))  #背景圖片
    draw_text(screen,'大噴射戰機',64,WIDTH/2,HEIGHT/4)  #遊戲標題
    draw_text(screen,'左右操控飛船，空白發射子彈',22,WIDTH/2,HEIGHT/2)  #遊戲說明
    draw_text(screen,'按任意鍵開始遊戲',16,WIDTH/2,HEIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP: #按鍵鬆手開始
                waiting = False
                return False



#設定飛船的數值與移動方式
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,40))
        self.image=pygame.transform.scale(player_img,(50,40))
        self.image.set_colorkey(BLACK)  #將圖片的黑色部分變成透明
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10    #控制飛船軌道
        self.speedx = 10
        self.health = 100   #生命值

    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx    #控制向右
        if key_pressed[pygame.K_LEFT]:    
            self.rect.x -= self.speedx    #控制向左 


        if self.rect.right > WIDTH:
            self.rect.right = WIDTH    #控制右邊界
        if self.rect.left < 0:
            self.rect.left = 0         #控制左邊界
    def shoot(self):
        missile1 = missile(self.rect.centerx,self.rect.top)  #飛彈從飛船中心發出
        all_sprites.add(missile1)   
        missiles.add(missile1)      #將飛彈加入群組





#設定隕石的數值與移動方式
class meteorite(pygame.sprite.Sprite):  


    def __init__(self):
        super().__init__()
        self.image = rock_img
        self.image.set_colorkey(BLACK)
        scale = random.randrange(20,80)  #隕石大小隨機  
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,9)
        self.speedx = random.randrange(-3,3)


        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top> HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0,WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,9)  
            self.speedx = random.randrange(-3,3)



#設定飛彈的數值與移動方式
class missile(pygame.sprite.Sprite):  
    def __init__(self,x,y):
        super().__init__()
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x  
        self.rect.bottom = y
        self.speedy = -10


    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()   #刪除飛彈




all_sprites = pygame.sprite.Group()
missiles = pygame.sprite.Group()
meteorites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
   new_meteorite()
   score = 0



#遊戲迴圈
show_init = True
running=True
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
    clock.tick(fps)
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  #按下空白鍵發射飛彈
                


    #更新遊戲
    all_sprites.update()
    hits = pygame.sprite.groupcollide(meteorites,missiles,True,True)  #設定飛彈與隕石碰撞後刪除
    for hit in hits:
        new_meteorite()

        score += 40  #每打掉一個隕石就加分
        


    hits = pygame.sprite.spritecollide(player,meteorites,True)  #設定飛船與隕石碰撞後遊戲結束
    for hit in hits:
        new_meteorite()  #隕石被打掉後再生成一個新的隕石
        player.health -= 20  #減少生命值
        if player.health <= 0:
            show_init = True  #生命值歸零後回到開始畫面
            all_sprites = pygame.sprite.Group()
            missiles = pygame.sprite.Group()
            meteorites = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(8):
                new_meteorite()
            score = 0





    #畫面顯示
    screen.fill(BLUE)
    screen.blit(background_img,(0,0))  #背景圖片
    all_sprites.draw(screen)
    draw_health(screen,player.health,10,10)  #顯示生命條
    draw_text(screen,str(score),18,WIDTH/2,10)  #顯示分數
   



    pygame.display.update()

pygame.quit()