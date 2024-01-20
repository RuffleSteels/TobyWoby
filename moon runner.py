import pygame
from sys import exit
from random import randint
import math
import os

jetup = 0
shoot = 0
missilexv = 0
enemycoming = 0
speed = 10
max_speed = 40
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
enemy_missile_fire = 0
coordsx = 0
coordsy = 0
missile_angle = 0
acceleration_up_speed = 0
enemyshooting = 0
side_speed = 10
rotated_enemy_missile_rect = 0
canenemyshooting = 0
missilecolliding = 0


move_left = False
move_right = False
move_up = 0
move_down = False   

pygame.init()

screenWidth = 1500
screenHeight = 900
screenCentre = (screenWidth/2, screenHeight/2)
scale = screenHeight/1.2/screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)



pygame.display.set_caption('Moon Explorer')
clock = pygame.time.Clock()


# sky_surf = pygame.display.set_mode((2000, 1200))
sky_rect = screen.get_rect(center = (1000, 600))

background1_surf = pygame.image.load('graphics/background.png').convert_alpha()
background_surf = pygame.transform.scale(background1_surf, (6000*scale, 900*scale))
background_rect = background_surf.get_rect(bottomleft = (0, screenHeight))

midground1_surf = pygame.image.load('graphics/midground.png').convert_alpha()
midground_surf = pygame.transform.scale(midground1_surf, (6000*scale, 900*scale))
midground_rect = background_surf.get_rect(bottomleft = (0, screenHeight))

foreground1_surf = pygame.image.load('graphics/foreground.png').convert_alpha()
foreground_surf = pygame.transform.scale(foreground1_surf, (6000*scale, 900*scale))
foreground_rect = foreground_surf.get_rect(bottomleft = (0, screenHeight))

cloud1_surf1 = pygame.image.load('graphics/cloud1.png').convert_alpha()
cloud1_surf = pygame.transform.scale(cloud1_surf1, (640*scale, 400*scale))
cloud1_rect = cloud1_surf.get_rect(midleft = (2100, 400))

cloud2_surf1 = pygame.image.load('graphics/cloud2.png').convert_alpha()
cloud2_surf = pygame.transform.scale(cloud2_surf1, (640*scale, 400*scale))
cloud2_rect = cloud2_surf.get_rect(midleft = (2100, 400))

cloud3_surf1 = pygame.image.load('graphics/cloud2.png').convert_alpha()
cloud3_surf = pygame.transform.scale(cloud2_surf1, (640*scale, 400*scale))
cloud3_rect = cloud2_surf.get_rect(midleft = (2100, 400))    

heli_surf1 = pygame.image.load('graphics/Helicopter.png').convert_alpha()
heli_surf =  pygame.transform.scale(heli_surf1, (140*scale, 70*scale))
heli_rect = heli_surf.get_rect(center = (1800, 600))

jet_surf1 = pygame.image.load('graphics/fighter jet.png').convert_alpha()
jet_surf =  pygame.transform.scale(jet_surf1, (120*scale, 40*scale))
jet_rect = jet_surf.get_rect(center = screenCentre)

missile_surf1 = pygame.image.load('graphics/missile.png').convert_alpha()
missile_surf = pygame.transform.scale(missile_surf1, (35*scale, 12*scale))
missile_rect = missile_surf.get_rect(center = (200, 600))

enemy_surf1 = pygame.image.load('graphics/enemy.png').convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf1, (100*scale, 36*scale))
enemy_rect = enemy_surf.get_rect(center = (0, screenCentre[1]))

enemy_missile_surf1 = pygame.image.load('graphics/missile.png').convert_alpha()
enemy_missile_surf = pygame.transform.scale(enemy_missile_surf1, (35*scale, 12*scale))
enemy_missile_rect = enemy_missile_surf.get_rect(center = (200, 600))

speedomiterImg = pygame.image.load('graphics/speedomiter.png').convert_alpha()
speedomiterObj = pygame.transform.scale(speedomiterImg, (400*scale, 250*scale))
speedomiterRect = speedomiterObj.get_rect(bottomright = (screenWidth, screenHeight+speedomiterObj.get_height()/8))

