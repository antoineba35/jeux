import pygame
import random

# créer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, commet_event):
        super().__init__()
        #définir l'image de la comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 400)
        self.commet_event = commet_event

    def remove(self):
        # retirer la boule de feu
        self.commet_event.all_comet.remove(self)
        #jouer le son
        self.commet_event.game.sound_manager.play('meteorite')

        # vérifier si le nombre de comete est 0
        if len(self.commet_event.all_comet) == 0:
            # remettre la barre a zero
            self.commet_event.reset_percent()
            #apparaitre les 2 premiers monstres
            self.commet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        #elle ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()

            # si il n'y a plus de boule de feu sur le jeu
            if len(self.commet_event.all_comet) == 0:
                # remettre la jauge au depart
                self.commet_event.reset_percent()
                self.commet_event.fall_mode = False

        # vérifier si la boule de feu touche le joueur
        if self.commet_event.game.check_collision(
            self, self.commet_event.game.all_player
        ):
            # retirer la boule de feu
            self.remove()
            # subir 20 points de dégats
            self.commet_event.game.player.damage(20)