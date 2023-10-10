import pygame,sys,time  #Importing the python library for the game development 
from settings import *
from sprites import *


class Game:
    def __init__(self) -> None:
        # setup of the main screen of the game
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('FLAPPY BIRD REMASTERED')
        self.clock=pygame.time.Clock()

        # Sprite groups
        
        # This is the plane group


        self.all_sprites=pygame.sprite.Group()

        # scale factor
        max_height=pygame.image.load('./graphics/environment/background.png').get_height()
        self.scale_factor=max_height/WINDOW_HEIGHT


        BG(self.all_sprites,self.scale_factor)
        Ground(self.all_sprites,self.scale_factor)
        self.plane=Plane(self.all_sprites,self.scale_factor)
        



        # this is the obstacles sprite group
        self.collisonSprites=pygame.sprite.Group()


        # timer
        self.obstacle_timer=pygame.USEREVENT+1
        pygame.time.set_timer(self.obstacle_timer,1400)
    def run(self):
        last_time=time.time()
        while True:
            # Delta Time
            dt=time.time()-last_time


            # Event loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.plane.jump()
                if event.type==self.obstacle_timer:
                    Obstacles(self.all_sprites,self.scale_factor)
            

            self.display_surface.fill('pink')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)

       
            
            #Game logic

            pygame.display.update()
            self.clock.tick(FRAME_RATE)
        
     





if __name__=='__main__':
    game=Game()
    game.run()