import pygame
import random

# Inicializalas
pygame.init()

# Szinek definicioja
FEHER = (255, 255, 255)
FEKETE = (0, 0, 0)
PIROS = (255, 0, 0)
ZOLD = (0, 255, 0)
SZINEK = [FEKETE, PIROS, ZOLD]
PIROS_SZAMOK = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
FEKETE_SZAMOK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
ZOLD_SZAMOK = [0]
# Képernyo beállítása
SZELESSEG, MAGASSAG = 800, 600
kepernyo = pygame.display.set_mode((SZELESSEG, MAGASSAG))
pygame.display.set_caption("Rulett")

# Betutipusok
betu = pygame.font.Font(None, 36)

# Jatekos egyenlege
egyenleg = 100


def szoveg_kirajzolasa(szoveg, betutipus, szin, felulet, x, y):
    szoveg_obj = betutipus.render(szoveg, True, szin)
    szoveg_teglalap = szoveg_obj.get_rect()
    szoveg_teglalap.topleft = (x, y)
    felulet.blit(szoveg_obj, szoveg_teglalap)


def main():
    global egyenleg

    fut = True
    tet_osszeg = 0
    tet_szin = None
    gep_tet_szin = None

    while fut:
        kepernyo.fill(FEHER)

        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                fut = False
            if esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_q:
                    fut = False
            elif esemeny.type == pygame.MOUSEBUTTONDOWN:
                # Bet gombok
                if piros_teglalap.collidepoint(esemeny.pos):
                    tet_szin = PIROS
                elif zold_teglalap.collidepoint(esemeny.pos):
                    tet_szin = ZOLD
                elif fekete_teglalap.collidepoint(esemeny.pos):
                    tet_szin = FEKETE
                # Tet beallitasa
                elif tiz_teglalap.collidepoint(esemeny.pos):
                    tet_osszeg += 10
                elif otven_teglalap.collidepoint(esemeny.pos):
                    tet_osszeg += 50
                elif szaz_teglalap.collidepoint(esemeny.pos):
                    tet_osszeg += 100
                elif torol_teglalap.collidepoint(esemeny.pos):
                    tet_osszeg = 0
                    tet_szin = None
                elif porgetes_teglalap.collidepoint(esemeny.pos):
                    if tet_osszeg > 0 and tet_szin:
                        porgetes_eredmeny = random.randint(0, 36)
                        if porgetes_eredmeny in PIROS_SZAMOK:
                            gep_tet_szin = PIROS
                        elif porgetes_eredmeny in FEKETE_SZAMOK:
                            gep_tet_szin = FEKETE
                        else:
                            gep_tet_szin = ZOLD
                        if tet_szin == gep_tet_szin:
                            if gep_tet_szin == FEKETE or gep_tet_szin == PIROS:
                                egyenleg += tet_osszeg
                            else:
                                egyenleg += tet_osszeg * 14
                        else:
                            # Egyebkent veszteseg
                            egyenleg -= tet_osszeg
                        # Tet alaphelyzetbe allitasa
                        tet_osszeg = 0
                        tet_szin = None

        # Gombok kirajzolasa
        tiz_teglalap = pygame.draw.rect(kepernyo, FEKETE, (20, 450, 80, 50))
        szoveg_kirajzolasa("10", betu, FEHER, kepernyo, 35, 460)

        otven_teglalap = pygame.draw.rect(kepernyo, FEKETE, (120, 450, 80, 50))
        szoveg_kirajzolasa("50", betu, FEHER, kepernyo, 135, 460)

        szaz_teglalap = pygame.draw.rect(kepernyo, FEKETE, (220, 450, 80, 50))
        szoveg_kirajzolasa("100", betu, FEHER, kepernyo, 225, 460)

        torol_teglalap = pygame.draw.rect(kepernyo, FEKETE, (320, 450, 80, 50))
        szoveg_kirajzolasa("Clear", betu, FEHER, kepernyo, 330, 460)

        piros_teglalap = pygame.draw.rect(kepernyo, PIROS, (450, 450, 80, 50))
        szoveg_kirajzolasa("Red", betu, FEHER, kepernyo, 470, 460)

        zold_teglalap = pygame.draw.rect(kepernyo, ZOLD, (550, 450, 80, 50))
        szoveg_kirajzolasa("Green", betu, FEHER, kepernyo, 560, 460)

        fekete_teglalap = pygame.draw.rect(kepernyo, FEKETE, (650, 450, 80, 50))
        szoveg_kirajzolasa("Black", betu, FEHER, kepernyo, 660, 460)

        porgetes_teglalap = pygame.draw.rect(kepernyo, FEKETE, (720, 200, 60, 60))
        szoveg_kirajzolasa("Spin", betu, FEHER, kepernyo, 720, 220)

        # Egyenleg kirajzolasa
        szoveg_kirajzolasa("Balance: ${}".format(egyenleg), betu, FEKETE, kepernyo, 20, 20)

        # Tet es tet szinek kirajzolasa
        szoveg_kirajzolasa("Bet: ${}".format(tet_osszeg), betu, FEKETE, kepernyo, 20, 80)
        if tet_szin:
            szoveg_kirajzolasa(
                "Bet Color: {}".format("Red" if tet_szin == PIROS else ("Green" if tet_szin == ZOLD else "Black")),
                betu, FEKETE, kepernyo, 20, 120)

        # Gep altal valasztott szin kirajzolasa
        if gep_tet_szin:
            szoveg_kirajzolasa("Machine Bet: {}".format(
                "Red" if gep_tet_szin == PIROS else ("Green" if gep_tet_szin == ZOLD else "Black")), betu, FEKETE,
                kepernyo, 20, 160)
            szoveg_kirajzolasa(f"Number:{porgetes_eredmeny}",betu,FEKETE,kepernyo,20,200)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
