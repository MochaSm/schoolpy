import pygame
import sys
import random
pygame.font.init()
WIDTH, HEIGHT = 800,500 
win = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.Font(None, 40, )
sec = []
BLACK = (0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)

def end(sec):
    win.fill(WHITE)
    text = font.render("Game Over press enter to start again or ESC to leave", True, BLACK)
    score_text = font.render(f"It took you: {sec[0]}s", True, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    win.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - score_text.get_height()//2 + 100))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
        main()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
def main():
    clock =pygame.time.Clock()
    x,y = 30,50
    speed =10
    coords =0
    z,w = 0,0
    
    last_event_time = 0
    circlepos = []
    


  
    Score =0
    start_ticks = pygame.time.get_ticks()
    def rand ():
        w = random.randint(0,480)
        z = random.randint(0,780)
        return z ,w
    
    FPS = 60
    z, w = rand()
    sec.clear()
    pygame.init()
    
    while True:
        keys = pygame.key.get_pressed()

        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        if seconds - last_event_time >= 1.5:
            z, w = rand()
            circlepos.append((z, w))
            last_event_time = seconds

        for a,b in circlepos:
            pygame.draw.circle(win,YELLOW,(a,b),10)
            if player.collidepoint(a,b):
                Score += 1
                circlepos.remove((a,b))
       
         
        
        
        pygame.draw.rect(win,RED,player)
        pygame.draw.circle(win,YELLOW,(z,w),10) 
        
        if Score >= 10:
            sec.append(round(seconds,1))
            end(sec)
        time = font.render(f"{round(seconds,1)}s", True, WHITE)
        score_text = font.render(f"Score:{Score}", True, WHITE)
        win.blit(time, (time.get_width(),time.get_height()))
        win.blit(score_text, (score_text.get_width()+50,  score_text.get_height() ))
            
        pygame.display.update()
    
if __name__ == "__main__":

    main()
