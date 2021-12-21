import pygame, math, time, sys
from Classes import OptionBox,button
from secondpage import secondPge, second1

pygame.init()
angle = 0
screen = pygame.display.set_mode((1400,883), pygame.NOFRAME)
pygame.display.update()
pygame.display.set_caption("JU Simulator")


icon = pygame.image.load('dog.png')
bg   = pygame.image.load('download.png')
logo = pygame.image.load('logo .png')
arrow = pygame.image.load('arrow.png')

bg   = pygame.transform.scale(bg,(1400,933))
arrow = pygame.transform.scale(arrow,(10,16))
logo = pygame.transform.scale(logo,(211,153))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
wiat = False
rn = True

txt = pygame.font.SysFont('Segoe UI', 27, True)
main = pygame.font.SysFont('freesansbold.ttf', 64)
secmain = pygame.font.SysFont('freesansbold.ttf', 52)

text = txt.render('INPUT:',True, (255,255,255))
Atxt = txt.render('ALGORITHM:',True, (255,255,255))
mtxt = main.render('CPU-Scheduling', True,(46,46,48))
stxt = secmain.render('Simulation', True, (95,93,94),(243,243,243))

textRect = text.get_rect()
mtxtR = mtxt.get_rect()
AtxtR = Atxt.get_rect()
stxtR = stxt.get_rect()
textRect.bottomleft = (410+96, 319+94)
AtxtR.bottomleft = (410+96, 319+183)
mtxtR.center = (700, 120)
stxtR.center = (750, 164)

Olist1 = OptionBox(
    410+328, 319+55, 160, 40, (182, 244, 233), (182, 244, 233), pygame.font.SysFont('arial', 25), 
    ["DYNAMIC","STATIC"])
Olist2 = OptionBox(
    410+328, 319+148, 160, 40, (182, 244, 233), (182, 244, 233), pygame.font.SysFont('arial', 25), 
    ["FCFS", "SJF"])

start = button((74,77,84), 442, 670, 140,42, 'Start    ')
exit = button((74,77,84), 442+343, 670, 140,42, 'Exit    ')
close = pygame.Surface((31,23))
close.set_alpha(0)
close.fill((209,54,57))
mini = pygame.Surface((31,23))
mini.set_alpha(0)
mini.fill((255-40,255-42,255-42))

second = False

while rn:
    from secondpage import second1
    clock.tick(100)
    
    evt = pygame.event.get()
    if second:
        if Olist2.option_list[Olist2.selected] == 'FCFS' and Olist1.option_list[Olist1.selected] == 'DYNAMIC':
            secondPge(screen, evt, bg, logo, False,'FCFS')
            second = second1
        elif Olist2.option_list[Olist2.selected] == 'FCFS' and Olist1.option_list[Olist1.selected] == 'STATIC':
            
            secondPge(screen, evt, bg, logo,True,'FCFS')
            second = second1
        elif Olist2.option_list[Olist2.selected] == 'SJF' and Olist1.option_list[Olist1.selected] == 'DYNAMIC':
            secondPge(screen, evt, bg, logo, False,'SJF')
            second = second1
        elif Olist2.option_list[Olist2.selected] == 'SJF' and Olist1.option_list[Olist1.selected] == 'STATIC':
            secondPge(screen, evt, bg, logo,True,'SJF')
            second = second1   
        else:
              sys.exit()

    if not second:
        
        screen.blit(bg, (0,-50))
        screen.blit(logo,(123,59))
        pygame.draw.rect(screen, (74,77,84), pygame.Rect(410, 319, 580, 273),  0, 4)
        screen.blit(text, textRect)
        screen.blit(Atxt, AtxtR)
        screen.blit(mtxt, mtxtR)
        screen.blit(stxt, stxtR)

        opt = Olist1.update(evt)
        input = Olist1.option_list[Olist1.selected]
        opt2 = Olist2.update(evt)
        algo = Olist2.option_list[Olist2.selected]
        Olist2.draw(screen)
        Olist1.draw(screen)
        start.draw(screen)
        exit.draw(screen)
        screen.blit(arrow,(442+110,670+12))
        pygame.display.flip()

        for event in evt: 
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                rn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isOver(pos):
                    rn=False
                if start.isOver(pos):
                    second = True
                    second1 = True
                    
                    break
            if event.type == pygame.MOUSEMOTION:   
                if start.isOver(pos):
                    start.color = (102,119,126)
                    start.x,start.y = 442-5, 670-2
                    start.width,start.height = 150,45
                elif exit.isOver(pos):
                    exit.color = (102,119,126)
                    exit.x,exit.y = 442+343-5, 670-2
                    exit.width,exit.height = 150,45
                elif pos[0] > 1369 and pos[0] < 1400:
                    if pos[1] > 0 and pos[1] < 23:
                        close.set_alpha(255)
                elif pos[0] > 1369-31 and pos[0] < 1400-31:
                    if pos[1] > 0 and pos[1] < 23:
                        mini.set_alpha(100) 
                elif pygame.mouse.get_focused() == 0:
                    close.set_alpha(0)
                    mini.set_alpha(0)
               
                else:
                    start.color = (74,77,84)
                    exit.color = (74,77,84)
                    start.x,start.y = 442, 670
                    exit.x,exit.y = 442+343, 670
                    start.width,start.height = 140,42
                    exit.width,exit.height = 140,42
                    close.set_alpha(0)
                    mini.set_alpha(0)
        pygame.display.update()
    
pygame.quit()
