import pygame
import random

pygame.init()

#화면 크기 설정
screen_width=1000
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))

#게임이름
pygame.display.set_caption("기둥피하기")

clock=pygame.time.Clock()
#배경
background= pygame.image.load("배경.png")

cha= pygame.image.load("캐릭.png")
cha_size=cha.get_rect().size
cha_width=cha_size[0]
cha_height=cha_size[1]
cha_x_pos=(cha_width)
cha_y_pos=(screen_height/2-cha_height/2)
cha_to_x=0
cha_to_y=0
cha_spd=1

#기둥 (30,200), (30,400), (30,200 왔다갔다), (30,250), (30,350)
pillar=pygame.image.load("기둥.png")
pillar_size=pillar.get_rect().size
pillar_width=pillar_size[0]
pillar_height=pillar_size[1]
pillar_x_pos=screen_width
pillar_y_pos=random.randint(0,screen_height-pillar_height)


pillar1=pygame.image.load("기둥1.png")
pillar1_size=pillar1.get_rect().size
pillar1_width=pillar1_size[0]
pillar1_height=pillar1_size[1]
pillar1_x_pos=pillar_x_pos+400
pillar1_y_pos=random.randint(0,screen_height-pillar1_height)

pillar2=pygame.image.load("기둥2.png")
pillar2_size=pillar2.get_rect().size
pillar2_width=pillar2_size[0]
pillar2_height=pillar2_size[1]
pillar2_x_pos=pillar1_x_pos+400
pillar2_y_pos=random.randint(0,screen_height-pillar2_height)
pillar2_to_y=-3

pillar3=pygame.image.load("기둥3.png")
pillar3_size=pillar3.get_rect().size
pillar3_width=pillar3_size[0]
pillar3_height=pillar3_size[1]
pillar3_x_pos=pillar2_x_pos+400
pillar3_y_pos=random.randint(0,screen_height-pillar3_height)

pillar4=pygame.image.load("기둥4.png")
pillar4_size=pillar4.get_rect().size
pillar4_width=pillar4_size[0]
pillar4_height=pillar4_size[1]
pillar4_x_pos=pillar3_x_pos+400
pillar4_y_pos=random.randint(0,screen_height-pillar4_height)

pillar_spd=-3

start_ticks=pygame.time.get_ticks()
game_font=pygame.font.Font(None, 40)

running = True#게임이 진행 중인가?
while running:
    dt=clock.tick(50)
    time=(pygame.time.get_ticks()-start_ticks)/1000
    timer=game_font.render("timer:"+ str(int(time)),True,(0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창 종료 이벤트 발생 하였는가?
            running=False#게임 진행 중이 아님
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                cha_to_x -= 0.1
            elif event.key==pygame.K_RIGHT:
                cha_to_x+=0.1
            if event.key == pygame.K_UP:
                cha_to_y-=cha_spd
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                cha_to_x=0
            elif event.key == pygame.K_UP:
                cha_to_y=0
    cha_x_pos+=cha_to_x*dt
    cha_y_pos+=(cha_to_y*dt)+10

    if cha_x_pos<0-(cha_width/2):
        running=False
    if cha_x_pos>=300:
        cha_x_pos=300
    elif cha_x_pos>screen_width-cha_width:
        cha_x_pos=screen_width-cha_width
    #세로 경계값 처리
    if cha_y_pos<0:
        cha_y_pos=0 
    elif cha_y_pos>screen_height:
        running=False    
    pillar_x_pos+=pillar_spd
    pillar1_x_pos+=pillar_spd
    pillar2_x_pos+=pillar_spd
    pillar2_y_pos+=pillar2_to_y
    if pillar2_y_pos < 0:
        pillar2_to_y=(pillar2_to_y*-1)
    if pillar2_y_pos>screen_height-pillar2_height:
        pillar2_to_y=(pillar2_to_y*-1)
    pillar3_x_pos+=pillar_spd
    pillar4_x_pos+=pillar_spd

    if pillar_x_pos<0:
        pillar_x_pos=screen_width
        pillar_y_pos=random.randint(0,screen_height-pillar_height)
    if pillar1_x_pos<0:
        pillar1_x_pos=pillar_x_pos+400
        pillar1_y_pos=random.randint(0,screen_height-pillar1_height)
    if pillar2_x_pos<0:
        pillar2_x_pos=pillar1_x_pos+400
        pillar2_y_pos=random.randint(0,screen_height-pillar2_height)
    if pillar3_x_pos<0:
        pillar3_x_pos=pillar2_x_pos+400
        pillar3_y_pos=random.randint(0,screen_height-pillar3_height)
    if pillar4_x_pos<0:
        pillar4_x_pos=pillar3_x_pos+400
        pillar4_y_pos=random.randint(0,screen_height-pillar4_height)
        pillar_spd+=-0.5
    #충돌처리
    cha_rect=cha.get_rect()
    cha_rect.left=cha_x_pos
    cha_rect.top=cha_y_pos

    pillar_rect=pillar.get_rect()
    pillar_rect.left=pillar_x_pos
    pillar_rect.top=pillar_y_pos

    pillar1_rect=pillar1.get_rect()
    pillar1_rect.left=pillar1_x_pos
    pillar1_rect.top=pillar1_y_pos

    pillar2_rect=pillar2.get_rect()
    pillar2_rect.left=pillar2_x_pos
    pillar2_rect.top=pillar2_y_pos

    pillar3_rect=pillar3.get_rect()
    pillar3_rect.left=pillar3_x_pos
    pillar3_rect.top=pillar3_y_pos

    pillar4_rect=pillar4.get_rect()
    pillar4_rect.left=pillar4_x_pos
    pillar4_rect.top=pillar4_y_pos
    
    if cha_rect.colliderect(pillar_rect):
        cha_x_pos=pillar_x_pos-cha_width
    if cha_rect.colliderect(pillar1_rect):
        cha_x_pos=pillar1_x_pos-cha_width
    if cha_rect.colliderect(pillar2_rect):
        cha_x_pos=pillar2_x_pos-cha_width
    if cha_rect.colliderect(pillar3_rect):
        cha_x_pos=pillar3_x_pos-cha_width
    if cha_rect.colliderect(pillar4_rect):
        cha_x_pos=pillar4_x_pos-cha_width
    
    #화면 그리기
    screen.blit(background,(0,0))
    screen.blit(pillar,(pillar_x_pos,pillar_y_pos ))
    screen.blit(pillar1,(pillar1_x_pos,pillar1_y_pos ))
    screen.blit(pillar2,(pillar2_x_pos,pillar2_y_pos ))
    screen.blit(pillar3,(pillar3_x_pos,pillar3_y_pos))
    screen.blit(pillar4,(pillar4_x_pos,pillar4_y_pos))
    screen.blit(timer,(870,10))
    screen.blit(cha,(cha_x_pos,cha_y_pos))
    
    pygame.display.update()#게임화면 다시 그리기
pygame.time.delay(2000)
#pygame 종료
pygame.quit()