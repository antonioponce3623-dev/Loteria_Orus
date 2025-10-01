import pygame
import sys

# Inicializar Pygame
pygame.init()

#Optenemos la informacion del Display actual
try:
    info_display = pygame.display.Info()
    screen_width = info_display.current_w
    screen_height = info_display.current_h
except pygame.error as e:
    # Si falla (muy raro), volvemos a un tamaño seguro por defecto
    print(f"No se pudo obtener la información del display: {e}")
    screen_width, screen_height = 800, 600

# Ahora creamos la ventana usando la resolución obtenida y la bandera NOFRAME
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption("Lotería Orus")

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            # Si la tecla es ESCAPE
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 128, 0)) # Fondo verde
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()