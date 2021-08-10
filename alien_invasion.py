#import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gfunc


def run_game():
    # Initializa pygame, Settings and screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # we create a game window using attribute from Settings module
    # window title
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        gfunc.check_events(ship)
        ship.update()
        gfunc.update_screen(ai_settings, screen, ship)


run_game()
