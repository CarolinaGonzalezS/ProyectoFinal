import random
import pygame
import math
from pygame.locals import *
import sys
import time
NEGRO=(0, 0, 0)
BLANCO=(255, 255, 255)
VERDE= (0, 255, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
VIOLETA=(98, 0, 255)
verde = (0, 255, 0)


class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, VIOLETA)
        self.imagen_destacada = fuente.render(titulo, 1, VIOLETA)
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 150
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = []        
        fuente = pygame.font.Font('dejavu.ttf', 20)
        #ubicacion del cursor
        x = 149
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)            

def comenzar_nuevo_juego():
    arri=0
    angulo=math.pi
    salto=0
    velocidad=150
    pygame.init()
    dimensiones=[700,500]
    posicion_base=[0, 0]
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("JUEGO:Pac-Jumps")
    pygame.mixer.music.load("pacman.mp3")
    pygame.mixer.music.play(1)
    pacman = pygame.image.load("pacman1.jpg").convert_alpha()
    perder = pygame.image.load("perder.jpg").convert_alpha()
    fantasma1 = pygame.image.load("fantasma2.jpg").convert_alpha()
    fantasma2 = pygame.image.load("fantasma3.jpg").convert_alpha()

    imagen_de_fondo = pygame.image.load("fondo1.jpg").convert()

    hecho = False

    reloj = pygame.time.Clock()

    rect_x=260
    rect_y=203
    x_speed = 0
    y_speed = 0
    cuerdaUP = 50
    cadenay=[203]
    x=90
    y=400
    f1=540
    f2=1

    while not hecho:
    # --- Bucle principal de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

       

        pantalla.fill(NEGRO)
        # Copia la imagen en pantalla:        
        pantalla.blit(imagen_de_fondo, posicion_base)
        pantalla.blit(fantasma1, (f1, 216))
        pantalla.blit(fantasma2, (f2, 216))
        pantalla.blit(pacman, (rect_x, rect_y))
        
        #dibuja el cuadrado
    
        #dibuja el arco

        pygame.time.delay(velocidad)  

        #mueve la cuerda
        #detectar la accion de las teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                y_speed=-30    
                rect_x=260
                salto+=1 
                pacman = pygame.image.load("pacman2.jpg").convert_alpha() 
                fantasma1 = pygame.image.load("fantasma4.jpg").convert_alpha()
                fantasma2 = pygame.image.load("fantasma7.jpg").convert_alpha()
                f1=560                
          
                    
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP:
                y_speed = 0
                rect_x=255
                pacman = pygame.image.load("pacman1.jpg").convert_alpha() 
                fantasma1 = pygame.image.load("fantasma5.jpg").convert_alpha()
                fantasma2 = pygame.image.load("fantasma6.jpg").convert_alpha()

            

        
        #cuerda     
        pygame.draw.arc(pantalla, ROJO, (70, x, 500, y), 0, angulo,4 )    
        if x==50:       
            arri=1        
        elif x==280:
            arri=2        
        if arri==1:
            x=x+10
            y=y-20           
    
        else:        
            x=x-10
            y=y+20
            print(x)

        #Coliciones

        print(y)
        
        if y==20 and rect_y==203:
            for i in range(0, 10):
                pantalla.blit(perder, (255, 150))
            print("----------------------perdio------------------------")
            time.sleep(10)
            sys.exit(0)       


        #Aumento de velocidad
        if salto==5:
            velocidad=velocidad-5
            salto=0


        #Cambio de cuerda
        if velocidad==20:
            angulo=2*angulo
            velocidad=150
            fantasma1 = pygame.image.load("fantasma1.jpg").convert_alpha()
            fantasma2 = pygame.image.load("fantasma1.jpg").convert_alpha()


    # salto del jugador:
    
        for rect_y in  cadenay:
            rect_y += y_speed
            print("cuadrado")
            print(rect_y)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

def mostrar_opciones():
    pygame.init()
    dimensiones=[700,399]
    posicion_base=[0, 0]
    hecho = False
    reloj = pygame.time.Clock()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("JUEGO:Pac-Jumps")
    pygame.mixer.music.load("pacman.mp3")
    pygame.mixer.music.play(1)
    instrucciones = pygame.image.load("regla.jpg").convert_alpha()

    while not hecho:
    # --- Bucle principal de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
        pantalla.fill(NEGRO)
        # Copia la imagen en pantalla:        
        pantalla.blit(instrucciones, posicion_base)

    
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()


def salir_del_programa():
    print (" Gracias por utilizar este programa.")
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("¿Como Jugar?", mostrar_opciones),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()    
    screen = pygame.display.set_mode((379, 288))
    fondo = pygame.image.load("fondo.jpg").convert()
    menu = Menu(opciones)


    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))        
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
