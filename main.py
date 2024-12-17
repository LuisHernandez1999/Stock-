from tkinter import *
from tkinter import Tk,StringVar, ttk
import tkinter.messagebox
from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import * 

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
entrada_nome= Entry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_nome.place(x= 130, y= 11)

l_descricao= Label(frameMeio, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_descricao.place(x= 10, y=40)
entrada_descricao= Entry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_descricao.place(x= 130, y= 41)

l_valor= Label(frameMeio, text="Valor", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_valor.place(x= 10, y=70)
entrada_valor= Entry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_valor.place(x= 130, y= 72)

l_data_compra= Label(frameMeio, text="Data da compra ", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_data_compra.place(x= 10, y=100)
entrada_data_compra= DateEntry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_data_compra.place(x= 130, y= 101)

l_quantidade= Label(frameMeio, text="Quantidade", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_quantidade.place(x= 10, y=132)
entrada_quantidade = Spinbox(frameMeio, from_=0, to=100, width=30, justify='center', relief=SOLID)
entrada_quantidade.place(x= 130, y= 133)

l_serie= Label(frameMeio, text="Número de série ", height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1,fg =co4)
l_serie.place(x= 10, y=163)
entrada_serie= Entry(frameMeio, width=30, justify='left',relief=SOLID)
entrada_serie.place(x= 130, y= 163)

## bs
l_carregar=Label(frameMeio, text='Imagem do produto', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10,y=193)
b_carregar= Button(frameMeio,width=30,text='carregar'.upper(),compound=CENTER, anchor=CENTER, overrelief=RIDGE,font=('Ivy 8 '),bg=co1,fg=co0)
b_carregar.place(x=140, y=191)

## inserir b
img_add = Image.open('addbtt.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
######## criando funcoes 
global tree

### inserir 
def inserir():
    global imagem, imagem_string, l_imagem

    nome= entrada_nome.get()
    descricao= entrada_descricao.get()
    quantidade= entrada_quantidade.get()
    data=entrada_data_compra.get()
    valor= entrada_valor.get()
    serie= entrada_serie.get()
    imagem= imagem_string

    listra_inserir = [nome,descricao,quantidade,data,valor,serie,imagem]

    for i in listra_inserir:
        if i =="":
            tkinter.messagebox.showerror('Erro','Preencha todos os campos')
            return 
    inserir_form(listra_inserir)
    tkinter.messagebox.showinfo('Sucesso','Os dados foram inseridos')

    nome.delete(0,'end')
    descricao.delete(0,'end')
    quantidade.delete(0,'end')
    data.delete(0,'end')
    valor.delete(0,'end')
    serie.delete(0,'end')

    for widget in frameMeio.winfo_children():
         widget.destroy()
    
            
    


b_inserir= Button(frameMeio, image=img_add,width=95,text='Adicionar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8 '),bg=co1,fg=co0)
b_inserir.place(x=350, y=10)


## update b
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)


b_atualizar= Button(frameMeio, image=img_update,width=95,text='Atualizar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8 '),bg=co1,fg=co0)
b_atualizar.place(x=350, y=50)

## delete b 

img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)


b_atualizar= Button(frameMeio, image=img_delete,width=95,text='Deletar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8 '),bg=co1,fg=co0)
b_atualizar.place(x=350, y=90)


## b ver item 
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)


b_item= Button(frameMeio, image=img_item,width=95,text='Ver item'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE,font=('Ivy 8 '),bg=co1,fg=co0)
b_item.place(x=350, y=190)

## labels qtnd total e valores 
l_total= Label(frameMeio, text=" ",width=14 ,height=2, anchor=NW, font=('Ivy 17 bold'), bg= co7,fg =co1)
l_total.place(x= 510, y=17)
l_total= Label(frameMeio, text=" Valor total", anchor=NW, font=('Ivy 17 bold'), bg= co7,fg =co1)
l_total.place(x= 520, y=27)

l_quantidade_total= Label(frameMeio, text=" ",width=18 ,height=2, anchor=NW, font=('Ivy 17 bold'), bg= co7,fg =co1)
l_quantidade_total.place(x= 510, y=97)
l_quantidade_total= Label(frameMeio, text="Quantidade total", anchor=NW, font=('Ivy 17 bold'), bg= co7,fg =co1)
l_quantidade_total.place(x= 520, y=107)

def mostrar():
   
   tabela_head = ['#Item','Nome', 'Descrição', 'Marca', 'Data da compra','Quantidade', 'Número de série','Fornecedor']

   lista_itens = []



   tree = ttk.Treeview(frameBaixo, selectmode="extended",columns= tabela_head, show="headings")

  ## vertical scrollbar
   vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

## horizontal scrollbar
   hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

   tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
   tree.grid(column=0, row=0, sticky='nsew')
   vsb.grid(column=1, row=0, sticky='ns')
   hsb.grid(column=0, row=1, sticky='ew')
   frameBaixo.grid_rowconfigure(0, weight=12)
 
   hd=["center","center","center","center","center","center","center", 'center']
   h=[40,150,100,160,130,100,100, 100]
   n=0

   for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
  
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


##inserindo os itens dentro da tabela
    for item in lista_itens:
      tree.insert('', 'end', values=item)

# Obter os totais diretamente das funções
   Total_quantidade = quantidade_total_estoque()  # Função que calcula a soma da quantidade
   Total_valor = valor_total_estoque()            # Função que calcula o valor total do estoque

# Atualizar os labels com os valores calculados
   l_quantidade_total['text'] = f"Total de Itens: {Total_quantidade}"
   l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)

mostrar()


janela.mainloop()
