import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla y colores
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Vibora")

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Tamaño y velocidad de la serpiente
TAMANO_CUADRO = 20
velocidad = 10

# Función para mostrar el puntaje en pantalla
def mostrar_puntaje(puntaje):
    fuente = pygame.font.SysFont("comicsansms", 35)
    texto = fuente.render("Puntaje: " + str(puntaje), True, VERDE)
    pantalla.blit(texto, [0, 0])

# Función para mostrar la pantalla de "Perdiste"
def mostrar_pantalla_perdiste(puntaje):
    pantalla.fill(NEGRO)
    fuente = pygame.font.SysFont("comicsansms", 50)
    mensaje = fuente.render("¡Perdiste!", True, ROJO)
    pantalla.blit(mensaje, [ANCHO // 4, ALTO // 3])
    
    # Mostrar el puntaje final
    fuente_puntaje = pygame.font.SysFont("comicsansms", 20)
    texto_puntaje = fuente_puntaje.render("Puntaje final: " + str(puntaje), True, BLANCO)
    pantalla.blit(texto_puntaje, [ANCHO // 4, ALTO // 2])
    
    # Mensaje de reinicio
    reiniciar_texto = fuente_puntaje.render("Presiona cualquier tecla para reiniciar", True, BLANCO)
    pantalla.blit(reiniciar_texto, [ANCHO // 4, ALTO // 2 + 50])
    
    pygame.display.flip()
    
    # Esperar a que el jugador presione una tecla para reiniciar
    esperar_reinicio()

# Función para esperar a que el jugador presione una tecla para reiniciar
def esperar_reinicio():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

# Función para mostrar el mensaje de pausa en el centro de la pantalla
def mostrar_pausa():
    pantalla.fill(NEGRO)
    fuente = pygame.font.SysFont("comicsansms", 40)
    texto_pausa = fuente.render("Pausa", True, BLANCO)
    
    # Obtener el rectángulo del texto y centrarlo
    rect_texto = texto_pausa.get_rect(center=(ANCHO // 2, ALTO // 2))
    
    # Dibujar el texto centrado en la pantalla
    pantalla.blit(texto_pausa, rect_texto)
    pygame.display.flip()

# Función principal del juego
def juego():
    
    # Configuración inicial de la serpiente
    x_serpiente = ANCHO // 2
    y_serpiente = ALTO // 2
    direccion_x = 0
    direccion_y = 0
    cuerpo_serpiente = []
    longitud_serpiente = 1

    # Ubicación aleatoria para la comida
    x_comida = round(random.randrange(0, ANCHO - TAMANO_CUADRO) / TAMANO_CUADRO) * TAMANO_CUADRO
    y_comida = round(random.randrange(0, ALTO - TAMANO_CUADRO) / TAMANO_CUADRO) * TAMANO_CUADRO

    # Configuración del reloj para controlar la velocidad
    reloj = pygame.time.Clock()
    juego_terminado = False
    en_pausa = False  # Estado de pausa

    # Bucle principal del juego
    while not juego_terminado:
        # Eventos de teclado
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Pausar/Despausar con Enter
                    en_pausa = not en_pausa  # Alternar el estado de pausa
                    if en_pausa:
                        mostrar_pausa()
                if not en_pausa:
                    if evento.key == pygame.K_LEFT:
                        direccion_x = -TAMANO_CUADRO
                        direccion_y = 0
                    elif evento.key == pygame.K_RIGHT:
                        direccion_x = TAMANO_CUADRO
                        direccion_y = 0
                    elif evento.key == pygame.K_UP:
                        direccion_x = 0
                        direccion_y = -TAMANO_CUADRO
                    elif evento.key == pygame.K_DOWN:
                        direccion_x = 0
                        direccion_y = TAMANO_CUADRO

        # Si está en pausa, no actualizar el juego
        if en_pausa:
            pygame.display.update()
            reloj.tick(5)  # Reducir la frecuencia de actualización en pausa
            continue

        # Actualizar la posición de la serpiente
        x_serpiente += direccion_x
        y_serpiente += direccion_y

        # Condiciones de fin del juego (colisión con paredes)
        if x_serpiente < 0 or x_serpiente >= ANCHO or y_serpiente < 0 or y_serpiente >= ALTO:
            juego_terminado = True

        # Dibujar la pantalla y comida
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, ROJO, [x_comida, y_comida, TAMANO_CUADRO, TAMANO_CUADRO])

        # Agregar la cabeza de la serpiente al cuerpo
        cabeza_serpiente = [x_serpiente, y_serpiente]
        cuerpo_serpiente.append(cabeza_serpiente)
        if len(cuerpo_serpiente) > longitud_serpiente:
            del cuerpo_serpiente[0]

        # Colisión con el propio cuerpo
        for segmento in cuerpo_serpiente[:-1]:
            if segmento == cabeza_serpiente:
                juego_terminado = True

        # Dibujar la serpiente
        for segmento in cuerpo_serpiente:
            pygame.draw.rect(pantalla, VERDE, [segmento[0], segmento[1], TAMANO_CUADRO, TAMANO_CUADRO])

        # Comer la comida y generar una nueva
        if x_serpiente == x_comida and y_serpiente == y_comida:
            x_comida = round(random.randrange(0, ANCHO - TAMANO_CUADRO) / TAMANO_CUADRO) * TAMANO_CUADRO
            y_comida = round(random.randrange(0, ALTO - TAMANO_CUADRO) / TAMANO_CUADRO) * TAMANO_CUADRO
            longitud_serpiente += 1

        # Mostrar el puntaje en pantalla
        mostrar_puntaje(longitud_serpiente - 1)

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar la velocidad de la serpiente
        reloj.tick(velocidad)

    # Mostrar pantalla de "Perdiste" con el puntaje final
    mostrar_pantalla_perdiste(longitud_serpiente - 1)

# Bucle principal que permite reiniciar el juego al perder
while True:
    juego()
