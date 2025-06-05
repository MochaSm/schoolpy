import pygame
import sys
import random
import time
WIDTH, HEIGHT = 800,500 
BLACK = (0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
def main():
    FPS = 60
    pygame.init()
    clock =pygame.time.Clock()
    x,y = 30,50
    speed =10
    coords =0
    z,w = 0,0
    count=0
    win = pygame.display.set_mode((WIDTH,HEIGHT))

    def end():
        pygame.draw.rect(win,RED,player)


    def rand ():
        w = random.randint(0,480)
        z = random.randint(0,780)
        return z ,w
    
    Score =0
    start_ticks = pygame.time.get_ticks()
    while Score !=10:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if y> 0:
                y-=speed
        if keys[pygame.K_DOWN]:
            if y<480:
                y+=speed
        if keys[pygame.K_LEFT]:
            if x> 0:
                x-=speed
        if keys[pygame.K_RIGHT]:
            if x < 780:
                x+=speed
        win.fill(BLACK)
        player = pygame.Rect(x,y,20,20)
        seconds= (pygame.time.get_ticks()-start_ticks)/1000

        if seconds % 5000 == 0:
            z,w = rand()
            count+=1
    


        pygame.display.set_caption(str(seconds) +" " + str(count))
        pygame.draw.rect(win,RED,player)

        pygame.draw.circle(win,YELLOW,(z,w),10) 
        pygame.display.update()
    
if __name__ == "__main__":

    main()