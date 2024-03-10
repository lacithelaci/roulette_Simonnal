import pygame
import math
# Színek

hatter = (53, 113, 87)
feher = (172, 182, 198)
piros = (156, 12, 2)
fekete = (31, 29, 30)
zold = (53, 173, 84)
feher2 = (255, 255, 255)

tabla = [["P", "F", "P", "P", "F", "P", "P", "F", "P", "P", "F", "P", "Z"],
         ["F", "P", "F", "F", "P", "F", "F", "P", "F", "F", "P", "F", "Z"],
         ["P", "F", "P", "F", "F", "P", "P", "F", "P", "F", "F", "P", "Z"]]

# inicializálás
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Casino Rulette Game")
angle = 0
# game loop

def teglalap_kirajzolasa(screen, szin, x, y, szelesseg, magassag):
    # téglalap rajzolása
    pygame.draw.rect(screen, szin, (x, y, szelesseg, magassag))  # (x, y, width, height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)


    screen.fill(hatter)
    # tabla 1-3 sorának kirajzolasához a változók
    uj_sorkezdes = 0
    tabla_x_koordinata = 150
    tabla_y_koordinata = 160
    teglalap_szelessege = 52
    teglalap_hossza = 82

    # tábla 1-3 sorának kirajzolása
    for i in range(3):
        for y in range(0, len(tabla[0]) - 1):

            if tabla[i][y] == "P":
                pygame.draw.rect(screen, piros, (
                    tabla_x_koordinata + y * 50, tabla_y_koordinata, teglalap_szelessege, teglalap_hossza))

            else:
                pygame.draw.rect(screen, fekete, (
                    tabla_x_koordinata + y * 50, tabla_y_koordinata, teglalap_szelessege, teglalap_hossza))
            uj_sorkezdes += 1

        if uj_sorkezdes == 12:
            tabla_y_koordinata += 83

        if uj_sorkezdes == 24:
            tabla_y_koordinata += 77
            teglalap_hossza = 78

    # fehér vonalak kirajzolása
    feher_vonal_y = 160
    feher_vonal_uj_sor = 0

    for i in range(0, 3):
        if i == 1:
            feher_vonal_y += 79
        if i == 2:
            feher_vonal_y += 77

        for y in range(150, 800, 50):
            pygame.draw.rect(screen, feher, (y, feher_vonal_y, 52, 82), 3)
            feher_vonal_uj_sor += 1
    # 4. sor

    pygame.draw.rect(screen, feher, (150, 395, 203, 60), 3)
    pygame.draw.rect(screen, feher, (150, 395, 603, 60), 3)
    pygame.draw.rect(screen, feher, (150, 395, 403, 60), 3)
    # 5. sor

    pygame.draw.rect(screen, piros, (350, 454, 103, 56))
    pygame.draw.rect(screen, fekete, (455, 454, 96, 53))
    pygame.draw.rect(screen, feher, (150, 450, 603, 60), 3)
    pygame.draw.rect(screen, feher, (150, 450, 203, 60), 3)
    pygame.draw.rect(screen, feher, (150, 450, 403, 60), 3)
    pygame.draw.rect(screen, feher, (253, 450, 100, 60), 3)
    pygame.draw.rect(screen, feher, (453, 450, 100, 60), 3)
    pygame.draw.rect(screen, feher, (653, 450, 100, 60), 3)

    # oldalsó bizbasz
    pygame.draw.line(screen, feher, (115, 161), (161, 161), 2)
    pygame.draw.line(screen, feher, (115, 394), (260, 396), 2)
    pygame.draw.line(screen, feher, (115, 161), (105, 188), 2)
    pygame.draw.line(screen, feher, (115, 394), (105, 367), 2)
    pygame.draw.line(screen, feher, (105, 190), (105, 365), 2)
    pygame.draw.ellipse(screen, zold, (114, 245, 30, 72))  # 0
    # Egyenleg

    pygame.draw.rect(screen, feher, (40, 20, 260, 100), 3)
    # elozmeny

    pygame.draw.rect(screen, feher, (590, 20, 225, 50), 3)
    # Kerek

    logo = pygame.image.load("rlogo.png")
    pygame.display.set_icon(logo)
    kerek = pygame.image.load(("rkerek.png"))
    screen.blit(kerek, (375, 15))

    x = 440
    y = 80

    pygame.draw.circle(screen, feher, (x, y), 45, 2)
    golyocska = pygame.draw.circle(screen, feher2, (53 * math.cos(angle) + x, 53 * math.sin(angle) + y), 3)

    angle += 0.03
    pygame.display.update()
    clock.tick(60)

pygame.quit()
