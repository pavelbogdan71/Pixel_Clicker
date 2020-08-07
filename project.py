import pygame
import os
import pygame_menu



pygame.font.init()

imagine_casuta = pygame.image.load("imagine.png")
imagine_help = pygame.image.load("help_icon.png")
imagine_help = pygame.transform.scale(imagine_help, (30, 30))
casuta_help = pygame.image.load("imagine_help.png")

# setare icon
gameIcon = pygame.image.load("coin.jpg")
pygame.display.set_icon(gameIcon)

# culori
galben = (255, 255, 0)
portocaliu = (255, 153, 0)
negru = (0, 0, 0)
background_color = (0, 204, 122)
culoare_turcoaz = (1, 36, 69)

# setam suprafata de joc

pygame.init()

width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Clicker")
screen.fill(background_color)



# verifica daca numarul trebuie prescurtat cu K
def verificaDacaNrK(numar):
    if numar >= 1000 and numar < 1000000:
        return True
    else:
        return False
# verifica daca numarul trebuie prescurtat cu M
def verificaDacaNrM(numar):
    if numar >= 1000000:
        return True
    else:
        return False

# textul care arata cantitatea de bani
def afisareCantitateBani(cantitate):
    if verificaDacaNrK(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("Money:" + str(round(cantitate/1000, 2)) + "K", True, culoare_turcoaz)
        screen.blit(img, (20, 20))
    elif verificaDacaNrM(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("Money:" + str(round(cantitate / 1000000, 2)) + "M", True, culoare_turcoaz)
        screen.blit(img, (20, 20))
    else:
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("Money:"+str(round(cantitate, 2)), True, culoare_turcoaz)
        screen.blit(img, (20, 20))

def afisareBaniPeSecunda(cantitate):
    if verificaDacaNrK(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPS:" + str(round(cantitate/1000, 2)) + "K", True, culoare_turcoaz)
        screen.blit(img, (790, 20))
    elif verificaDacaNrM(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPS:" + str(round(cantitate / 1000000, 2)) + "M", True, culoare_turcoaz)
        screen.blit(img, (790, 20))
    else:
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPS:" + str(round(cantitate, 2)), True, culoare_turcoaz)
        screen.blit(img, (790, 20))

def afisareBaniPeCoin(cantitate):
    if verificaDacaNrK(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("MPC:" + str(round(cantitate/1000, 2)) + "K", True, culoare_turcoaz)
        screen.blit(img, (550, 20))
    elif verificaDacaNrM(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("MPC:" + str(round(cantitate/1000000, 2)) + "M", True, culoare_turcoaz)
        screen.blit(img, (550, 20))
    else:
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("MPC:" + str(round(cantitate, 2)), True, culoare_turcoaz)
        screen.blit(img, (550, 20))

def afisareBlocksPerClick(cantitate):
    if verificaDacaNrK(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPC:" + str(round(cantitate/1000, 2)) + "K", True, culoare_turcoaz)
        screen.blit(img, (310, 20))
    elif verificaDacaNrM(cantitate):
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPC:" + str(round(cantitate/1000000, 2)) + "M", True, culoare_turcoaz)
        screen.blit(img, (310, 20))
    else:
        font = pygame.font.Font("font8BIT.ttf", 30)
        img = font.render("BPC:" + str(round(cantitate, 2)), True, culoare_turcoaz)
        screen.blit(img, (310, 20))

def afisareHelp(button):
    run = True
    font = pygame.font.Font("font8BIT.ttf", 15)
    font.set_bold(1)
    font.render("In this game your goal it's to make 1B money", True, culoare_turcoaz)
    while run:
        screen.blit(casuta_help, (200, 130))

        screen.blit(font.render("In this game your goal it's to make 1B (1000M) money", True, culoare_turcoaz), (230, 160))
        screen.blit(font.render("BPC - block's you make every click", True, culoare_turcoaz), (230, 200))
        screen.blit(font.render("MPC - amount of money you make when you complete a coin", True, culoare_turcoaz), (230, 220))
        screen.blit(font.render("BPS - block's you make every second", True, culoare_turcoaz), (230, 240))
        screen.blit(font.render("You can buy upgrades to make money faster", True, culoare_turcoaz), (230, 260))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # buton pentru help
                if button.collidepoint(mouse_pos[0], mouse_pos[1]):
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()

def game(index):
    # matricea banului  (276 pixeli colorati cu portocaliu sau galben)
    matrice = [
        ['n', 'n', 'n', 'n', 'n', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'p', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'p', 'n', 'n', 'n'],
        ['n', 'n', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'n', 'n'],
        ['n', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'n'],
        ['p', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'p', 'p', 'p', 'p', 'p', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p'],
        ['p', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'p', 'p', 'p', 'p', 'p', 'g', 'g', 'g', 'g', 'p'],
        ['n', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'n'],
        ['n', 'n', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'n', 'n'],
        ['n', 'n', 'n', 'p', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'p', 'p', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'n', 'n', 'n', 'n', 'n']
    ]


    # parcurgerea matricei cu banul
    """"
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if (matrice[i][j] == 'p') and (i == index[0]) and (j == index[1]):
                pygame.draw.rect(screen, portocaliu, (j*10+100, i*10+100, 10, 10))

            if (matrice[i][j] == 'g') and (i == index[0]) and (j == index[1]):
                pygame.draw.rect(screen, galben, (j*10+100, i*10+100, 10, 10))

            if (matrice[i][j] == 'n') and (i == index[0]) and (j == index[1]):
                pygame.draw.rect(screen, negru, (j * 10+100, i * 10+100, 10, 10))
    """
    vectorMatrice = []
    vectorCoordonate = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if (matrice[i][j] == 'p') or (matrice[i][j] == 'g'):
                vectorMatrice.append(matrice[i][j])
                vectorCoordonate.append((i, j))

    for i in range(len(vectorMatrice)):
        if vectorMatrice[i] == 'p' and (i <= index[1]+(index[0]*18)):
            pygame.draw.rect(screen, portocaliu, (vectorCoordonate[i][1]*20 + 320,vectorCoordonate[i][0]*20 + 190, 20, 20))

        if vectorMatrice[i] == 'g' and (i <= index[1]+(index[0]*18)):
            pygame.draw.rect(screen, galben, (vectorCoordonate[i][1]*20 + 320, vectorCoordonate[i][0]*20 + 190, 20, 20))


def main():
    run = True
    # setam valorile maxime ale matricei
    index = [0, 0]
    max = 276
    bani = 0
    baniPeTura = 1
    baniPeSecunda = 0
    # viteza de desenare
    # blocks per click
    speed = 1
    # variabile pentru upgradeuri
    pretMPC = 2
    pretBPS = 5
    # Blocks Per Click
    pretBPC = 5
    # 0.2 1 0.001
    incBPC = 0.2
    incMPC = 1
    incBPS = 0.001

    button = pygame.Rect(960, 80, 30, 30)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #apasa click pentru incrementare
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                index[1] = index[1] + speed
                # buton pentru help
                if button.collidepoint(mouse_pos[0], mouse_pos[1]):
                    afisareHelp(button)

            # apasa tasta 1 pentru upgrade
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1) and (bani >= pretMPC):
                    baniPeTura = baniPeTura + incMPC
                    incMPC = incMPC * 1.2
                    bani = bani - pretMPC
                    pretMPC = pretMPC * 1.5
                if (event.key == pygame.K_2) and (bani >= pretBPC):
                    speed = speed + incBPC
                    incBPC = incBPC * 1.2
                    bani = bani - pretBPC
                    pretBPC = pretBPC * 1.45
                if (event.key == pygame.K_3) and (bani >= pretBPS):
                    baniPeSecunda = baniPeSecunda + incBPS
                    incBPS = incBPS * 1.2
                    bani = bani - pretBPS
                    pretBPS = pretBPS * 1.65


        index[1] = index[1] + baniPeSecunda
        if index[1] == 18:
            index[0] = index[0] + speed
            index[1] = 0

        # afisare informatii bani
        pygame.display.flip()
        screen.fill(background_color)
        afisareCantitateBani(bani)
        afisareBaniPeSecunda(baniPeSecunda*100)
        afisareBaniPeCoin(baniPeTura)
        afisareBlocksPerClick(speed)



        #casuta de sus cu statusurile
        pygame.draw.rect(screen, culoare_turcoaz, (10, 10, 980, 50), 6)

        # afisare casuta help
        screen.blit(imagine_help, (960, 80))

        # afisare casuta upgrade BPC
        # pygame.draw.rect(screen, galben, (30, 630, 300, 150))
        font = pygame.font.Font("font8BIT.ttf", 20)
        font.set_bold(1)
        screen.blit(imagine_casuta, (30, 630))
        if verificaDacaNrM(incMPC):
            screen.blit(font.render('Upgrade MPC:+' + str(round(incMPC/1000000, 2))+"M", True, culoare_turcoaz), (50, 640))
        elif verificaDacaNrK(incMPC):
            screen.blit(font.render('Upgrade MPC:+' + str(round(incMPC/1000, 2))+"K", True, culoare_turcoaz), (50, 640))
        else:
            screen.blit(font.render('Upgrade MPC:+' + str(round(incMPC, 2)), True, culoare_turcoaz), (50, 640))

        screen.blit(font.render('Press 1 to upgrade ', True, culoare_turcoaz), (50, 690))

        if verificaDacaNrK(pretMPC):
            screen.blit(font.render('Upgrade cost:' + str(round(pretMPC/1000, 2))+"K", True, culoare_turcoaz), (50, 740))
        elif verificaDacaNrM(pretMPC):
            screen.blit(font.render('Upgrade cost:' + str(round(pretMPC/1000000, 2))+"M", True, culoare_turcoaz), (50, 740))
        else:
            screen.blit(font.render('Upgrade cost:' + str(round(pretMPC, 2)), True, culoare_turcoaz), (50, 740))

        # afisare casuta upgrade BPC
        # pygame.draw.rect(screen, galben, (350, 630, 300, 150))
        font = pygame.font.Font("font8BIT.ttf", 20)
        font.set_bold(1)
        screen.blit(imagine_casuta, (350, 630))
        if verificaDacaNrK(incBPC):
            screen.blit(font.render('Upgrade BPC:+' + str(round(incBPC/1000, 2))+"K", True, culoare_turcoaz), (370, 640))
        elif verificaDacaNrM(incBPC):
            screen.blit(font.render('Upgrade BPC:+' + str(round(incBPC/1000000, 2))+"M", True, culoare_turcoaz), (370, 640))
        else:
            screen.blit(font.render('Upgrade BPC:+' + str(round(incBPC, 2)), True, culoare_turcoaz), (370, 640))

        screen.blit(font.render('Press 2 to upgrade ', True, culoare_turcoaz), (370, 690))

        if verificaDacaNrK(pretBPC):
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPC/1000, 2))+"K", True, culoare_turcoaz), (370, 740))
        elif verificaDacaNrM(pretBPC):
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPC/1000000, 2))+"M", True, culoare_turcoaz), (370, 740))
        else:
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPC, 2)), True, culoare_turcoaz), (370, 740))

        #afisare casuta upgrade BPS
        # pygame.draw.rect(screen, galben, (670, 630, 300, 150))
        font = pygame.font.Font("font8BIT.ttf", 20)
        font.set_bold(1)
        screen.blit(imagine_casuta, (670, 630))

        if verificaDacaNrK(incBPS):
            screen.blit(font.render('Upgrade BPS:+' + str(round(incBPS * 100 / 1000, 2))+"K", True, culoare_turcoaz), (690, 640))
        elif verificaDacaNrM(incBPS):
            screen.blit(font.render('Upgrade BPS:+' + str(round(incBPS * 100 / 1000000, 2))+"M", True, culoare_turcoaz), (690, 640))
        else:
            screen.blit(font.render('Upgrade BPS:+' + str(round(incBPS * 100, 2)), True, culoare_turcoaz), (690, 640))

        screen.blit(font.render('Press 3 to upgrade ', True, culoare_turcoaz), (690, 690))

        if verificaDacaNrK(pretBPS):
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPS/1000, 2))+"K", True, culoare_turcoaz), (690, 740))
        elif verificaDacaNrM(pretBPS):
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPS/1000000, 2))+"M", True, culoare_turcoaz), (690, 740))
        else:
            screen.blit(font.render('Upgrade cost:' + str(round(pretBPS, 2)), True, culoare_turcoaz), (690, 740))




        #verifica cand se termina randul si apoi cand se termina toate randurile
        if index[0] < 18:
            game(index)
        if index[0]*18+index[1] > 261:
            # screen.fill((70, 70, 70))
            pygame.display.update()
            index[1] = 0
            index[0] = 0
            bani = bani + baniPeTura

        if bani >= 1000000000:
            run = False
        pygame.display.update()
    run = True
    while run:
        screen.fill(background_color)
        font = pygame.font.Font("font8BIT.ttf", 50)
        font.set_bold(1)
        screen.blit(font.render("Congratulations !!", True, culoare_turcoaz), (150, 200))
        screen.blit(font.render("You finish the game !!", True, culoare_turcoaz), (150, 300))
        pygame.display.update()

# incepere joc
def start_the_game():
    menu.clear()
    main()


#definim tema meniului
mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
mytheme.title_background_color = (0, 0, 0)
mytheme.widget_font = pygame_menu.font.FONT_8BIT
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
mytheme.widget_shadow = True
mytheme.widget_shadow_color = (169, 169, 169)
mytheme.widget_font_size = 55




#setam meniul
menu = pygame_menu.Menu(800, 1000, 'Welcome', theme=mytheme)


menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)