heartone_surf = pygame.image.load('graphics/heart.png').convert_alpha()
heart1_surf = pygame.transform.scale(heartone_surf, (80*scale, 80*scale))
heart1_rect = heart1_surf.get_rect(center = (100, 1110))

hearttwo_surf = pygame.image.load('graphics/heart.png').convert_alpha()
heart2_surf = pygame.transform.scale(hearttwo_surf, (80*scale, 80*scale))
heart2_rect = heart2_surf.get_rect(center = (200, 1100))

heartthree_surf = pygame.image.load('graphics/heart.png').convert_alpha()
heart3_surf = pygame.transform.scale(heartthree_surf, (80*scale, 80*scale))
heart3_rect = heart3_surf.get_rect(center = (300, 1100))

mph_font = pygame.font.Font(None, int(70*scale))
mphtext_surf = mph_font.render('mph', False, (225, 225, 225))
mphtext_rect = mphtext_surf.get_rect(center = (screenWidth-mphtext_surf.get_width()*1.2, screenHeight-mphtext_surf.get_height()/1.5)) 

sky_rect = screen.get_rect(topleft = (0, 0))

def calculate_angle(x1, y1, x2, y2):
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return angle

colliding = 0
animations = []
temp_acc = 1     
 
background_distance = 0
midground_distance = 0
foreground_distance = 0
 
