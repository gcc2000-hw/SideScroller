from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pygame
count=0
import random
from tkinter import messagebox
clock = pygame.time.Clock()
e=None
        
        # Here, we are creating our class, Window, and inheriting from the Frame
        # class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
    # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   
    #reference to the master widget, which is the tk window                 
        self.master = master
    #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
    #Creation of init_window
    def init_window(self):
        
        global entry, s, playB,helpB,quitB,bgi
        bgi= ImageTk.PhotoImage(Image.open('ps.png'))
    # changing the title of our master widget      
        self.master.title("MAIN MENU")
    # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        limg= Label(self, i=bgi)
        limg.pack()
    # creating a button instance
        # gg=Tk()
        # label1=Label(self,text="ENTER THE PLAYER NAME:")
        # s = StringVar()
        # entry = Entry(gg, textvariable=s)
        # button=Button(gg,text="OK",command=self.client_getname)
        # entry.grid()
        # button.grid()
        playB= ImageTk.PhotoImage(Image.open('Frame 1.png'))
        helpB= ImageTk.PhotoImage(Image.open('Frame 2.png'))
        quitB= ImageTk.PhotoImage(Image.open('Frame 3.png'))
        playButton = Button(self,image = playB,border= 0 ,borderwidth=0 ,padx =0,pady=0,highlightthickness=0,cursor="hand2",relief=FLAT,command = self.client_play)
        helpButton = Button(self,image = helpB, border=0,borderwidth=0 ,padx =0,pady=0,highlightthickness=0,cursor="hand2",relief=FLAT,command = self.client_help)
        quitButton = Button(self,image = quitB,border=0,borderwidth=0 ,padx =0,pady=0,highlightthickness=0,cursor="hand2",relief=FLAT,command = self.client_exit)
    # placing the button on my window
        # label1.place(x=142, y=20)
        playButton.place(x=200,y=70)
        helpButton.place(x=200,y=220)
        quitButton.place(x=200,y=370)
        # playButton.config(height=3, width=17)
        # helpButton.config(height=3, width=17)
        # quitButton.config(height=3,width=17)
    def client_getname(self):
        global e, s
        e=s.get()
        #e is the variable which will contain the name
    def client_exit(self):
        root.destroy()
    def client_play(self):
        #IMPORTING MODULES
        import pygame
        import time
        import random
        pygame.init()
        #SCREEN DIMENSIONS AND OTHER SPECIFICATIONS
        white=(255,255,255)
        black=(0,0,0)
        red=(250,0,0)
        green=(0,240,0)
        blue=(250,0,250)
        display_width=520
        display_height=360
        passed=0
        display=pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption("Fall Of The REDtangle")
        walkright=[pygame.image.load('R1.png'),
                pygame.image.load('R2.png'),
                pygame.image.load('R3.png'),
                pygame.image.load('R4.png'),
                pygame.image.load('R5.png'),
                pygame.image.load('R6.png'),
                pygame.image.load('R7.png'),
                pygame.image.load('R8.png'),
                pygame.image.load('R9.png')]
        walkleft=[pygame.image.load('L1.png'),
                pygame.image.load('L2.png'),
                pygame.image.load('L3.png'),
                pygame.image.load('L4.png'),
                pygame.image.load('L5.png'),
                pygame.image.load('L6.png'),
                pygame.image.load('L7.png'),
                pygame.image.load('L8.png'),
                pygame.image.load('L9.png')]
        background=pygame.image.load('back.png')
        standingchar=pygame.image.load('standing.png')
        block=pygame.image.load('redtangle.jpg')
        block2= pygame.image.load('Purptangle.jpeg')
        letter= pygame.image.load('letter.jpg')
        letter = pygame.transform.scale(letter, (display_width, display_height))
        smallblock= pygame.transform.scale(block, (1, 1))
        yeeting=True
        #FUNCTIONS
        def score(count):
            font=pygame.font.SysFont("jokerman",20)
            texttt=font.render("dodged:"+str(count),True,(255,255,255))
            display.blit(texttt,(0,0))
        def startc():
            font = pygame.font.SysFont("comicsansms", 45)
            text = font.render("DEATH", True, (250, 0, 0))
            start=True
            while start:
                for event in pygame.event.get():
                    if event .type==pygame.QUIT:
                        pygame.quit()
                        quit()
                display.blit(background,(0,0))
                FONtt=pygame.font.SysFont('magneto',45)
                textt = FONtt.render("THE REDtangle", True, (250, 0, 0))
                display.blit(textt,(220-text.get_width(),180-text.get_height()))
                mouse=pygame.mouse.get_pos()
                click=pygame.mouse.get_pressed()
                if 70+90>mouse[0]>70 and 260+40>mouse[1]>260:
                    pygame.draw.rect(display,(0,230,0),(70,260,90,40))
                    texty1=textb1.render("PLAY",True,(0,0,0))
                    display.blit(texty1,(248-text.get_width(),336-text.get_height()))
                    if click[0]==1:
                        loop()
                        pygame.quit()
                else:
                    pygame.draw.rect(display,(0,246,0),(70,260,90,40))
                    textb1=pygame.font.Font('freesansbold.ttf',20)
                    texty1=textb1.render("PLAY",True,(0,0,0))
                    display.blit(texty1,(245-text.get_width(),336-text.get_height()))
                if 320+90>mouse[0]>320 and 260+40>mouse[1]>260:
                    pygame.draw.rect(display,(0,230,0),(320,260,90,40))
                    texty1=textb1.render("QUIT",True,(0,0,0))
                    display.blit(texty1,(500-text.get_width(),335-text.get_height()))
                    if click[0]==1:
                        pygame.quit()
                        quit()
                else:
                    pygame.draw.rect(display,(0,246,0),(320,260,90,40))
                    texty1=textb1.render("QUIT",True,(0,0,0))
                    display.blit(texty1,(500-text.get_width(),335-text.get_height()))
                    
                pygame.display.flip()
                clock.tick(100) 
        def paused():
            pause=True
            while pause:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            pause=False
                        elif event.key==pygame.K_q:
                            pygame.quit()
                            quit()
                display.fill((0,0,0))
                font = pygame.font.SysFont("comicsansms", 45)
                text = font.render("DEATH", True, (250, 0, 0))
                fontt = pygame.font.SysFont("comicsansms",20)
                textt = font.render("PAUSE", True, (250, 0, 0))
                textt2=fontt.render("SPACE--->CONTINUE AND Q--->QUIT",True,(250,0,0))
                display.blit(textt,(180 - text.get_width(), 240 - text.get_height()))
                display.blit(textt2,(180-text.get_width(),340-text.get_height()))
                pygame.display.flip()
                clock.tick(100)
        def commitdie():
            global score ,count
            font = pygame.font.SysFont("comicsansms", 45)
            fonty = pygame.font.SysFont("comicsansms", 30)
            text = font.render("DEATH", True, (250, 0, 0))
            texty = fonty.render("SCORE:",True,(250 ,0 ,0 ))
            scorey=fonty.render(str(count),True,(250,0,0))
            display.fill((255, 255, 255))
            display.blit(scorey,(150,0))
            display.blit(texty,(0,0))
            display.blit(text,(150, 180))
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        False
                mouse=pygame.mouse.get_pos()
                click=pygame.mouse.get_pressed()
                if 70+90>mouse[0]>70 and 260+40>mouse[1]>260:
                    textb1=pygame.font.Font('freesansbold.ttf',20)
                    pygame.draw.rect(display,(0,230,0),(70,260,90,40))
                    texty1=textb1.render("Retry",True,(0,0,0))
                    display.blit(texty1,(245-text.get_width(),336-text.get_height()))
                    if click[0]==1:
                        count = 0
                        loop()
                        pygame.quit()
                else:
                    pygame.draw.rect(display,(0,246,0),(70,260,90,40))
                    textb1=pygame.font.Font('freesansbold.ttf',20)
                    texty1=textb1.render("Retry",True,(0,0,0))
                    display.blit(texty1,(245-text.get_width(),336-text.get_height()))
                pygame.display.flip()
        def pro(x,y,w,h,c):
            display.blit(block ,(x,y,w,h))
        def proPurp(x,y,w,h,c):
            display.blit(block2 ,(x,y,w,h))        
        def char(walk):
            display.blit(background,(0,0))
            
        def loop():
            global pause
            global e
            global count
            pup = False
            if count > 15: 
                pup = True
            x=0
            y=300
            width=40
            height=10
            start_time = pygame.time.get_ticks() 
            vel=10
            walk=0
            left=False
            right=False
            proxp = random.randrange(0,display_width)
            proyp =-10
            prox=random.randrange(0,display_width)
            proy=-10
            prospeed=10
            prowidth=30
            proheight=30
            yeeting=False
            trigger = False
            while not yeeting:
                press=pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        yeeting=False
                        pygame.quit()
                        quit()
                if walk+1>=27:
                    walk=0
                if left:
                    display.blit(walkleft[walk//3],(x,y))
                    walk+=1
                elif right:
                    display.blit(walkright[walk//3],(x,y))
                    walk+=1
                else:
                    display.blit(standingchar,(x,y))
                pygame.display.update()
                if press[pygame.K_LEFT]and x+13>vel:
                    x-=vel
                    left=True
                    right=False
                elif press[pygame.K_RIGHT]and x<545-width-vel-60:
                        x+=vel
                        left=False
                        right=True
                elif press[pygame.K_p]:
                    paused()
                else:
                    left=False
                    right=False
                    walk=0
                if proy>display_height:
                        proy=0-proheight
                        prox=random.randrange(0,display_width-10)
                        count+=1
                if proyp>display_height:
                        proyp=0-proheight
                        proxp=random.randrange(0,display_width-10)
                proy=proy+prospeed 
                proyp = proyp + prospeed
                score(count)
                pygame.display.update()
                char(walk)
                print(count)
                if count > 15 : 
                    proPurp(proxp,proyp,prowidth,proheight,red)
                    trigger = True
                pro(prox,proy,prowidth,proheight,red)
                clock.tick(45)           
                if proy+proheight-30==y-height:
                    if x > prox and x < prox + prowidth or x+width > prox and x + width < prox+prowidth+30:
                        commitdie()
                        start_time = pygame.time.get_ticks()
                        pygame.display.update()
                        break
                if proyp+proheight-30==y-height:
                    if (x > proxp and x < proxp + prowidth or x+width > proxp and x + width < proxp+prowidth+30 )& trigger:
                        commitdie()
                        start_time = pygame.time.get_ticks()
                        pygame.display.update()
                        break
                    else : 
                        continue

        startc()
        loop()
        pygame.quit()
        quit()
        
    def client_help(self):
        hellp = Tk()
        messagebox.showinfo("INSTRUCTIONS", "1.Use the right arrow key to move rightwards and the left arrow key to move leftwards.\n"
                            "2.The aim of the game would be to survive as long as you can by dodging the redtangles falling from the sky\n"
                            "3.Compete with your fellow buddies and try scoring world records!!!\n"
                            "4.PRESS P TO PAUSE\n"                                                                   
                            "5.Your score will be determined by the total time you have survived")

root = Tk()
root.geometry("600x500")
#creation of an instance
app = Window(root)
#mainloop 
root.mainloop()



