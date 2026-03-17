from tkinter import *
import random


def comp_win():
    c=Tk()
    b.destroy()

    sco=Label(c,text="Player Score: "+str(score)+" | Computer Score: "+str(comp_score),font=("normal",10))
    sco.grid(row=0,column=0,columnspan=6)
comp_score =0
def compcha():
    def but1(num1):
        global comp_score
        global c
        comp =random.randint(0,6)
        

        if num1 == comp:
            Label(b,text="Game Over",font=("normal",10)).grid(row=4,column=0,columnspan=6)

            comp_win()
            if comp_score == score:
                Label(c,text="Tie",font=("normal",10)).grid(row=5,column=0,columnspan=6)
        elif comp == 0:
            comp_score+=num1

        elif comp_score >= score:
            comp_win()

        else:
            comp_score+=comp
            
            
        
        sc.config(text="player: "+str(num1)+" | Computer : "+str(comp))
        sco.config(text="Player Score: "+str(score)+" | Computer Score: "+str(comp_score))
    global b
    b=Tk()
    a.destroy()
    
    sc=Label(b,text="",font=("normal",10))
    sc.grid(row=1,column=0,columnspan=6)
    sco=Label(b,text="Player Score: "+str(score)+" | Computer Score: 0",font=("normal",10))
    sco.grid(row=2,column=0,columnspan=6)

    Button(b,text="0",command=lambda: but1(0)).grid(row=3,column=0)
    Button(b,text="1",command=lambda: but1(1)).grid(row=3,column=1)
    Button(b,text="2",command=lambda: but1(2)).grid(row=3,column=2)
    Button(b,text="3",command=lambda: but1(3)).grid(row=3,column=3)
    Button(b,text="4",command=lambda: but1(4)).grid(row=3,column=4)
    Button(b,text="5",command=lambda: but1(5)).grid(row=3,column=5)
    Button(b,text="6",command=lambda: but1(6)).grid(row=3,column=6)

#************************************************************************************
score=0
def but(num):
    global score
    comp =random.randint(0,6)
    
    
    if num == comp:
        compcha()
    elif num == 0:
        score+=comp
    else:
        score+=num
        
    s_1.config(text="player: "+str(num)+" | Computer : "+str(comp))
    s_2.config(text="Player Score: "+str(score)+" | Computer Score: 0")
    
a=Tk()

s_1=Label(a,text="You Are Batting",font=("normal",10))
s_1.grid(row=1,column=0,columnspan=6)
s_2=Label(a,text="",font=("normal",10))
s_2.grid(row=2,column=0,columnspan=6)

Button(a,text="0",command=lambda: but(0)).grid(row=3,column=0)
Button(a,text="1",command=lambda: but(1)).grid(row=3,column=1)
Button(a,text="2",command=lambda: but(2)).grid(row=3,column=2)
Button(a,text="3",command=lambda: but(3)).grid(row=3,column=3)
Button(a,text="4",command=lambda: but(4)).grid(row=3,column=4)
Button(a,text="5",command=lambda: but(5)).grid(row=3,column=5)
Button(a,text="6",command=lambda: but(6)).grid(row=3,column=6)

a.mainloop()
