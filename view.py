import sqlite3 as lite 

con=lite.connect('dados.db')


### inserir dados 
def inserir_form(i):
  with con :
    cur= con.cursor ()
    query = "INSERT INTO inventario(nome,descricao,marca,quantidade,data_da_compra,valor_da_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,i)
### ver dados 
def ver_form():
  ver_dados=[]
  with con:
    cur=con.cursor()
    query= "SELECT * FORM inventario "
    cur.execute(query, ver_dados)

    rows = cur.fetchall()
    for row in rows :
        ver_dados.append(row)
    return ver_dados
### atualizar dados 
def atualiza(i):
 with con:
    cur= con.cursor()
    query= "UPDATE inventario SET nome=? ,descricao=? ,marca=? ,quantidade= ?,data_da_compra= ?,valor_da_compra=?,serie=?,imagem=? WHERE id = ?"
    cur.execute(query,i)
### deletar dados 
def deletar_form(i):
 with con:
    cur=con.cursor()
    query="DELETE FROM  inventario WHERE id=?"
    cur.execute(query,i)
### ver item unico 
def ver_item(id):
  ver_dados_item = []
  with con:
    cur=con.cursor()
    query="SELECT FROM inventario WHERE id=?"
    cur.execute(query,id)

    rows=cur.fetchall()
    for row in rows:
      ver_dados_item.append(row)


