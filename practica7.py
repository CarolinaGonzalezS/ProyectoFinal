import pygame
import math
NEGRO=(0, 0, 0)
BLANCO=(255, 255, 255)
VERDE= (0, 255, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
VIOLETA=(98, 0, 255)
verde = (0, 255, 0)
class Menu:
    def __init__(self, opciones):
        self.opciones = opciones
        self.seleccionado = False
        self.mantiene_pulsado = False
 
    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
 
        tecla = pygame.key.get_pressed()
 
        if not self.mantiene_pulsado:
            if tecla[K_UP]:
                self.seleccionado -= 1
            elif tecla[K_DOWN]:
                self.seleccionado += 1
            elif tecla[K_RETURN]:
 
                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print "Selecciona la opción: ", titulo
                funcion()
 
        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
 
        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = tecla[K_UP] or tecla[K_DOWN] or tecla[K_RETURN]
    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""
 
        total = self.total
        indice = 0
        altura_de_opcion = 30
        x = 200
        y = 300
 
        for (titulo, funcion) in self.opciones:
 
            # evalúa si debe destacar al opción
            if indice == self.seleccionado:
                color = (255, 255, 255)
            else:
                color = (230, 230, 230)
 
            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)