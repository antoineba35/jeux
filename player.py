import pygame
from projectile import Projectile
import animation


#créer notre premiere classe qui va représenter notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100                                       #point de vie
        self.max_health = 100                                   #max point de vie
        self.attack = 15                                        #point d'attaque
        self.velocity = 5                                       #vitesse joueur
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()                       #localisation image a l'aide d'un rectangle qui encadre l'image
        self.rect.x = 400                                       #rectangle positionnement en x
        self.rect.y = 500                                       # rectangle positionnement en y

    def damage(self, amount):
        if self.health - amount > amount:
            # infliger les dégats
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.health = 0
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5]) #dessiner un rectangle

    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        # démarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur n'est pas en collision avec l'entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity