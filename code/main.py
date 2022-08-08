import pygame, sys
from settings import * 
from level import Level

class Game:
    def __init__(self): 
        
        window_title = 'Hi Ro :P'
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(window_title)
        self.clock = pygame.time.Clock() 

        self.level = Level()
        
    # init()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        self.level.toggle_menu()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
    # run()
# Game:
if __name__ == '__main__': # check if main file
    game = Game() # create instance of class
    game.run() # call run method in class
