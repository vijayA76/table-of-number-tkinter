import tkinter as t

mainframe=t.Tk()
mainframe.title("Table Print")
mainframe.geometry('250x200')
mainframe.resizable(False,False)
mainframe["background"]='darkgrey'

L1=t.Label(mainframe,text="Adjust the scale to take Number",font=('Georgia', 10, 'bold'))
L1.place(x=9,y=20)

num=t.IntVar()
num_=t.Scale(mainframe,from_=1,to=20,orient='horizontal',variable=num )
num_.place(x=70,y=70)

def table():
    frame=t.Tk()
    frame.geometry('150x270')
    a=num.get()
    v=6
    for i in range(1,11,1):
        z=str(a)+" "+'x'+" "+str(i)+" "+'='+" "+str(a*i)+"\n"        
        L2=t.Label(frame,text=z,font=('Gaudy old style', 14, 'italic'),fg='royalblue')
        L2.place(x=18,y=v)
        v+=25
       
tbutton=t.Button(mainframe,text="Print Table",command=table)
tbutton.place(x=90,y=140)
