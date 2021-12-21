import pygame
from pygame import gfxdraw 
# Button
def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

class button:
    def __init__(self, color, x,y,width,height, text='', Tcolor=(177,243,231),tsize=42):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.Tcolor = Tcolor
        self.tsize = tsize

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0,4)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.tsize)
            text = font.render(self.text, 1, self.Tcolor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
#Optionbox
class OptionBox:
    
    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected = 0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.text_option = [None for _ in range(len(option_list))]

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect,0,4)
        msg = self.font.render(self.option_list[self.selected], 1, (76,106,102))
        surf.blit(msg, msg.get_rect(center = self.rect.center))
        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                if i == len(self.option_list)-1:
                    pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect,0,4)
                else:
                    pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect,0)
                msg = self.font.render(text, 1, (76,106,102))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1


class textbox:
    def __init__(self,x,y,tcolor=(255,255,255)):
        pygame.font.init()
        self.font = pygame.font.SysFont('comicsans',30)

        self.rect = pygame.Rect(x,y,48,30)
        self.x = x
        self.y = y
        self.txt = ''
        self.tcolor = tcolor
        self.white = (255,255,255)
        self.grey = (100,100,100)
        self.color = self.grey
        self.active = False

    def draw(self,win):

        if self.color == (255,0,0) and not self.active:
            pass
        else:
            self.color = self.grey


            if self.active:
                self.color = self.white
            else:
                self.color = self.grey     

        

        pygame.draw.rect(win,self.color,self.rect,2,4)
        
        msg = self.font.render(self.txt, 1, self.tcolor)
        win.blit(msg, (self.rect.x+(self.rect.w/2 - msg.get_width()/2), self.rect.y+(self.rect.h/2 - msg.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + 48:
            if pos[1] > self.y and pos[1] < self.y + 30:
                return True
    def txtupdate(self,event = None,text = ''):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                    self.txt = self.txt[:-1]
            else:
                if len(self.txt) == 2:
                    pass
                else:
                    lol = event.unicode
                    if lol.isdigit():
                        self.txt += event.unicode
        if text != '':
            self.txt = text
    def actives(self, pos):
        if self.isOver(pos):
            self.active = True 
        else:
            self.active = False


def FCFS(P):
    for i in range(len(P)):
        for l in range(len(P)):
            if P[i][1] < P[l][1]:
                temp = P[l]
                P[l] = P[i]                                                        
                P[i] = temp
                
    print(P)
    ct = []
    tat = []
    wt = []
    gantt = []
    ct.append([P[0][0],P[0][1]+P[0][2]])


    for i in range(1,len(P)):

        j = i - 1
        print(i+1 ,len(P),ct[j][1] ,P[i][1])
        if ct[j][1] <= P[i][1]:
            ct.append([P[i][0],P[i][1]+P[i][2]])
        else:
            ct.append([P[i][0],ct[j][1]+P[i][2]])


    for i in range(len(P)):
        tat.append([P[i][0],ct[i][1]-P[i][1]])
        wt.append([P[i][0],tat[i][1]-P[i][2]])

    gantt.append(0)
    if P[0][1] != 0:
        gantt.append(P[0][1])
    gantt.append(ct[0][1])

    for i in range(1,len(P)):
        if P[i][1] > ct[i-1][1]:
            gantt.append(P[i][1])
            gantt.append(ct[i-1][1])
        else:
            gantt.append(ct[i][1])
            

    print(gantt)
    print(ct)
    print(tat)
    print(wt)
    return ct,tat,wt,gantt,P

def SJF(P):
    for i in range(len(P)):
        for l in range(len(P)):
            if P[i][1] < P[l][1]:
                temp = P[l]
                P[l] = P[i]                                                        
                P[i] = temp
                
    for i in range(len(P)):
        for l in range(len(P)):
            if P[i][2] < P[l][2]:
                temp = P[l]
                P[l] = P[i]                                                        
                P[i] = temp
    print(P)
    ct = []
    tat = []
    wt = []
    gantt = []
    ct.append([P[0][0],P[0][1]+P[0][2]])

    for i in range(1,len(P)):

        j = i - 1
        print(i+1 ,len(P),ct[j][1] ,P[i][1])
        if ct[j][1] <= P[i][1]:
                ct.append([P[i][0],P[i][1]+P[i][2]])
        else:
            ct.append([P[i][0],ct[j][1]+P[i][2]])


    for i in range(len(P)):
        tat.append([P[i][0],ct[i][1]-P[i][1]])
        wt.append([P[i][0],tat[i][1]-P[i][2]])


    gantt.append(0)
    if P[0][1] != 0:
        gantt.append(P[0][1])
    gantt.append(ct[0][1])

    for i in range(1,len(P)):
        if P[i][1] > ct[i-1][1]:
            gantt.append(P[i][1])
            gantt.append(ct[i-1][1])
        else:
            gantt.append(ct[i][1])
            
    print(gantt)
    print(ct)
    print(tat)
    print(wt)
    return ct,tat,wt,gantt,P