while True:
    red = 79 + redheight
    green = 176 + greenheight
    blue = 240 + blueheight
    pygame.draw.rect(screen, (red, green, blue), sky_rect)

    screen.blit(background_surf, background_rect)
    background_distance += speed / 20
    if background_distance == int(background_distance):
        background_rect.left - background_distance
        background_rect.y += up_speed / 30

    screen.blit(midground_surf, midground_rect)
    midground_rect.left -= speed / 10
    midground_rect.y += up_speed / 10
    print(speed / 10, up_speed / 10)



    #EVERYTHING WHICH MOVES
    
    

    

    
    speed_font = pygame.font.Font(None, int(130*scale))

    speedtext_surf = speed_font.render(str(math.trunc(speed*10)), False, (225, 225, 225))
    speedtext_rect = speedtext_surf.get_rect(center = (screenWidth-mphtext_surf.get_width()*1.3-mphtext_surf.get_width()*1.3, screenHeight-mphtext_surf.get_height())) 


    screen.blit(speedomiterObj, speedomiterRect)
    screen.blit(mphtext_surf, mphtext_rect)
    screen.blit(speedtext_surf, speedtext_rect)

    #screen.blit(foreground_surf, foreground_rect)
    #foreground_rect.x -= speed/2
    #foreground_rect.y += up_speed/20
    #screen.blit(foreground2_surf, foreground2_rect)
    #foreground2_rect.x -= speed/2
    #foreground2_rect.y += up_speed/20
    #if foreground_rect.right < 0:
    #    foreground_rect = foreground_surf.get_rect(topleft = (2000, 0))
    #if foreground2_rect.right < 0:
    #    foreground2_rect = foreground2_surf.get_rect(topleft = (2000, 0))


    if lives >= 1:
        screen.blit(heart1_surf, heart1_rect)
        if lives >= 2:
            screen.blit(heart2_surf, heart2_rect)
            if lives == 3:
                screen.blit(heart3_surf, heart3_rect)




              
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
        if side_speed < max_speed:
            side_speed += 0.3

            
    if move_left:
        if side_speed > min_speed:
            side_speed -= 0.3

   

    
    #CHANGING UP SPEED DEPENDING ON VARIABLE


    # if move_up == 1:
    #     acceleration_up_speed = up_speed
    #     if angle >= 0:
    #         if angle < 15:
    #             up_speed = 1 * ((angle + 1) * 5 * angle)
    #         if angle < 45:
    #             up_speed = 1 * ((angle + 1) * .01 * angle)
    #         if angle > 45:
    #             up_speed = 0.4 * ((angle + 1) * .01 * angle)
    #     if angle < 0:
    #             up_speed = 0.4 * ((angle + 1) * .01 * -angle)
    #     jet_angle = 1
    # if move_up == -1:
    #     acceleration_up_speed = up_speed
    #     if angle <= 0:
    #         if angle > -45:
    #             up_speed = 1 * ((angle + 1) * .01 * -angle)
    #         if angle < -45:
    #             up_speed = 0.4 * ((angle + 1) * .01 * -angle)
    #     if angle > 0:
    #             up_speed = 0.4 * ((angle + 1) * .01 * angle)
    #     jet_angle = -1
    # if move_up == 0:
    #     acceleration_up_speed = acceleration_up_speed
    #     jet_angle = 0
    
    # up_speed = calculate_y_velocity(angle)
    
    up_speed = angle
    

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
        if angle > 25:
            if angle_increment > 0.2:
                angle_increment -= 0.1
        if angle < 35:
            angle += angle_increment
    if jet_angle == -1:

        if angle > -35:
            angle_increment += 0.1
        if angle > -35:
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
    


    jet_top_left = jet_rect.topleft
    jet_centre = jet_rect.center
    

    speed = math.cos(angle*(math.pi/180)) * side_speed 
    # up_speed =  math.sin(angle*(math.pi/180)) * side_speed

    enemy = randint(1, 150)
    if enemy == 54:
        enemycoming = 1
        canenemyshooting = 1

    if enemy_missile_rect.colliderect(jet_rect):    
        if missilecolliding == 0:
            lives -= 1
            missilecolliding = 1 

    if canenemyshooting == 1:

        missile_fire = randint(1, 100)
        if missile_fire == 53:
            enemyshooting = 1
            if enemy_missile_fire == 0:
                coordsx = enemy_rect.centerx
                coordsy = enemy_rect.centery
                enemy_missile_rect = enemy_missile_surf.get_rect(center = (coordsx, coordsy))

                xdist = jet_centre[0] - enemy_rect.centerx
                ydist = jet_centre[1] - enemy_rect.centery

                missile_angle = math.degrees(math.atan2(ydist, xdist))

                
                rotated_enemy_missile_surf = pygame.transform.rotate(enemy_missile_surf, -missile_angle)
                rotated_enemy_missile_rect = rotated_enemy_missile_surf.get_rect(center = (enemy_missile_rect[0], enemy_missile_rect[1]))

            enemy_missile_fire = 1

            if missilecolliding == 1 or rotated_enemy_missile_rect.x > 2000:
                missilereset = 1
                enemy_missile_rect = enemy_missile_surf.get_rect(center = (100, -100))
                enemy_missile_fire == 0

        if enemy_missile_fire == 1:

            screen.blit(rotated_enemy_missile_surf, rotated_enemy_missile_rect)

            #coordsx += 13
            rotated_enemy_missile_rect.x += math.cos(missile_angle*(math.pi/180))*10
            rotated_enemy_missile_rect.y += ( math.sin(missile_angle*(math.pi/180))*10 ) + acceleration_up_speed


        


    
    if enemycoming == 1:


        enemy_rect.x += randint(5, 15) - speed/2 
        enemy_rect.y += up_speed
        
        xdist = jet_top_left[0] - enemy_rect.left
        ydist = jet_top_left[1] - enemy_rect.top

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
        cloud1_rect = cloud1_surf.get_rect(midleft = (screenWidth, randint(10, 1000)))


    jet_rotated_surf = pygame.transform.rotate(jet_surf, angle)
    jet_rotated_rect = jet_rotated_surf.get_rect(center = screenCentre)
    
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

    screen.blit(heli_surf, heli_rect)
  
    
    if enemy_rect.colliderect(jet_rect):    
        if colliding == 0:
            startExplosion(animations, jet_rect.x-175, jet_rect.y-256)
            lives -= 1
            colliding = 1
    
    
    
    animations_to_remove = []
    for animation in animations:
        if animation.update(screen, speed, up_speed):
            animations_to_remove.append(animation)

    for animation in animations_to_remove:
        animations.remove(animation)


    screen.blit(foreground_surf, foreground_rect)
    foreground_rect.left -= speed / 5
    foreground_rect.y += up_speed / 5

    pygame.display.update()
    clock.tick(60)

