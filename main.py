import pygame, sys
import math
from game import Game
pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 60

#générer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)       #arrondir

#importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)       #arrondir
play_button_rect.y = math.ceil(screen.get_height() / 2)         #arrondir


#charger notre jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    #vérifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # détecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN: #touche appuyés
            #quelle touche a été utiisé
            game.pressed[event.key] = True
            #Détecter si la touche espace est pressé pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:   #touche relachés
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérifier pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)