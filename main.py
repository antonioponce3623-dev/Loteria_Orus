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
    screen_width, screen_height = 1280, 720

# Ahora creamos la ventana usando la resolución obtenida y la bandera NOFRAME
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption("Lotería Orus")

bg_color = (253, 248, 225)
yellow_color = (249, 216, 75)

# Cargar fonts
try:
    # font para LOTERIA
    font_loteria = pygame.font.Font('fonts/Oswald-Regular.ttf', 120) #120 es el tamaño
    # font para Orus
    font_orus = pygame.font.Font('fonts/GreatVibes-Regular.ttf', 150)
except FileNotFoundError:
    print("fonts, not founds in 'fonts/' folder. Using default fonts")
    # Using pygame default font
    font_loteria = pygame.font.Font(None, 150)
    font_orus = pygame.font.Font(None, 180)

# Render teh title texts
# The 'true; is for anti-aliasing (makes the text look smooth)
text_loteria_surface = font_loteria.render("LOTERIA", True, yellow_color)
text_orus_surface = font_orus.render("Orus", True, yellow_color)

# Get therectangles for positioning
text_loteria_rect = text_loteria_surface.get_rect(center=(screen_width / 2, screen_height / 2 - 80))
text_orus_rect = text_orus_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 50))

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

    screen.fill(bg_color)

    # Draw the title on the screen
    screen.blit(text_loteria_surface, text_loteria_rect)
    screen.blit(text_orus_surface, text_orus_rect)








    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()