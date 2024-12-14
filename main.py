from tkinter import *
from tkinter import Tk,StringVar, ttk

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

# criando janela 
janela=Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")

#criando frames 
frameCima=Frame(janela, width= 1043, height= 50, bg= co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio=Frame(janela,width=1043,height=303,bg=co1,pady=20,relief=FLAT)
frameMeio.grid(row=1, column=0,pady=1,padx=0,sticky=NSEW)

frameBaixo=Frame(janela,width=1043,height=303,bg=co1,relief=FLAT)
frameBaixo.grid(row=2, column=0,pady=0,padx=1,sticky=NSEW)

#abrindo imagem 
app_img = Image.open('estoque.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img,text=" Controle de estoque", width=900,compound=LEFT,relief=RAISED,anchor=NW,font=("Verdana 20 bold"), bg = co1, fg = co4,padx=10)
app_logo.place(x=0, y=0)

### frame meio (entradas)
l_nome= Label(frameMeio, text="Nome", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_nome.place(x= 10, y=10)
entrada_nome= Entry(frameMeio, width=25, justify='left',relief=SOLID)
entrada_nome.place(x= 130, y= 11)

l_descricao= Label(frameMeio, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_descricao.place(x= 10, y=40)
entrada_descricao= Entry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_descricao.place(x= 130, y= 41)

l_marca= Label(frameMeio, text="Marca", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_marca.place(x= 10, y=70)
entrada_marca= Entry(frameMeio, width=25, justify='left',relief=SOLID)
entrada_marca.place(x= 130, y= 72)

l_data_compra= Label(frameMeio, text="Data da compra ", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_data_compra.place(x= 10, y=100)
entrada_data_compra= DateEntry(frameMeio, width=14, justify='left',relief=SOLID)
entrada_data_compra.place(x= 130, y= 101)

l_quantidade= Label(frameMeio, text="Quantidade", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_quantidade.place(x= 10, y=132)
entrada_quantidade = Spinbox(frameMeio, from_=0, to=100, width=10, justify='center', relief=SOLID)
entrada_quantidade.place(x= 130, y= 133)

l_serie= Label(frameMeio, text="Número de série ", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_serie.place(x= 10, y=163)
entrada_serie= Entry(frameMeio, width=25, justify='left',relief=SOLID)
entrada_serie.place(x= 130, y= 163)

l_marca=Label(frameMeio, text='Imagem do produto')

janela.mainloop()
