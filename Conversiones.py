# -*- coding: cp1252 -*-
from Tkinter import *
def con():
    q=de(op)
    p=a(op2)
    if q==1 and p==1:
        r.set( float( c.get() )*1000)
    elif q=="Metros" and p=="Kilometros":
        r.set( float( c.get() )/1000)
    elif q=="Metros" and p=="Pies":
        r.set( float( c.get() )*3.281)
    elif q=="Pies" and p=="Metros":
        r.set( float( c.get() )/3.281)
    elif q=="Centimetros" and p=="Pulgadas":
        r.set( float( c.get() )/2.54) 
    elif q=="Yardas" and p=="Metros":
        r.set( float( c.get() )/1.094) 
    elif q=="Millas" and p=="Kilometros":
        r.set( float( c.get() )*1.609)
    elif q=="Grados C" and p=="Grados F":
        r.set( float( c.get() )* (9/5) + 32) 
        
def de(op):
    global q
    if op==OptionList[0]:
        q=1
        trr.set("Km")
    elif op==OptionList[1]:
        q="Metros"
        trr.set("M")
    elif op=="Metros":
        q="Metros"
        trr.set("M")
    elif op=="Pies":
        q="Pies"
        trr.set("Ft")
    elif op=="Centimetros":
        q="Centimetros"
        trr.set("Cm")
    elif op=="Yardas":
        q="Yardas"
        trr.set("Yd")
    elif op=="Millas":
        q="Millas"
        trr.set("Milles")
    elif op=="Grados C":
        q="Grados C"
        trr.set("C°")
    return q
        
def a(op2):
    global p
    if op2=="Metros":
        p=1
        trrr.set("M")
    elif op2=="Kilometros":
        p="Kilometros"
        trrr.set("Km")
    elif op2=="Pies":
        p="Pies"
        trrr.set("Ft")
    elif op2=="Metros":
        p="Metros"
        trrr.set("M")
    elif op2=="Pulgadas":
        p="Pulgadas"
        trrr.set("P")
    elif op2=="Metros":
        p="Metros"
        trrr.set("M")
    elif op2=="Kilometros":
        p="Kilometros"
        trrr.set("Km")
    elif op2=="Grados F":
        p="Grados F"
        trrr.set("F°")
    return p
       



OptionList = [
"Kilometros",
"Metros",
"Pies",
"Centimetros",
"Yardas",
"Millas",
"Grados C",
]
OptionList2 = [
"Metros",
"Kilometros",
"Pies",
"Pulgadas",
"Grados F",
]


root=Tk()
root.title("Conversiones uwu")
root.geometry("300x200")
root.config(bg="mint cream")
q=1
p=1
c=StringVar()
r=StringVar()
trr=StringVar()
trrr=StringVar()
trr.set("Km")
trrr.set("M")
op=StringVar(root)
op.set(OptionList[0])
op2=StringVar(root)
op2.set(OptionList2[0])
Label(root, text="Convertir de:", bg="mint cream", font=("Fixedsys"), anchor="c").place(x=10, y=10)
Label(root, text="Convertir a:", bg="mint cream", font=("Fixedsys"), anchor="c").place(x=150, y=10)
opt = OptionMenu(root, op,command=de, *OptionList)
opt.config(width=10, font=('Arial', 9), bg='lavender')
opt.place(x=10, y=40)
opt2 = OptionMenu(root, op2, command=a, *OptionList2)
opt2.config(width=10, font=('Arial', 9), bg='lavender')
opt2.place(x=150, y=40)
Entry(root, width=11, justify=LEFT, textvariable=c).place(x=10, y=100)
Entry(root, width=11, justify=CENTER, state=DISABLED, textvariable=r).place(x=150, y=100)
Label(root, textvariable=trr, bg="mint cream", font=("Fixedsys"), anchor="c").place(x=80, y=100)
Label(root, textvariable=trrr, bg="mint cream", font=("Fixedsys"), anchor="c").place(x=225, y=100)
Button(root, text="Aceptar", command=con, font=("Fixedsys",9), bg='lavender').place(x=100, y=150)
root.mainloop()


