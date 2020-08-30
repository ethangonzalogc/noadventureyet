import pygame
pygame.init ()

win = pygame.display.set_mode ((1000,700))
surface=pygame.image.load('images/fondo1.png')
personaje_1=pygame.image.load('images/personaje1.png')
personaje_2=pygame.image.load('images/personaje2.png')
pygame.display.set_caption ("NOT ADVENTURE YET")


personaje_mov = personaje_1
personaje_mov_control = 1

vel = 3
x = 50
y = 500
width = 20
height = 20

run = True 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    keys= pygame.key.get_pressed()

    if keys [pygame.K_LEFT]:
        x -= vel
    if keys [pygame.K_RIGHT]:
        x += vel 
        personaje_mov = personaje_1
    if keys [pygame.K_UP]:
        y -= vel
        personaje_mov = personaje_1
    if keys [pygame.K_DOWN]:
        y += vel
        personaje_mov = personaje_2



    #win.fill ((0,0,0))        
    #pygame.draw.rect ( win, (8, 20, 129), (x, y, width, height))
    win.blit(personaje_mov,(x,y))
    pygame.display.update ()
    win.blit(surface,(0,0))

pygame.quit ()