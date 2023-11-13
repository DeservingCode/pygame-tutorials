import pygame

#used to close game loop
from sys import exit

#Starts pyGame 
pygame.init()


#Create Window / Display surface 
width = 1398
height = 645
screen = pygame.display.set_mode((width,height))

#Set Window Name
pygame.display.set_caption('Runner')

#setting framerate by creating clock - (Easy to set ceiling. hard to set floor)
clock = pygame.time.Clock()

#Creating surfaces creates items. Then use BLIT to attach to display surface
#3 Types of Surfaces - Block / Image / Text

# 1.Block Surface
dirt_fill = pygame.Surface((width,200))
dirt_fill.fill((43,24,12))

ground_fill = pygame.Surface((width,20))
ground_fill.fill((90,79,62))

bg_fill = pygame.Surface((width,100))
bg_fill.fill((56,86,97))

# 2. Image Surface 
# !! Remember to .covert_alpha to ensure images are convered to comething pygame can manage
sky_surface = pygame.image.load('graphics/back.png').convert_alpha()
foreground_surface = pygame.image.load('graphics/middle.png').convert_alpha()

#Make a sprite Move by calling variable and them change the variable
frog_sprite = pygame.image.load('graphics/frog-idle-1.png').convert_alpha()
frog_xloc = 0
frog_rectangle = frog_sprite.get_rect(midbottom=(width/.5,500))
frog_speed = 5



#Make a player image and create a rectangle around it player-idle-1.png
player_sprite = pygame.image.load('graphics/player-idle-1.png').convert_alpha()
player_rectangle = player_sprite.get_rect(midbottom=(width/2,500))
player_gravity = 0

#3. Text Surface - 
#1. Create font | 2. Write text to a Surface | 3. Blit Surface

#1. Create Font - Font(Font Type, Font Size)
test_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 50)
#2. Create Surface render("What to say", AntiAlias, Color) 
text_surface = test_font.render("My Game", False, 'Black')
text_rectangle = text_surface.get_rect(midbottom=(width/2,height/5))




#keep code running with while true loop "The Game Loop"
while True:

    #checking to see if any events are happening in the code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos): print ('Mouse Collision!')
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('SpacBar Down')
                player_gravity -= 20
                player_rectangle.bottom -= 10

                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print('SpacBar Up')
                


    #Blit (what surface, (where XY)) 0,0 is top left corner
    screen.blit(sky_surface,(0,0))
    screen.blit(foreground_surface,(0,105))
    screen.blit(dirt_fill,(0,500))
    screen.blit(bg_fill,(0,400))
    screen.blit(ground_fill,(0,500))


    player_gravity += 1
    player_rectangle.y += player_gravity
    
    if player_rectangle.bottom >= 500 : 
        player_rectangle.bottom = 501
        player_gravity = 0
 
    screen.blit(player_sprite,player_rectangle)
    print(player_rectangle.bottom)
    
    
        
    
    
    screen.blit(frog_sprite,frog_rectangle)
    frog_rectangle.x -= frog_speed
    if frog_rectangle.x < -40:
        frog_rectangle.x = 1400
        player_sprite = pygame.transform.flip(player_sprite, True, False)

    
    if frog_rectangle.x > 1400:
        frog_rectangle.x = -40
        player_sprite = pygame.transform.flip(player_sprite, True, False)

    pygame.draw.rect(screen,'pink',text_rectangle)

    screen.blit(text_surface,text_rectangle)


    if player_rectangle.colliderect(frog_rectangle):
        
        print('Collision!')
        frog_speed *= -1
        frog_sprite = pygame.transform.flip(frog_sprite, True, False)
        


    #Continuously update display
    pygame.display.update()
    clock.tick(60)