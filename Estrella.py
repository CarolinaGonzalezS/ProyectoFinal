import math

import pygame

verde = (0, 255, 0)
azul = (0, 0, 255)

pygame.init()

pygame.display.set_caption('Formas')
pantalla = pygame.display.set_mode((1000, 1000))
x=400
y=80
for i in range(1,10):
    pygame.draw.arc(pantalla, verde, (60, x, 500, y), 0, math.pi, 1)     
    x=x-10
    y=y+20
    print(x)
    print(y)
    #10
    #200
for j in range(1,10):
    pygame.draw.arc(pantalla, verde, (400, x, 500, y), 0, math.pi, 1)     
    x=x+10
    y=y-20


# línea suavizada (anti-aliased)


pygame.display.flip()

while True:
    evento = pygame.event.wait()

    if evento.type == pygame.QUIT:
        break

pygame.quit()