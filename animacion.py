import pygame
import math
NEGRO=(0, 0, 0)
BLANCO=(255, 255, 255)
VERDE= (0, 255, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
VIOLETA=(98, 0, 255)


pygame.init()

dimensiones=[700,500]
posicion_base=[0, 0]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("JUEGO:JUMPSTREET")
imagen_de_fondo = pygame.image.load("saturn_family1.jpg").convert()
pulsar_sonido = pygame.mixer.Sound("jump2.ogg")
hecho = False

reloj = pygame.time.Clock()

rect_x=350
rect_y=450
rect_cambio_y=-3
rect_cambio_x=0
x_speed = 0
y_speed = 0
cuerdaUP = 100
cadenay=[440]
pi= math.pi
arcx1=250
arcx2=250
arcy=250
angulo1=2*pi
angulo2=pi

while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    pantalla.fill(NEGRO)
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, posicion_base)
    #dibuja el cuadrado
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    #dibuja el arco
    pygame.draw.arc(pantalla, ROJO, [250, 250, 250, cuerdaUP], angulo1, angulo2, 2)
    #mueve la cuerda

    #detectar la accion de las teclas
    if evento.type == pygame.KEYDOWN:
    	if evento.key == pygame.K_UP:
    		y_speed=-100    
    		pulsar_sonido.play()
    				
    		  		
    if evento.type == pygame.KEYUP:
    	if evento.key == pygame.K_UP:
    		y_speed = 10


    cuerdaUP += 1

    #Salto del jugador
    for rect_y in  cadenay:
    	rect_y += y_speed
    #arcy +=1




    pygame.display.flip()
    reloj.tick(60)

pygame.quit()