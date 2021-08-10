import pygame

class Ship():
    """Class that controls user ship details"""
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set the ship starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load  the ship image and get its rect
        self.image = pygame.image.load("D:\Python\Python projects\Alien Invasion\images\ship.bmp")
        self.rect = self.image.get_rect()
        #get_rect()-get the image in rectangular shape 
        self.screen_rect = screen.get_rect()
        #get screen rectangular 

        #Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centerx is controls position of ship
        #places image at the center of screen
        self.rect.bottom = self.screen_rect.bottom
        #places image at the bottom of screen

        #Store decimal value for ship center as centerx only store int
        self.center = float(self.rect.centerx)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        """Updates ship's movement based on movement flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
