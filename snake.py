import pygame
import time
import random

# Inicializo Pygame
pygame.init()

# Defino los colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
rojo = (213, 50, 80)
azul = (50, 153, 213)
gris = (169, 169, 169)

# Configuro la pantalla
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de Snake')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Tamaño de cada bloque
tamaño_bloque = 20
velocidad_snake = 15

# Fuente para el marcador
fuente = pygame.font.SysFont(None, 35)

def tu_puntaje(puntaje):
    valor = fuente.render("Puntaje: " + str(puntaje), True, blanco)
    pantalla.blit(valor, [0, 0])

def mensaje_final(msg, color):
    mesg = fuente.render(msg, True, color)
    pantalla.blit(mesg, [ancho / 6, alto / 3])

def botones(mensaje, color, pos):
    fuente_boton = pygame.font.SysFont(None, 25)
    texto = fuente_boton.render(mensaje, True, color)
    pygame.draw.rect(pantalla, gris, pos)
    pantalla.blit(texto, (pos[0] + 10, pos[1] + 10))

def nuestra_snake(tamaño_bloque, lista_snake):
    for x in lista_snake:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamaño_bloque, tamaño_bloque])

def juego():
    """
    Función principal del juego.
    """
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_snake = []
    longitud_snake = 1

    comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20.0

    while not game_over:
        while game_close == True:
            pantalla.fill(azul)
            if longitud_snake - 1 >= 100:
                mensaje_final("¡Ganaste! Felicitaciones!", verde)
            else:
                mensaje_final("Perdiste", rojo)
            tu_puntaje(longitud_snake - 1)

            # Botones para jugar de nuevo o terminar
            botones("Jugar de nuevo", blanco, [ancho / 4, alto / 2, 150, 50])
            botones("Terminar", blanco, [ancho / 2 + 10, alto / 2, 150, 50])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if ancho / 4 <= x <= ancho / 4 + 150 and alto / 2 <= y <= alto / 2 + 50:
                        # reinicio el juego
                        juego()  
                    elif ancho / 2 + 10 <= x <= ancho / 2 + 10 + 150 and alto / 2 <= y <= alto / 2 + 50:
                        game_over = True
                        game_close = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_bloque
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_bloque
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])
        cabeza_snake = []
        cabeza_snake.append(x1)
        cabeza_snake.append(y1)
        lista_snake.append(cabeza_snake)
        if len(lista_snake) > longitud_snake:
            del lista_snake[0]

        for x in lista_snake[:-1]:
            if x == cabeza_snake:
                game_close = True

        nuestra_snake(tamaño_bloque, lista_snake)
        tu_puntaje(longitud_snake - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20.0
            longitud_snake += 1

        reloj.tick(velocidad_snake)

    pygame.quit()
    quit()

# Función para mostrar el menú de inicio
def menu_inicio():
    inicio = True
    while inicio:
        pantalla.fill(azul)
        mensaje_final("Juego de Snake", verde)
        botones("Iniciar Juego", blanco, [ancho / 4, alto / 2, 150, 50])
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if ancho / 4 <= x <= ancho / 4 + 150 and alto / 2 <= y <= alto / 2 + 50:
                    inicio = False
                    juego()

menu_inicio()
