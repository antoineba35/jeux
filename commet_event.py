import pygame
from commet import Comet

# créer uhe classe pour gérer cette évenement
class CometFallEvent:

    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        # définir un groupe de sprite pour stocker les cometes
        self.all_comet = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # apparaitre la premiere boule de feu
            self.all_comet.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'évenement est otalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True   # activer l'évenement

    def update_bar(self, surface):

        #ajouter du poucentage à la barre
        self.add_percent()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() - 20,   # l'axe des y
            surface.get_width(),    # longeur de la fenetre
            10 # epaisseur de la barre
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longeur de la fenetre
            10  # epaisseur de la barre
        ])