import pygame
import random

pygame.init()
white = (255,255,255)
transparent = (0, 0, 0, 0)
x=1280
y=720
imageran = 0 
display_surfaces = pygame.display.set_mode((x,y))
display_surfaces.fill((255,255,255))
finish = True

hole_positions = []
hole_positions.append((-37, 557))
hole_positions.append((-207, 509))
hole_positions.append((-421, 560))
hole_positions.append((-705, 528))
hole_positions.append((953, 563))
print(hole_positions)

picture_list = []
Q1 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C1.png').convert()
picture_list.append(Q1)
Q2 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C2.png').convert()
picture_list.append(Q2)
Q3 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C3.png').convert()
picture_list.append(Q3)
Q4 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C4.png').convert()
picture_list.append(Q4)
Q5 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C5.png').convert()
picture_list.append(Q5)
Q6 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Charactor\\C6.png').convert()
picture_list.append(Q6)
Q7 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B1.png').convert()
picture_list.append(Q7)
Q8 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B2.png').convert()
picture_list.append(Q8)
Q9 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B3.png').convert()
picture_list.append(Q9)
Q10 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B4.png').convert()
picture_list.append(Q10)
Q11 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B5.png').convert()
picture_list.append(Q11)
Q12 = pygame.image.load('C:\\Users\ACER\\Final project CPE102\\Boss\\B6.png').convert()
picture_list.append(Q12)
imageran = picture_list.pop(random.randint(0,len(picture_list)-1))


while True:
    display_surfaces.blit(imageran,(x,y))
    pygame.display.update() 
    for event in pygame.event.get() :
        if finish == False or event.type == pygame.QUIT : 
        # deactivates the pygame library 
            pygame.quit() 
        # quit the program. 
            quit() 
    pygame.display.update() 


MALLETROTNORM   = 15
MALLETROTHIT    = 30
thisHammer = transform.rotate(self.img_mallet.copy(),
                                      (Constants.MALLETROTHIT if clicked else Constants.MALLETROTNORM))
        hammer_x, hammer_y = mouse.get_pos()
        hammer_x -= thisHammer.get_width() / 5
        hammer_y -= thisHammer.get_height() / 4
        self.screen.blit(thisHammer, (hammer_x, hammer_y))
        
        display_surface.blit(image, (0, 0))
        m,n = pygame.mouse.get_pos()
        m -= Hit01.get_width()/2
        n -= Hit01.get_height()/2
        thor = display_surface.blit(Hit01,(m,n))
def man(x,y,z)




man(1,2,3)