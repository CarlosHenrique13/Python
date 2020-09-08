import pygame
import random
from player import Player
from Asteroide import Asteroide
from shot import Shot

# Inicializando o Pygame e criando a Janela
pygame.init()
display = pygame.display.set_mode([840,480])
pygame.display.set_caption("Meu Super Jogo 01")

# Groups
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()


player = Player(objectGroup)


# Music
pygame.mixer.music.load("data/awesomeness.wav")
pygame.mixer.music.play(-1)

# Sounds
shoot = pygame.mixer.Sound("data/SFX_Jump_01.wav")

gameLoop = True
gameover = False
time = 10
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newShot = Shot(objectGroup,shotGroup)
                    newShot.rect.center = player.rect.center


        #Update logic
        if not gameover:
            objectGroup.update()

            time += 1
            if time > 30:
                time = 0
                if random.random() < 0.3:
                    newAsteroid = Asteroide(objectGroup,asteroidGroup)
                    print("New Asteroide")

            collisions = pygame.sprite.spritecollide(player,asteroidGroup,False, pygame.sprite.collide_mask)

            if collisions:
                print("Gamer Over")
                gameover = True

            hits = pygame.sprite.groupcollide(shotGroup,asteroidGroup,True,True,pygame.sprite.collide_mask)

        # Draw:
        display.fill([255,255,255])
        objectGroup.draw(display)
        pygame.display.update()
