import pygame
import math
NEGRO=(0, 0, 0)
BLANCO=(255, 255, 255)
VERDE= (0, 255, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
VIOLETA=(98, 0, 255)
verde = (0, 255, 0)
subida=0

pygame.init()

dimensiones=[700,500]
posicion_base=[0, 0]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("JUEGO:JUMPSTREET")
imagen_de_fondo = pygame.image.load("2.jpg").convert()

hecho = False

reloj = pygame.time.Clock()

rect_x=300
rect_y=250
x_speed = 0
y_speed = 0
cuerdaUP = 50
cadenay=[250]
x=90
y=400


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


    #mueve la cuerda



    #detectar la accion de las teclas
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_UP:
            y_speed=-30
            
                    
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_UP:
            y_speed = 10


    #cuerda		
    pygame.draw.arc(pantalla, ROJO, (60, x, 500, y), 0, math.pi,4 ) 
     #velocidad
    pygame.time.delay(100)  
  
    if x==60:    	
        subida=1        
    elif x==280:
        subida=2        
    if subida==1:
        x=x+10
        y=y-20
        

    else:        
        x=x-10
        y=y+20

    print(y)
    print("cuadrado")
    print(rect_y)
    if y==20 and rect_y==250:
        print("perdio")

# salto del jugador:
	
    for rect_y in  cadenay:
    	rect_y += y_speed


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()