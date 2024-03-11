import pygame
import math

# Színek

hatter = (53, 113, 87)
feher = (172, 182, 198)
piros = (156, 12, 2)
fekete = (31, 29, 30)
zold = (53, 173, 84)
feher2 = (255, 255, 255)
sarga = (249, 194, 97)
sarga2 = (255, 252, 207)

tabla = [["P", "F", "P", "P", "F", "P", "P", "F", "P", "P", "F", "P", "Z"],
         ["F", "P", "F", "F", "P", "F", "F", "P", "F", "F", "P", "F", "Z"],
         ["P", "F", "P", "F", "F", "P", "P", "F", "P", "F", "F", "P", "Z"]]

elso_sor_szoveg = ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"]
masodik_sor_szoveg = ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"]
harmadik_sor_szoveg = ["1", "4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"]
sorhossz = len(elso_sor_szoveg)
# inicializálás
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Casino Rulette Game")
angle = 0
# Font objektum létrehozása
betutipus = pygame.font.Font(None, 30)


# game loop

def teglalap_kirajzolasa(screen, szin, x, y, szelesseg, magassag):
    # téglalap rajzolása
    pygame.draw.rect(screen, szin, (x, y, szelesseg, magassag))  # (x, y, width, height)


def szoveget_kirajzol(screen, szoveg, szoveg_x, szoveg_y, betumeret=30, szin=feher, betutipus=None, forgatas=False):
    if betutipus is None:
        betutipus = pygame.font.Font(None, betumeret)
    megjelenitendo_szoveg = betutipus.render(szoveg, True, szin)
    if forgatas:
        megjelenitendo_szoveg = pygame.transform.rotate(megjelenitendo_szoveg, 90)
    screen.blit(megjelenitendo_szoveg, (szoveg_x, szoveg_y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)

    screen.fill(hatter)

    # Egyenleg
    egyenleg = 100000
    tet = 0
    utolso_nyeremeny = ""
    pygame.draw.rect(screen, feher, (40, 20, 260, 100), 3)
    szoveget_kirajzol(screen, f"HUF: {egyenleg}", 45, 30, 10, feher, betutipus)
    szoveget_kirajzol(screen, f"Tét: {tet}", 45, 60, 10, feher, betutipus)
    szoveget_kirajzol(screen, f"Utolsó Nyeremény: {utolso_nyeremeny}", 45, 90, 10, feher, betutipus)

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

    # 1. sor számok
    for i in range(0, sorhossz):
        szoveget_kirajzol(screen, f"{elso_sor_szoveg[i]}", 165 + i * 50, 195, 50, feher, betutipus, forgatas=True)
    # 2. sor számok
    for i in range(0, sorhossz):
        szoveget_kirajzol(screen, f"{masodik_sor_szoveg[i]}", 165 + i * 50, 195 + 75, 50, feher, betutipus,
                          forgatas=True)
    # 3. sor számok
    for i in range(0, sorhossz):
        szoveget_kirajzol(screen, f"{harmadik_sor_szoveg[i]}", 165 + i * 50, 195 + 150, 50, feher, betutipus,
                          forgatas=True)

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
    # tucatok kirajzolása175 420
    for i in range(0, 3):
        szoveget_kirajzol(screen, f"{i + 1}. tucat", 200 * i + 200, 410, 10, feher, betutipus)

    # 5. sor

    pygame.draw.rect(screen, piros, (350, 454, 103, 56))
    pygame.draw.rect(screen, fekete, (455, 454, 96, 53))
    pygame.draw.rect(screen, feher, (150, 450, 603, 60), 3)
    pygame.draw.rect(screen, feher, (150, 450, 203, 60), 3)
    pygame.draw.rect(screen, feher, (150, 450, 403, 60), 3)
    pygame.draw.rect(screen, feher, (253, 450, 100, 60), 3)
    pygame.draw.rect(screen, feher, (453, 450, 100, 60), 3)
    pygame.draw.rect(screen, feher, (653, 450, 100, 60), 3)

    szoveget_kirajzol(screen, f"páratlan", 560, 470, 10, feher, betutipus)
    szoveget_kirajzol(screen, f"magas", 660, 470, 10, feher, betutipus)
    szoveget_kirajzol(screen, f"páros", 270, 470, 10, feher, betutipus)
    szoveget_kirajzol(screen, f"alacsony", 155, 470, 10, feher, betutipus)

    # oldalsó bizbasz
    pygame.draw.line(screen, feher, (115, 161), (161, 161), 2)
    pygame.draw.line(screen, feher, (115, 394), (260, 396), 2)
    pygame.draw.line(screen, feher, (115, 161), (105, 188), 2)
    pygame.draw.line(screen, feher, (115, 394), (105, 367), 2)
    pygame.draw.line(screen, feher, (105, 190), (105, 365), 2)
    pygame.draw.ellipse(screen, zold, (114, 245, 30, 72))  # 0

    # elozmeny

    pygame.draw.rect(screen, feher, (590, 20, 225, 50), 3)
    # Kerek

    logo = pygame.image.load("kepek/rlogo.png")
    pygame.display.set_icon(logo)
    kerek = pygame.image.load(("kepek/rkerek.png"))
    screen.blit(kerek, (375, 15))

    x = 440
    y = 80

    pygame.draw.circle(screen, feher, (x, y), 45, 2)
    golyocska = pygame.draw.circle(screen, feher2, (53 * math.cos(angle) + x, 53 * math.sin(angle) + y), 3)

    angle += 0.03

    # kiegeszíto&indito
    pygame.draw.rect(screen, sarga, (38, 520, 103, 50), 3)
    pygame.draw.rect(screen, sarga2, (42, 524, 95, 42))  # ismetles
    pygame.draw.rect(screen, sarga, (678, 520, 122, 50), 3)
    pygame.draw.rect(screen, sarga2, (682, 524, 113, 42))  # start
    pygame.draw.rect(screen, sarga, (149, 520, 96, 50), 3)
    pygame.draw.rect(screen, sarga2, (154, 524, 86, 42))  # vissza
    pygame.draw.rect(screen, sarga, (251, 520, 96, 50), 3)
    torles = pygame.draw.rect(screen, sarga2, (255, 524, 87, 42))  # torles
    szoveget_kirajzol(screen, f"törlés", 710, 537, 10, feher, betutipus)

    # zseton
    sargabet = pygame.image.load("kepek/sarga.png").convert_alpha()
    screen.blit(sargabet, (364, 524))

    piros_bet = pygame.image.load("kepek/piros.png").convert_alpha()
    screen.blit(piros_bet, (428, 524))

    zold_bet = pygame.image.load("kepek/zold.png").convert_alpha()
    screen.blit(zold_bet, (491, 524))

    kek_bet = pygame.image.load("kepek/kek.png").convert_alpha()
    screen.blit(kek_bet, (553, 524))

    fekete_bet = pygame.image.load("kepek/fekete.png").convert_alpha()
    screen.blit(fekete_bet, (615, 524))

    # eger
    eger = pygame.image.load("kepek/mousepos.png").convert_alpha()
    egkep = screen.blit(eger, (-100, -10))
    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    egkep.center = pos

    screen.blit(eger, egkep)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
