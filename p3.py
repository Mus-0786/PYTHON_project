from tkinter import *
from PIL import Image,ImageTk
from random import randint

window=Tk()
window.title("Rock Paper Scissor")


rock1=ImageTk.PhotoImage(Image.open("rock.png"))
paper1=ImageTk.PhotoImage(Image.open("paper1.png"))
scissor1=ImageTk.PhotoImage(Image.open("scissor.png"))
rock2=ImageTk.PhotoImage(Image.open("rock.png"))
paper2=ImageTk.PhotoImage(Image.open("paper1.png"))
scissor2=ImageTk.PhotoImage(Image.open("scissor.png"))

computer=Label(window, image=scissor1)
player=Label(window, image=scissor2)
computer.grid(row=0, column=0, padx=20, pady=20)
player.grid(row=0, column=4, padx=20, pady=20)

c_indicator=Label(window,font=('arial',30,"bold"),text="COMPUTER",bg="purple",fg="blue")
p_indicator=Label(window,font=('arial',30,"bold"),text="PLAYER",bg="purple",fg="blue")

c_indicator.grid(row=1,column=0)
p_indicator.grid(row=1,column=4)

def mssg_update(a):
    message['text']=a
def Computer_update():
    final=int(c_score['text'])
    final +=1
    c_score['text']=str(final)
def p_update():
      final=int(p_score['text'])
      final +=1
      p_score['text']=str(final)
def  winner(p,c):
    if p==c:
        mssg_update("It's a tie")
    elif p=="rock":
         if c=="paper":
              mssg_update("Computer Wins !!")
              Computer_update()
         else: 
               mssg_update("Player Wins !!")
               p_update()
    elif p=="paper":
          if c=="scissor":
              mssg_update("Computer Wins !!")
              Computer_update()
          else:
               mssg_update("Player Wins !!")
               p_update()
    elif p=="scissor":
          if c=="rock":
              mssg_update("Computer Wins !!")
              Computer_update()
          else:
               mssg_update("Player Wins !!")
               p_update()   
    else:
        pass
       
img_comp = Label(window, bg="white")
img_comp.grid(row=1, column=3, padx=20, pady=20)


img_player = Label(window, bg="white")
img_player.grid(row=1, column=1, padx=20, pady=20)
    
    
to_select=["rock","paper","scissor"]

def choice_update(a):
    choice_comp=to_select[randint(0,2)]
    if choice_comp=="rock":
        img_comp.configure(image=rock2)
    elif choice_comp=="paper":
        img_comp.configure(image=paper2)
    else:
         img_comp.configure(image=scissor2)
    if a=="rock":
         img_player.configure(image=rock1)
    elif choice_comp=="paper":
         img_player.configure(image=paper1)
    else:
         img_player.configure(image=scissor1)
         
    winner( a,choice_comp)      
    
message=Label(window,font=("arial",30,"bold"),bg="white",fg="red")
message.grid(row=0,column=2)
c_score=Label(window,font=('arial',40,"bold"),text=0,fg="blue")
p_score=Label(window,font=('arial',40,"bold"),text=0,fg="blue")
c_score.grid(row=2,column=0)
p_score.grid(row=2,column=4)
rock=Button(window,width=8, height=2, text="ROCK",font=("arial",20,"bold"),bg="lightblue",fg="red",command=lambda: choice_update("rock")).grid(row=3,column=1, pady=20)
paper=Button(window,width=8, height=2, text="PAPER",font=("arial",20,"bold"),bg="lightblue",fg="red",command=lambda: choice_update("paper")).grid(row=3,column=2, pady=20)

scissor=Button(window,width=8, height=2, text="SCISSOR",font=("arial",20,"bold"),bg="lightblue",fg="red", command=lambda: choice_update("scissor")).grid(row=3,column=3, pady=20)



window.mainloop()

