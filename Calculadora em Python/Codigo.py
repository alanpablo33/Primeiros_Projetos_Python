#bibliotecas para transformar em .exe
import pandas as pd
import win32com.client as win32

# importar o TK Criador de janelas
from ctypes.wintypes import SIZE
from tkinter import *
from tkinter import ttk
import tkinter

#minuto52
#Cores definidas

cor1= "#36322f" # cinza mais escuro
cor2= "#050505" #Preto
cor3= "#423d37" #cinza escuro
cor4= "#756e65" #cinza
cor5= "#fc8803" #laranja

#janela do app
janela =Tk()
#titulo do app
janela.title("Calculadora_Alan")
#tamanho da janela do app
janela.geometry("233x268")
#Configuração de Cores para a janela
janela.config(bg=cor2)

#Separando o Display do app, tamanho do display
frame_tela = Frame(janela, width=250, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

#Corpo da calculadora
frame_corpo = Frame(janela, width=250, height=268, bg=cor4)
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todos_valores = ' '

#Tela Label
valor_texto = StringVar()

#criando função
def entrar_valor(evento):
      
 global todos_valores

 todos_valores = todos_valores + str(evento)

 #passando valor para tela
 valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


app_label = Label(frame_tela , textvariable=valor_texto , width=16,height=2 , padx=7 , relief=FLAT, anchor="e", justif= RIGHT ,font=('Ivy 18 '), bg=cor1 ,fg=cor5)
app_label.place(x=0 , y=0)

#Criando Botoes 
#bg,fg e font
b_c = Button(frame_corpo, command= limpar_tela, text="C",width=12, height=2, bg=cor4 , fg=cor2, font=('Times 9 bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=5,y=2)

b_g = Button(frame_corpo,command = calcular, text="=", width=8 , height=2, bg=cor3, font=('Ivy 9 bold'))
b_g.place(x=101,y=175)

b_b = Button(frame_corpo, command = lambda: entrar_valor('%') , text="%", width= 8 , height=2, bg=cor5 , relief=RAISED, overrelief=RIDGE, font=('Ivy 9 bold'))
b_b.place(x=101,y=2)

b_a = Button(frame_corpo, command = lambda: entrar_valor('/'),text="/", width=7 , height=2, bg=cor5, relief=RAISED, overrelief=RIDGE, font=('Ivy 9 bold'))
b_a.place(x=170,y=2)

b_c = Button(frame_corpo, command = lambda: entrar_valor('+'), text="+", width=7 , height=2, bg=cor5, relief=RAISED, overrelief=RIDGE,font=('Ivy 9 bold'))
b_c.place(x=170,y=132)

b_d = Button(frame_corpo, command = lambda: entrar_valor('-'), text="-", width=7 , height=2, bg=cor5, relief=RAISED, overrelief=RIDGE,font=('Ivy 9 bold'))
b_d.place(x=170,y=89)

b_e = Button(frame_corpo, command = lambda: entrar_valor('*') ,text="*", width=7 , height=2, bg=cor5 , relief=RAISED, overrelief=RIDGE,font=('Ivy 9 bold'))
b_e.place(x=170,y=45)

b_f = Button(frame_corpo, command = lambda: entrar_valor('.'),text=".", width=7 , height=2, bg=cor5 , relief=RAISED, overrelief=RIDGE,font=('Ivy 9 bold'))
b_f.place(x=170,y=175)

# Numeros
b_1 = Button(frame_corpo, command = lambda: entrar_valor('1') ,text="1", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_1.place(x=5,y=132)

b_2 = Button(frame_corpo,command = lambda: entrar_valor('2'), text="2", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_2.place(x=53,y=132)

b_3 = Button(frame_corpo,command = lambda: entrar_valor('3'), text="3", width=8 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_3.place(x=101,y=132)

b_4 = Button(frame_corpo, command = lambda: entrar_valor('4'), text="4", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_4.place(x=5,y=89)

b_5 = Button(frame_corpo,command = lambda: entrar_valor('5'), text="5", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_5.place(x=53,y=89)

b_6 = Button(frame_corpo, command = lambda: entrar_valor('6') ,text="6", width=8 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_6.place(x=101,y=89)

b_7 = Button(frame_corpo, command = lambda: entrar_valor('7'), text="7", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_7.place(x=5,y=45)

b_8 = Button(frame_corpo, command = lambda: entrar_valor('8') ,text="8", width=5 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_8.place(x=53,y=45)

b_9 = Button(frame_corpo, command = lambda: entrar_valor('9'),text="9", width=8 , height=2, bg=cor3,font=('Ivy 9 bold'))
b_9.place(x=101,y=45)

b_0 = Button(frame_corpo,command = lambda: entrar_valor('0'), text="0", width=12 , height=2, bg=cor3 , fg=cor5, font=('Ivy 9 bold'))
b_0.place(x=5,y=175)



#Comando usado para manter a janela aberta
janela.mainloop()
