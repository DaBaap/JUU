import pygame, math, time, sys
from Classes import draw_circle, button, textbox,FCFS,SJF

second1 = True
cx = 700
cy = 270
cr = 10
cts = 30
i = 0
p =[]
At = []
Bt = []
ct = []
tat = []
wt = []
P = []
closer = 0
closey = 230
simulatecheck = False
simulation = False
red_line = 0
pas = True
ReadyQue = []
GanttChart = []

pygame.font.init()
secmain = pygame.font.SysFont('freesansbold.ttf', 52)
Txtx = pygame.font.SysFont('freesansbold.ttf', 40)
Ctxt = pygame.font.SysFont('freesansbold.ttf', 30)
Ttxt = Txtx.render('Process     AT     BT    CT     TAT     WT     RT', True, (60,60,60,),(243,243,243))
Rtxt = Ctxt.render('Ready Queue',True, (95,93,94),(243,243,243))
Gtxt = Ctxt.render('Gantt Queue',True, (95,93,94),(243,243,243))
TtxtR = Ttxt.get_rect()
RtxtR = Rtxt.get_rect()
GtxtR = Gtxt.get_rect()
TtxtR.center = (700, 200)
RtxtR.center = (386+50,640)
GtxtR.center = (386+50,640)

back = pygame.image.load('arrow (1).png')
simulate = button((105,118,124), 1033, 271,180,50, 'SIMULATE' , (245,250,253))
pause = button((105,118,124), 1033, 380,180,50, 'PAUSE' , (245,250,253))
stop = button((105,118,124), 1033, 490,180,50, 'STOP' , (245,250,253))
p1 = button((186,237,228), 429, 230, 48, 30, 'P1',(29,60,55),30)

t1 = textbox(550,230)
t2 = textbox(625, 230)

stAt = []
stBt = []
q = 0
ganVar = 368
u = 1
ordered = []
wttt = 0
tattt = 0

