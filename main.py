from tkinter import *
from tkinter import Tk,StringVar, ttk

from PIL import Image, ImageTk

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
app_logo = Label(frameCima, image=app_img,text="Estoque", width=900,compound=LEFT,relief=RAISED,anchor=NW,font=("Verdana 20 bold"), bg = co1, fg = co4)
app_logo.place(x=0, y=0)
janela.mainloop()
