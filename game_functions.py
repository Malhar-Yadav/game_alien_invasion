import sys
import pygame


def check_KeyDown_events(event, ship):
    """Responds to KeyPress Events change"""
    if event.key == pygame.K_RIGHT:
            ship.moving_right = True
    elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_KeyUp_events(event, ship):
    """Responds to KeyRelease Events"""
    if event.key == pygame.K_RIGHT:
            ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # moving ship to right or left
        elif event.type == pygame.KEYDOWN:
            check_KeyDown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_KeyUp_events(event, ship)

            


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and fill to the new screen"""
    # redraw the screen each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

