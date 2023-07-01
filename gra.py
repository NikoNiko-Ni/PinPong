import pygame as pg
import random

pg.init()
win_width, win_height = 800, 600
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Pin Pong")
count_animation = 0


class GameSprite:

    def __init__(self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 600-100:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 600-100:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

x2, y2 = 2, 2

class Ball(GameSprite):

    def move(self):
        global x2,y2, player1, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2, self):
            x2= -5
        if pg.sprite.collide_rect(player1, self):
            x2= 5
        if self.rect.y < 0:
            y2 = 5
        if self.rect.y > 550:
            y2 = -5


back = GameSprite("fon.jpg", 0,0, 800,600, 0)
player1 = Player("feia1.png", 0,300, 50,100, 4)
player2 = Player("feia2.png", 750,300, 50,100, 4)
ball = Ball("miah.png", 400, 300, 50,50 , 4)

music = pg.mixer.Sound("Alfea.mp3")
music.play(-2)
music.set_volume(0.2)

game = True
score_1 = 0
score_2 = 0
gameover = "pobed2.jpg"

while game:

    pg.time.Clock().tick(144)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if ball.rect.x < 0:
        score_1 += 1
        ball.rect.x = 400
    if score_1 >=3:
        gameover = "pobed2.jpg"
        game = False
    

    if ball.rect.x > 800:
        score_2 += 1
        ball.rect.x = 400
    if score_2 >=3:
        gameover = "pobed1.jpg"
        game = False
    

    back.reset()
    player1.reset()
    player1.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    label = pg.font.SysFont("Gabriola", 35).render(f'команда "Сирень" : {score_2}', True, "purple")
    window.blit(label,(302,45))
    label2 = pg.font.SysFont("Gabriola", 35).render(f'команда "Малина" : {score_1}', True, "crimson")
    window.blit(label2,(300,100))
    pg.display.flip()

bg = GameSprite(gameover, 0, 0, 800,600, 0)
while True:

    pg.time.Clock().tick(60)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    bg.reset()
    pg.display.flip()