import pygame
from sys import exit
from random import randint
import math

jetup = 0
shoot = 0
missilexv = 0
enemycoming = 0
speed = 10
max_speed = 30
min_speed = 10
lives = 3
cloud1_coming = 0
cloud2coming = 0
cloud1reset = 0
redheight = 0
greenheight = 0
blueheight = 0
up_speed = 0
angle = 0
jet_angle = 0
angle_increment = 0
enemy_angle = 0
offsetspeed = 10

move_left = False
move_right = False
move_up = 0
move_down = False   

pygame.init()
screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption('Moon Explorer')
clock = pygame.time.Clock()


sky_surf = pygame.display.set_mode((2000, 1200))
sky_rect = sky_surf.get_rect(center = (1000, 600))

cloud1_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/cloud1.png').convert_alpha()
cloud1_surf = pygame.transform.scale(cloud1_surf1, (640, 400))
cloud1_rect = cloud1_surf.get_rect(midleft = (2100, 400))

cloud2_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/cloud2.png').convert_alpha()
cloud2_surf = pygame.transform.scale(cloud2_surf1, (640, 400))
cloud2_rect = cloud2_surf.get_rect(midleft = (2100, 400))

cloud3_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/cloud2.png').convert_alpha()
cloud3_surf = pygame.transform.scale(cloud2_surf1, (640, 400))
cloud3_rect = cloud2_surf.get_rect(midleft = (2100, 400))    



jet_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/fighter jet.png').convert_alpha()
jet_surf =  pygame.transform.scale(jet_surf1, (120, 40))
jet_rect = jet_surf.get_rect(center = (800, 600))

missile_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/missile.png').convert_alpha()
missile_surf = pygame.transform.scale(missile_surf1, (35, 12))
missile_rect = missile_surf.get_rect(center = (200, 600))

enemy_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/enemy.png').convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf1, (100, 36))
enemy_rect = enemy_surf.get_rect(center = (-50, 600))

speedomiter_surf1 = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/speedomiter.png').convert_alpha()
speedomiter_surf = pygame.transform.scale(speedomiter_surf1, (240, 165))
speedomiter_rect = speedomiter_surf.get_rect(center = (1600, 1100))

heartone_surf = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/heart.png').convert_alpha()
heart1_surf = pygame.transform.scale(heartone_surf, (80, 80))
heart1_rect = heart1_surf.get_rect(center = (100, 1100))

hearttwo_surf = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/heart.png').convert_alpha()
heart2_surf = pygame.transform.scale(hearttwo_surf, (80, 80))
heart2_rect = heart2_surf.get_rect(center = (200, 1100))

heartthree_surf = pygame.image.load('/Users/tobybrett/Documents/python/Python moon game/graphics/heart.png').convert_alpha()
heart3_surf = pygame.transform.scale(heartthree_surf, (80, 80))
heart3_rect = heart3_surf.get_rect(center = (300, 1100))



mph_font = pygame.font.Font(None, 70)
mphtext_surf = mph_font.render('mph', False, (225, 225, 225))
mphtext_rect = mphtext_surf.get_rect(center = (1730, 1120)) 

sky_rect = sky_surf.get_rect(topleft = (0, 0))

def calculate_angle(x1, y1, x2, y2):
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return angle

colliding = 0

temp_acc = 1     
 
while True:

    #EVERYTHING WHICH MOVES
    
    red = 79 + redheight
    green = 176 + greenheight
    blue = 240 + blueheight
    pygame.draw.rect(sky_surf, (red, green, blue), sky_rect)

    
    speed_font = pygame.font.Font(None, 200)

    speedtext_surf = speed_font.render(str(math.trunc(speed*10)), False, (225, 225, 225))
    speedtext_rect = speedtext_surf.get_rect(center = (1560, 1100)) 


    screen.blit(speedomiter_surf, speedomiter_rect)
    screen.blit(mphtext_surf, mphtext_rect)
    screen.blit(speedtext_surf, speedtext_rect)

    if lives >= 1:
        screen.blit(heart1_surf, heart1_rect)
        if lives >= 2:
            screen.blit(heart2_surf, heart2_rect)
            if lives == 3:
                screen.blit(heart3_surf, heart3_rect)


    if enemy_rect.colliderect(jet_rect):    
        if colliding == 0:
            lives -= 1
            colliding = 1

              
    if colliding == 1:
        if enemy_rect.colliderect(jet_rect) == False:
            colliding = 0
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if shoot == 0:
                    shoot = 1
                    permjetcentre = jetcentre
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True        
            if event.key == pygame.K_a:
                move_left = True
                
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_right = False
                    temp_acc = 0       
                if event.key == pygame.K_a:
                    move_left = False
                    temp_acc = 0

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                move_up = 1
            if event.key == pygame.K_s:
                move_up = -1
                
        if event.type == pygame.KEYUP:
            if event.type != pygame.KEYDOWN:
                angle_increment = 0
                if event.key == pygame.K_w:
                    move_up = 0   
                if event.key == pygame.K_s:
                    move_up = 0


    #TRAJECTORY

