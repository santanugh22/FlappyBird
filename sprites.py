import pygame


from settings import *
from random import randint


class BG(pygame.sprite.Sprite):
    def __init__(self,group,scale) -> None:
        super().__init__(group)


        bg_image=pygame.image.load('./graphics/environment/background.png')
        image_height=bg_image.get_height()*scale
        image_width=bg_image.get_width()*scale

        full_sized_image=pygame.transform.scale(bg_image,(image_width,image_height))
        self.image=pygame.Surface((image_width*2,image_height))
        self.image.blit(full_sized_image,(0,0))
        self.image.blit(full_sized_image,(image_width,0))

        self.rect=self.image.get_rect(topleft=(0,0))
        self.pos=pygame.math.Vector2(self.rect.topleft)
    def update(self,dt):
        self.pos.x-=dt*0.3
     
        if self.rect.centerx<=0:
            self.pos.x=0
        self.rect.x=round(self.pos.x)





class Ground(pygame.sprite.Sprite):
    def __init__(self,groups,scale) -> None:
        super().__init__(groups)


        ground_image=pygame.image.load('./graphics/environment/ground.png').convert_alpha()
        self.image=pygame.transform.scale(ground_image,pygame.math.Vector2(ground_image.get_size())*scale)
        self.rect=self.image.get_rect(bottomleft=(0,WINDOW_HEIGHT))
        self.pos=pygame.math.Vector2(self.rect.topleft)
    def update(self,dt):
        self.pos.x -=0.3*dt
        if self.rect.centerx<=0:
            self.pos.x=0
        self.rect.x=round(self.pos.x)



class Plane(pygame.sprite.Sprite):
    def __init__(self,group,scale_factor):
        super().__init__(group)

        # image
        self.import_frames(scale_factor)
        self.frame_index=0
        self.image=self.frames[self.frame_index]


        # rect
        self.rect=self.image.get_rect(midleft=(WINDOW_WIDTH/5,WINDOW_HEIGHT/2))
        self.pos=pygame.math.Vector2(self.rect.topleft)

        self.gravity=0.1
        self.direction=0
        
    def import_frames(self,scale_factor):
        self.frames=[]
        for i in range(3):
            surf=(pygame.image.load(f'./graphics/plane/red{i}.png'))
            scaled_surf=pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size())*scale_factor)
            self.frames.append(scaled_surf)
    def apply_gravity(self,dt):
        self.direction+=self.gravity
        self.pos.y+=self.direction
        self.rect.y=round(self.pos.y)
    def jump(self):
        self.direction=-5


    def animate(self):
        self.image=self.frames[randint(0,len(self.frames)-1)]

    def rotate(self,dt):
        self.image=pygame.transform.rotozoom(self.image,-self.direction,1)
    
    def update(self,dt):

        self.apply_gravity(dt)
        self.animate()
        self.rotate()




