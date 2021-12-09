# -*- coding: cp1252 -*-
def con():
    op=raw_input("Convertir:")
    op2=raw_input("a:")
    if op=="Km" and op2=="M":
        KmM()
    elif op=="M" and op2=="Km":
        MKm()
    elif op=="M" and op2=="Ft":
        MFt()
    elif op=="Ft" and op2=="M":
        FtM()
    elif op=="Cm" and op2=="P":
        cmP()
    elif op=="Yd" and op2=="M":
        ydM()
    elif op=="Mile" and op2=="Km":
        mileKm()
    elif op=="Celsius" and op2=="Farenheit":
        CF()
    else:
        print "ERROR"

def KmM():
    Km=float(input("Dame los kilómetros:"))
    m=Km*1000
    print "Eso es equivalente a",m,"metros"

def MKm():
    m=float(input("Dame los metros:"))
    Km=m/1000
    print"Eso es equivalente a",Km,"kilómetros"
      
def MFt():
    m=float(input("Dame los metros:"))
    ft=m*3.281
    print "Eso es equivalente a",ft,"pies"

def FtM():
    Ft=float(input("Dame los pies:"))
    m=Ft/3.281
    print"Eso es equivalente a",m,"metros"

def cmP():
    cm=float(input("Dame los centimetros:"))
    P=cm/2.54
    print"Eso es queivalente a",P,"pulgadas"

def ydM():
    yd=float(input("Dame las yardas:"))
    m=yd/1.094
    print "Eso es equivalente a",m,"metros"

def mileKm():
    mile=float(input("Dame las millas:"))
    Km=mile*1.609
    print"Eso es equivalente a",Km,"kilómetros"

def CF():
    c=float(input("Dame grado Celsius:"))
    f=( c * (9/5)) + 32
    print"Eso es equivalente a",f,"grado Fahrenheit"

con()

