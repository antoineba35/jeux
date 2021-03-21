import pygame
from player import Player
from monster import *
from commet_event import CometFallEvent
from sounds import SoundManager


#créer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        # définir si notre jeu a commencer ou non
        self.is_playing = False
        #générer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)          #appel de la fonction Player
        self.all_player.add(self.player)
        # generer l'evenement de comete
        self.commet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gérer le son
        self.sound_manager = SoundManager()
        # mettre le score a 0
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points


    def game_over(self):
        # remettre le jeu a neuf, retirer les monstrers, remettre le joueur a 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):

        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score :{self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie de mon joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'évenement du jeu
        self.commet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # recupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #récupérer les cometes de notre jeu
        for commet in self.commet_event.all_comet:
            commet.fall()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de commete
        self.commet_event.all_comet.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():  # longueur max de la fenetre
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))