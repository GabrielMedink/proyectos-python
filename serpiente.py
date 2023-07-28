import pygame
import time
import random

pygame.init()

# Dimensiones de la ventana del juego
ancho = 800
alto = 600

# Colores RGB
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)

# Tamaño del bloque y velocidad de la serpiente
tamano_bloque = 10
velocidad = 15

# Crear la ventana del juego
ventana_juego = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de Serpiente')

# Función para mostrar el mensaje en pantalla
def mensaje(msg, color):
    fuente = pygame.font.SysFont(None, 30)
    pantalla_texto = fuente.render(msg, True, color)
    ventana_juego.blit(pantalla_texto, [ancho / 6, alto / 3])

# Función principal del juego
def juego():
    juego_terminado = False
    juego_finalizado = False

    # Coordenadas iniciales de la serpiente
    cabeza_x = ancho / 2
    cabeza_y = alto / 2

    # Cambios en las coordenadas
    cambio_x = 0
    cambio_y = 0

    # Lista para guardar las partes del cuerpo de la serpiente
    cuerpo_serpiente = []

    # Longitud inicial de la serpiente
    longitud_serpiente = 1

    # Coordenadas del alimento
    comida_x = round(random.randrange(0, ancho - tamano_bloque) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamano_bloque) / 10.0) * 10.0

    # Loop principal del juego
    while not juego_terminado:

        while juego_finalizado == True:
            ventana_juego.fill(blanco)
            mensaje("Has perdido. Presiona C para continuar o Q para salir.", rojo)
            pygame.display.update()

            # Eventos del teclado mientras el juego está en la pantalla de finalización
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        juego_terminado = True
                        juego_finalizado = False
                    if event.key == pygame.K_c:
                        juego()

        # Eventos del teclado mientras el juego está en funcionamiento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_terminado = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambio_x = -tamano_bloque
                    cambio_y = 0
                elif event.key == pygame.K_RIGHT:
                    cambio_x = tamano_bloque
                    cambio_y = 0
                elif event.key == pygame.K_UP:
                    cambio_y = -tamano_bloque
                    cambio_x = 0
                elif event.key == pygame.K_DOWN:
                    cambio_y = tamano_bloque
                    cambio_x = 0

        # Si la cabeza de la serpiente sale de la ventana del juego, el juego termina
        if cabeza_x >= ancho or cabeza_x < 0 or cabeza_y >= alto or cabeza_y < 0:
            juego_finalizado = True

        cabeza_x += cambio_x
        cabeza_y += cambio_y
        ventana_juego.fill(blanco)

        # Dibujar la comida
        pygame.draw.rect(ventana_juego, verde, [comida_x, comida_y, tamano_bloque, tamano_bloque])
        # Actualizar la posición de la serpiente
        serpiente_cabeza = []
        serpiente_cabeza.append(cabeza_x)
        serpiente_cabeza.append(cabeza_y)
        cuerpo_serpiente.append(serpiente_cabeza)
        if len(cuerpo_serpiente) > longitud_serpiente:
            del cuerpo_serpiente[0]

        # Si la cabeza de la serpiente toca cualquier parte del cuerpo, el juego termina
        for bloque in cuerpo_serpiente[:-1]:
            if bloque == serpiente_cabeza:
                juego_finalizado = True

        # Dibujar el cuerpo de la serpiente
        for parte in cuerpo_serpiente:
            pygame.draw.rect(ventana_juego, negro, [parte[0], parte[1], tamano_bloque, tamano_bloque])

        pygame.display.update()

        # Si la serpiente come el alimento, crece y se coloca un nuevo alimento en otra posición
        if cabeza_x == comida_x and cabeza_y == comida_y:
            comida_x = round(random.randrange(0, ancho - tamano_bloque) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamano_bloque) / 10.0) * 10.0
            longitud_serpiente += 1

        # Controlar la velocidad del juego
        pygame.time.Clock().tick(velocidad)

    pygame.quit()
    quit()

# Iniciar el juego
juego()
