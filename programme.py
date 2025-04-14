
import pygame

#variables du niveau
NB_TILES = 30   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=16       #hauteur du niveau
hauteur=16       #largeur du niveau
tiles=[]      #liste d'images tiles
#variables de gestion du pacman
pacX=1          #position x y du pacman dans le niveau
pacY=7
compteurBilles=0
Coeur=3
DirectionPacman=14
#variables de gestion du fantome
FRAMERATE_FANTOME= 100 #vitesse du fantome chiffre elevé = vitesse lente

NB_DEPLACEMENT_FANTOME =39   #le fantome se deplace sur 38 cases
positionFantome=1
frameRateCounterFantome=0
posfX=14     #position initiale du fantome
posfY=14

NB_DEPLACEMENT_FANTOME2 =48
posfX2 = 1     #position fantome 2
posfY2 = 14
positionFantome2 = 1.1
frameRateCounterFantome2 = 0
#definition du niveau

niveau=[[1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,6],
     [6,12,1,5,5,2,12,0,1,5,5,5,5,2,12,6],
     [6,12,6,0,0,6,12,1,4,12,12,12,12,12,12,6],
     [6,12,6,0,1,4,12,12,12,12,1,5,2,12,12,6],
     [6,12,6,1,4,12,12,3,5,5,4,12,6,12,12,6],
     [6,12,3,4,12,12,12,12,12,12,12,12,3,2,12,6],
     [6,0,12,12,12,12,12,12,12,1,2,12,12,6,12,6],
     [6,12,1,12,5,5,5,2,12,6,3,2,12,12,12,6],
     [6,12,6,12,12,12,12,6,12,3,5,8,5,2,12,6],
     [6,12,3,5,5,2,12,6,12,12,12,12,12,12,12,6],
     [6,12,12,12,12,6,12,3,12,5,5,5,5,4,12,6],
     [7,5,5,2,12,4,12,12,12,12,12,12,12,12,12,6],
     [6,12,12,12,12,12,12,1,2,12,23,5,5,24,12,6],
     [6,12,12,12,12,12,1,4,6,12,12,12,12,12,12,6],
     [3,5,5,5,5,5,4,0,3,5,5,5,5,5,5,4]]

fantome=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,17,16,15,14,13,0,0],
     [0,0,0,0,0,0,21,20,19,18,0,0,0,12,0,0],
     [0,0,0,0,0,0,22,0,0,0,0,0,0,11,10,0],
     [0,0,0,0,0,0,23,0,0,0,0,0,0,0,9,0],
     [0,0,0,0,0,0,24,25,26,0,0,0,0,0,8,0],
     [0,0,0,0,0,0,0,0,27,0,0,0,0,0,7,0],
     [0,0,0,0,0,0,0,0,28,0,0,0,0,0,6,0],
     [0,0,0,0,0,0,0,0,29,0,0,0,0,0,5,0],
     [0,0,0,0,0,0,0,0,30,0,0,0,0,0,4,0],
     [0,0,0,0,0,0,0,0,31,32,0,0,0,0,3,0],
     [0,0,0,0,0,0,0,0,0,33,0,0,0,0,2,0],
     [0,0,0,0,0,0,0,0,0,34,35,36,37,38,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

fantome2=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,20.1,21.1,22.1,23.1,24.1,25.1,0,0,0,0,0,0,0,0,0],
     [0,19.1,0,0,0,0,26.1,0,0,0,0,0,0,0,0,0],
     [0,18.1,0,0,0,0,27.1,0,0,0,0,0,0,0,0,0],
     [0,17.1,0,0,0,0,28.1,0,0,0,0,0,0,0,0,0],
     [0,16.1,0,0,0,30.1,29.1,0,0,0,0,0,0,0,0,0],
     [0,15.1,0,0,32.1,31.1,0,0,0,0,0,0,0,0,0,0],
     [0,14.1,0,34.1,33.1,0,0,0,0,0,0,0,0,0,8,0],
     [0,13.1,0,35.1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,12.1,0,36.1,37.1,38.1,39.1,0,0,0,0,0,0,0,0,0],
     [0,11.1,0,0,0,0,40.1,0,0,0,0,0,0,0,0,0],
     [0,10.1,9.1,8.1,7.1,0,41.1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,6.1,0,42.1,0,0,0,0,0,0,0,0,0],
     [0,47.1,46.1,45.1,5.1,44.1,43.1,0,0,0,0,0,0,0,0,0],
     [0,1.1,2.1,3.1,4.1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))