#    speed = math.degrees(math.cos(angle))/10
 #   up_speed = math.degrees(math.sin(angle))/10

    #CONTROLS THE PLANES SPEED

    if move_right:
        if speed < max_speed:
            speed += 0.3
            
    if move_left:
        if speed > min_speed:
            speed -= 0.3

   

    
    #CHANGING UP SPEED DEPENDING ON VARIABLE


    if move_up == 1:
        if angle >= 0:
            if angle < 15:
                up_speed = 1 * ((angle + 1) * 5 * angle)
            if angle < 45:
                up_speed = 1 * ((angle + 1) * .01 * angle)
            if angle > 45:
                up_speed = 0.4 * ((angle + 1) * .01 * angle)
        if angle < 0:
                up_speed = 0.4 * ((angle + 1) * .01 * -angle)
        jet_angle = 1
    if move_up == -1:
        if angle <= 0:
            if angle > -45:
                up_speed = 1 * ((angle + 1) * .01 * -angle)
            if angle < -45:
                up_speed = 0.4 * ((angle + 1) * .01 * -angle)
        if angle > 0:
                up_speed = 0.4 * ((angle + 1) * .01 * angle)
        jet_angle = -1
    if move_up == 0:
        jet_angle = 0

    if move_up == 1:
        jet_angle = 1
    if move_up == -1:
        jet_angle = -1
    if move_up == 0:
        jet_angle = 0

    #MAKING THE SKY GRADIENT


    if blue > 1 and red > 1 and green > 1:
        if blue < 254 and red < 254 and green < 254:
            blueheight -= angle/100
            redheight -= angle/100
            greenheight -= angle/100

    if jet_angle == 1:
        if angle < 25:
            angle_increment += 0.1
        if angle > 35:
            if angle_increment > 0.3:
                angle_increment -= 0.2
        if angle > 25:
            if angle_increment > 0.2:
                angle_increment -= 0.1
        if angle < 60:
            angle += angle_increment
    if jet_angle == -1:

        if angle > -35:
            angle_increment += 0.1
        if angle < -35:
            if angle_increment > 0.3:
                angle_increment += 0.2
        if angle > -45:
            angle -= angle_increment

                
    mx,my = pygame.mouse.get_pos()
    jetx, jety, jetw, jeth = jet_rect
    jetcentre = jety + (jeth / 2)

    missilex = 10
    
    if shoot == 1:
        missile_rect1 = (jetx + missilexv, permjetcentre)
        missilex, missiley = missile_rect1
        screen.blit(missile_surf, (missile_rect1))
        missilexv += 40
    if missilex > 2000:
        shoot = 0
    if shoot == 0:
        missilexv = 0
    

            
    
    jet_centre = jet_rect.center
    enemy = randint(1, 150)
    if enemy == 54:
        enemycoming = 1
    if enemycoming == 1:
        enemy_rect.x += randint(5, 15) - speed/2
        enemy_rect.y += up_speed
        
        xdist = jet_centre[0] - enemy_rect.x
        ydist = jet_centre[1] - enemy_rect.y
        
        enemy_angle = 0
        if xdist != 0 or ydist != 0:
            enemy_angle = math.degrees(math.atan2(ydist, xdist))
            
        enemy_rect.y += up_speed + enemy_angle/3
        if enemy_rect.x > jet_centre[0]:
            enemy_rect.x -= speed/2

        enemy_rotated_surf = pygame.transform.rotate(enemy_surf, -enemy_angle)
        enemy_rotated_rect = enemy_rotated_surf.get_rect(center = (enemy_rect.centerx, enemy_rect.centery))
        screen.blit(enemy_rotated_surf, enemy_rotated_rect)
    
    if enemy_rect.x > 2000 or colliding == 1:
        enemyreset = 1
        enemy_rect = enemy_surf.get_rect(center = (-50, randint(10, 590)))
        enemycoming = 0

  
    cloud1form = randint(1, 200)
    if cloud1form == 50:
        cloud1_coming = 1
    if cloud1_coming == 1:
        screen.blit(cloud1_surf, cloud1_rect)
        cloud1_rect.left -= speed
        cloud1_rect.y += up_speed

    if cloud1_rect.right < 0:
        cloud1reset = 1
        cloud1_rect = cloud1_surf.get_rect(midleft = (2100, randint(10, 1000)))


    jet_rotated_surf = pygame.transform.rotate(jet_surf, angle)
    jet_rotated_rect = jet_rotated_surf.get_rect(center = (800, 600))
    
    screen.blit(jet_rotated_surf, jet_rotated_rect)

    cloud2form = randint(1, 400)
    if cloud2form == 50:
        cloud2coming = 1
    if cloud2coming == 1:
        screen.blit(cloud2_surf, cloud2_rect)
        cloud2_rect.left -= (speed - 1)
        cloud2_rect.y += (up_speed)
    if cloud2_rect.right < 0:
        cloud2reset = 1
        cloud2_rect = cloud2_surf.get_rect(midleft = (2100, randint(10, 1000)))
  
    

    
    
    
    
    pygame.display.update()
    clock.tick(60)