def secondPge(screen,evt, bg ,logo, static = False,Algo = ''):
    global ordered
    global back
    global second1
    global cr
    global cts
    global cx
    global cy 
    global p
    global i
    global closer
    global closey
    global P
    global ct 
    global tat 
    global wt
    global simulatecheck
    global simulation
    global stAt 
    global stBt
    global red_line 
    global pas 
    global ReadyQue 
    global GanttChart 
    global q
    global ganVar
    global u
    global wttt
    global tattt

    stxt = secmain.render(Algo + ' Simulation', True, (95,93,94),(243,243,243))
    stxtR = stxt.get_rect()
    stxtR.center = (700, 120)


    if Algo == 'SJF' and static:
        i = 3
        stAt = ["1","2","1","4"]
        stBt = ["3","4","2","4"]

    elif Algo == 'FCFS' and static:    
        i = 4
        stAt = ["0","2","4","1","6"]
        stBt = ["2","3","5","3","5"]

    second1 = True
    Cts = pygame.font.SysFont('freesansbold.ttf', cts)
    plus = Cts.render('+',True, (0,0,0))
    plusR = plus.get_rect() 
    plusR.center = (cx+1,cy-1)

    screen.blit(bg, (0,-50))
    screen.blit(logo,(123,59))
    screen.blit(stxt, stxtR)
    screen.blit(back, (5,0))

    pygame.draw.rect(screen, (74,77,84), pygame.Rect(410, 200, 580, 400),  0, 4)
    pygame.draw.rect(screen, (243,243,243), pygame.Rect(410, 180, 580, 40),  0, 4)
    pygame.draw.rect(screen, (20,20,20), pygame.Rect(368, 650, 665, 50),  2, 4)
    if cy+40 < 600 and not static:
        pygame.draw.rect(screen, (243,243,243), pygame.Rect(410, cy, 580, 5),  0, 1)
        draw_circle(screen, cx,cy, cr, (243,243,243))

    screen.blit(Ttxt, TtxtR)
    screen.blit(Gtxt, GtxtR)
    

    simulate.draw(screen)
    pause.draw(screen)
    stop.draw(screen)

    for j in range(i):
        if len(p) != i and not static:
            p.append(button((186,237,228), 429, cy-40, 48, 30, 'P'+str(i+1),(29,60,55),30))
            At.append(textbox(550, cy-40))
            Bt.append(textbox(625, cy-40))

        if len(p) != i and static:
            p.append(button((186,237,228), 429, cy, 48, 30, 'P'+str(j+2),(29,60,55),30))
            At.append(textbox(550, cy))
            Bt.append(textbox(625, cy))
            cy+=40

    p1.draw(screen)
    t1.draw(screen)
    t2.draw(screen)

    if static:
        t1.txt = stAt[0]
        t2.txt = stBt[0]

    for j in range(len(At)):
        p[j].draw(screen)
        if static:
            At[j].txt = stAt[j+1]
            Bt[j].txt = stBt[j+1]
        At[j].draw(screen)
        Bt[j].draw(screen)

    draw_circle(screen, 429, closey, closer,(227,93,93))

    if simulatecheck:
        ctt = []
        tatt = []
        wtt = []
        for j in range(len(ct)):
            ctt.append(Ctxt.render(f'{ct[j][1]}',True, (255,255,255)))
            tatt.append(Ctxt.render(f'{tat[j][1]}',True, (255,255,255)))
            wtt.append(Ctxt.render(f'{wt[j][1]}',True, (255,255,255)))

        for k in range(len(ct)):
            for j in range(len(p)):
                if ct[k][0] == p1.text:

                    w = t2.x + 90
                    h = t2.y + 15
                    r = ctt[k].get_rect()
                    r.center = (w,h)
                    screen.blit(ctt[k], r)

                    r = tatt[k].get_rect()
                    r.center = (w+90,h)
                    screen.blit(tatt[k], r)

                    r = wtt[k].get_rect()
                    r.center = (w+170,h)
                    screen.blit(wtt[k], r)

                    r = wtt[k].get_rect()
                    r.center = (w+250,h)
                    screen.blit(wtt[k], r)

                elif ct[k][0] == p[j].text:
                    w = Bt[j].x + 90
                    h = Bt[j].y + 15
                    r = ctt[k].get_rect()
                    r.center = (w,h)
                    screen.blit(ctt[k], r)

                    r = tatt[k].get_rect()
                    r.center = (w+90,h)
                    screen.blit(tatt[k], r)

                    r = wtt[k].get_rect()
                    r.center = (w+170,h)
                    screen.blit(wtt[k], r)

                    r = wtt[k].get_rect()
                    r.center = (w+250,h)
                    screen.blit(wtt[k], r)
        pygame.draw.rect(screen, (74,77,84), pygame.Rect(25,300, 335,100),2,4)
        if wttt != 0 and tattt != 0:
            wait = Ctxt.render('Average Waiting Time = '+str(wttt), True, (20,20,20))
            waitr = wait.get_rect()
            waitr.center = (190,325)
            screen.blit(wait,waitr)   

            turn = Ctxt.render('Average Turnaround Time = '+str(tattt), True, (20,20,20))
            turnr = turn.get_rect()
            turnr.center = (200,365)
            screen.blit(turn,turnr)                     
    
    if red_line <=665:
        pygame.draw.rect(screen, (190,20,20), pygame.Rect(368, 698, red_line, 3),  0, 2)
        z = 368
        c6 = int(661/(len(GanttChart)-1))

        if len(ct) != 0:
            # f = int(661/(len(GanttChart)-1))
            for a in range(len(ct)):
                # z = 366 + (f*a)
                for h in range(u):
                    f = ((661/GanttChart[-1])*int(GanttChart[h]))
                    if ct[a][1] == GanttChart[h]:
                        if ordered[a][1] == GanttChart[h-1]:
                            z = 366 + (f*(h-1))+2
                            # z = 366 + (f)+2
                            if h - 1 >= 0:
                                # lwl = ((661/GanttChart[-1])*(int(GanttChart[h]) - int(GanttChart[h-1]))) 
                                lwl = ((661/GanttChart[-1])*ordered[a][2]) 

                            else:
                                lwl = ((661/GanttChart[-1])*int(GanttChart[h]))
                            print(str(ct[a][0]), ((661/GanttChart[-1])*int(GanttChart[h])), GanttChart[h], lwl, "h = ",h)
                            button((186,237,228), z, 652, lwl, 46, str(ct[a][0]), (29,60,55), 30).draw(screen)
                    elif ordered[a][1] < GanttChart[h]:
                        if h+1<len(GanttChart) and ct[a][1] == GanttChart[h+1]:
                            z = 366 + (f)+2
                            # z = 366 + (f)+2

                            if h - 1 >= 0:
                                # lwl = ((661/GanttChart[-1])*(int(GanttChart[h+1]) - int(GanttChart[h-1]))) 
                                lwl = ((661/GanttChart[-1])*ordered[a][2]) 

                            else:
                                lwl = ((661/GanttChart[-1])*int(GanttChart[h+1]))
                            print(str(ct[a][0]), " adsa", ((661/GanttChart[-1])*int(GanttChart[h])), GanttChart[h],"h = ",h)
                            button((186,237,228), z, 652, lwl, 46, str(ct[a][0]), (29,60,55), 30).draw(screen)
                    
        if len(GanttChart) != 0:
            for a in range(u):
                # z = 368 + (c6*a)
                z = 368 + ((661/GanttChart[-1])*int(GanttChart[a]))
                # Bt[a].txt)
                pygame.draw.line(screen,(0,0,0),(z,650),(z,701))
                O = Ctxt.render(str(GanttChart[a]), True, (0,0,0))
                Ot = O.get_rect()
                Ot.center = (z,710)
                screen.blit(O,Ot)

        if simulatecheck and not pas:
            if len(GanttChart) != 0:
                if u != len(GanttChart) and (red_line+368 == 368 + int(((661/GanttChart[-1])*int(GanttChart[u]))) or red_line+367 == 368 +int(((661/GanttChart[-1])*int(GanttChart[u])))):
                    #ganVar
                    if u != len(GanttChart):
                        u+=1
                    if u == len(GanttChart):
                        u = len(GanttChart)
                    ganVar += c6
                    if ganVar > 1033:
                        ganVar = 1033

            if red_line+2>661:
                red_line = 661
            else:
                red_line+=2

        pygame.display.update()
            
    for event in evt:
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if pos[0] > 0 and pos[0] < 37:
                if pos[1] > 0 and pos[1] < 32:
                    back = pygame.transform.scale(back,(37,37))
                    screen.blit(back, (0,-5))
            elif simulate.isOver(pos):
                    simulate.color = (145,158,164)
                    simulate.x,simulate.y = 1033-5,271-2
                    simulate.width,simulate.height = 190,53
            elif pause.isOver(pos):
                    pause.color = (145,158,164)
                    pause.x,pause.y = 1033-5,380-2
                    pause.width,pause.height = 190,53
            elif stop.isOver(pos):
                    stop.color = (145,158,164)
                    stop.x,stop.y = 1033-5,490-2
                    stop.width,stop.height = 190,53       
            elif math.sqrt((pos[0]-700)**2 + (pos[1]-cy+2)**2) < 10:
                cr = 13
                cts = 35
            else:
                back = pygame.image.load('arrow (1).png')
                screen.blit(back, (5,0))

                simulate.color = (105,118,124)
                simulate.x,simulate.y = 1033,271
                simulate.width,simulate.height = 180,50

                pause.color = (105,118,124)
                pause.x,pause.y = 1033,380
                pause.width,pause.height = 180,50

                stop.color = (105,118,124)
                stop.x,stop.y = 1033, 490
                stop.width,stop.height = 180,50
                cr = 10
                cts = 30

                closer = 0

                for j in range(len(p)):
                
                    if not static and p[j].isOver(pos) or math.sqrt((pos[0]-429)**2 + (pos[1]-closey)**2) < closer:
                        closer = 5
                        closey = p[j].y

                        if math.sqrt((pos[0]-429)**2 + (pos[1]-closey)**2) < closer:
                            closer = 7
                    
        if event.type == pygame.KEYDOWN and not static:
            t1.txtupdate(event)
            t2.txtupdate(event)
            for j in range(len(At)):
                At[j].txtupdate(event)
                Bt[j].txtupdate(event)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > 0 and pos[0] < 37:
                if pos[1] > 0 and pos[1] < 32:
                    i = 0
                    cy = 270
                    p.clear()
                    p = []
                    P = []
                    At.clear()
                    Bt.clear()
                    stAt = []
                    stBt = []
                    j = 0
                    static = False
                    simulatecheck = False
                    simulation = False
                    pas = True
                    u = 0
                    red_line = 0
                    second1 = False

            elif not static and math.sqrt((pos[0]-700)**2 + (pos[1]-cy+2)**2) < 10:
                if cy+40>600:
                    pass
                else:
                    cy += 40 
                    i+=1
                
            t1.actives(pos)
            t2.actives(pos)
            for j in range(len(At)):
                At[j].actives(pos)
                Bt[j].actives(pos)

            for j in range(len(p)):
                    try:
                        if p[j].isOver(pos) or math.sqrt((pos[0]-429)**2 + (pos[1]-closey)**2) < closer:
                            closey = p[j].y

                            if math.sqrt((pos[0]-429)**2 + (pos[1]-closey)**2) < closer and j==len(p)-1:
                                cy-=40
                                i-=1
                                p.pop(j)
                                At.pop(j)
                                Bt.pop(j)
                                j-=1
                    except IndexError:
                        pass
            if pause.isOver(pos) and simulatecheck:
                if simulatecheck and pause.text == 'PAUSE':
                    pause.text = 'UNPAUSE'
                    pas = True
                else: 
                    simulatecheck = True
                    pause.text = 'PAUSE'
                    pas = False

            if stop.isOver(pos):
                P=[]
                red_line = 0
                P.clear()
                ct.clear()
                tat.clear()
                wt.clear()
                u = 0
                ganVar = 368
                simulatecheck = False
                pas = True
                pause.text = 'PAUSE'

            if simulate.isOver(pos):
                simulation = True
                P.clear()
                ct.clear()
                tat.clear()
                wt.clear()
                red_line = 0
            
                if t1.txt == '':
                    t1.color = (255,0,0)
                    continue
                if t2.txt == '':
                    t2.color = (255,0,0)
                    continue
                    
                for j in range(len(At)):
                    if At[j].txt == '' :
                        At[j].color = (255,0,0)
                        continue
                    if  Bt[j].txt == '':
                        Bt[j].color = (255,0,0)
                        continue
                
                if t1.txt != '' and t2.txt != '':
                    P.append(['P1',int(t1.txt),int(t2.txt)])

                    for j in range(len(At)):
                        if At[j].txt != '' and Bt[j].txt !='':
                            P.append([f'P{j+2}',int(At[j].txt),int(Bt[j].txt)])
                if len(P) == len(At)+1:
                    M = P.copy()
                    if Algo == 'FCFS':
                        ct,tat,wt,GanttChart,ordered = FCFS(P)
                    
                    elif Algo == 'SJF':
                        ct,tat,wt,GanttChart,ordered = SJF(P)
                        
                    P = M.copy()
                    M.clear()

                simulatecheck = True
                pas = False
                ReadyQue = ct.copy()
                ReadyQue.reverse()


                if simulatecheck:
                    ctt = []
                    tatt = []
                    wtt = []
                    for j in range(len(ct)):
                        ctt.append(Ctxt.render(f'{ct[j][1]}',True, (255,255,255)))
                        tatt.append(Ctxt.render(f'{tat[j][1]}',True, (255,255,255)))
                        wtt.append(Ctxt.render(f'{wt[j][1]}',True, (255,255,255)))

                    
                    for k in range(len(ct)):
                        for j in range(len(p)):
                            if ct[k][0] == p1.text:
                                w = t2.x + 90
                                h = t2.y + 15
                                r = ctt[k].get_rect()
                                r.center = (w,h)
                                screen.blit(ctt[k], r)

                                r = tatt[k].get_rect()
                                r.center = (w+90,h)
                                screen.blit(tatt[k], r)

                                r = wtt[k].get_rect()
                                r.center = (w+170,h)
                                screen.blit(wtt[k], r)

                                r = wtt[k].get_rect()
                                r.center = (w+250,h)
                                screen.blit(wtt[k], r)

                                if simulation: 
                                    time.sleep(0.5)
                                    pygame.display.update()
                                    

                            elif ct[k][0] == p[j].text:
                                w = Bt[j].x + 90
                                h = Bt[j].y + 15
                                r = ctt[k].get_rect()
                                r.center = (w,h)
                                screen.blit(ctt[k], r)

                                r = tatt[k].get_rect()
                                r.center = (w+90,h)
                                screen.blit(tatt[k], r)

                                r = wtt[k].get_rect()
                                r.center = (w+170,h)
                                screen.blit(wtt[k], r)

                                r = wtt[k].get_rect()
                                r.center = (w+250,h)
                                screen.blit(wtt[k], r)
                                
                                if simulation: 
                                    time.sleep(0.5)
                                    pygame.display.update()
                    if len(wt) != 0:
                        wttt = 0
                        for la in range(len(wt)):
                            wttt+=int(wt[la][1])
                        wttt = wttt/len(wt)
                    if len(tat) != 0:

                        tattt = 0
                        for la in range(len(tat)):
                            tattt+=int(tat[la][1])
                        tattt = tattt/len(tat)

                                
                simulation = False

    if cy+40 < 600 and not static:            
        screen.blit(plus, plusR)
                
    pygame.display.update()
