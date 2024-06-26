import sys
import pygame

from player import Player
from stage import Stage
from config import *
from menu import Menu

pygame.init()


screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)
pygame.display.set_caption("Geometoid")
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()


def main():
    ########################## PHASE 2 #########################
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    stage = Stage(STAGE_PADDING, screen, player)
    ############################################################
    
    menu = Menu(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player.alive == True:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player.fire = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    player.fire = False
                if event.type == pygame.USEREVENT:
                    stage.plan_round()
######################## PHASE 2 #############################
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    stage.invincible_timer = 200
            else:
                action = menu.handle_event(event)
                if action == "start_game":
                    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    stage = Stage(STAGE_PADDING, screen, player)
                    player.alive = True
##############################################################
                
        if player.alive == True:
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            screen.fill(WHITE)

            player.update(mouse, keys)
            stage.update(player)
            stage.draw(screen, font)
            player.draw(screen, font)

        else: 
            menu.draw()

        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    main()