def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render("Score : " + str(score), True, (0, 255, 0))
    fenetre.blit(scoreAafficher,(240,500))

def afficheVie(Coeur):
    vieAafficher = font.render("Coeur : " + str(Coeur), True, (0, 255, 0))
    fenetre.blit(vieAafficher,(60,500))

def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coodFantome=x,y
            if fantome2[y][x]==position:
                coodFantome=x,y
    return coodFantome          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome(fantome):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome
    global positionFantome
    global posfX,posfY
    if frameRateCounterFantome==FRAMERATE_FANTOME:      #ralenti la viteese du fantome
        posfX,posfY=rechercheFantome(fantome,positionFantome)   #deballage du tuple coordonnées du fantome
        positionFantome+=1
        if positionFantome==NB_DEPLACEMENT_FANTOME:     #un tour est fait donc on passe à la 1ere position
            positionFantome=1
        frameRateCounterFantome=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[15],(posfX * TITLE_SIZE,posfY * TITLE_SIZE))
    frameRateCounterFantome+=1                          #incrémentation du compteur de vitesse


def deplaceFantome2(fantome2):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome2
    global positionFantome2
    global posfX2, posfY2
    if frameRateCounterFantome2 == FRAMERATE_FANTOME:  # ralenti la vitesse du fantome
        posfX2, posfY2 = rechercheFantome(fantome2, positionFantome2)  # déballage du tuple coordonnées du fantome
        positionFantome2 += 1
        if positionFantome2 >= NB_DEPLACEMENT_FANTOME2:  # un tour est fait donc on passe à la 1ère position
            positionFantome2 = 1.1
        frameRateCounterFantome2 = 0  # compteur de vitesse à zéro
    fenetre.blit(tiles[15], (posfX2 * TITLE_SIZE, posfY2 * TITLE_SIZE))
    frameRateCounterFantome2 += 1  # incrémentation du compteur de vitesse

chargetiles(tiles)              #chargement des images

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                posY = pacY - 1             #on deplace le pacman vituellement
                posX = pacX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile==13):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacY -= 1
                    DirectionPacman=29                               #on va en haut
                    print("deplacement possible",pacX,pacY)
                else:
                        print("deplacement impossible")
            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                print("down",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile==13):
                    pacY += 1
                    DirectionPacman=27                #on va en bas
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                pass
                posY = pacY              #on deplace le pacman virtuellement
                posX = pacX +1
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("right",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile==13):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX += 1
                    DirectionPacman=14                               #on va a gauche
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                pass
                posY = pacY              #on deplace le pacman vituellement
                posX = pacX -1
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("left",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile==13):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX -= 1
                    DirectionPacman=28                               #on va a droite
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            if (numeroTile==12):  #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la bille dans le niveau
                print("nouvelle bille")
            else:
                print("fond noir")
            if compteurBilles==116:
                loop=False
                print("Et c'est gagné!")



    if (posfX * TITLE_SIZE,posfY * TITLE_SIZE)==(pacX * TITLE_SIZE,pacY * TITLE_SIZE):
        Coeur=Coeur-1
        pacX=1
        pacY=7
    if (posfX2 * TITLE_SIZE,posfY2 * TITLE_SIZE)==(pacX * TITLE_SIZE,pacY * TITLE_SIZE):
        Coeur=Coeur-1
        pacX=1
        pacY=7
        fenetre.blit(tiles[14],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))
        print("Attention ! Vous perdez une vie")
    if Coeur==0:
        print("C'est perdu !")
        loop = False




    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    fenetre.blit(tiles[DirectionPacman],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))          #affiche la pacman et le score
    deplaceFantome(fantome)
    deplaceFantome2(fantome2) #mettre un commentaire pour desactiver le déplacement du fantome
    afficheScore(compteurBilles)
    afficheVie(Coeur)
    pygame.display.update() #mets à jour la fentre graphique
pygame.quit()

