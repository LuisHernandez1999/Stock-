import sqlite3 as lite

con = lite.connect('dados.db')

# inserir dados no inventário
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = """
            INSERT INTO inventario(
                nome, descricao, marca, quantidade, data_da_compra,
                valor_da_compra, serie, imagem, fornecedor_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, i)

# ver todos os dados do inventário com o nome do fornecedor
def ver_form():
    with con:
        cur = con.cursor()
        query = """
            SELECT
                inventario.id,
                inventario.nome,
                inventario.descricao,
                inventario.marca,
                inventario.quantidade,
                inventario.data_da_compra,
                inventario.valor_da_compra,
                inventario.serie,
                inventario.imagem,
                fornecedor.nome AS fornecedor_nome
            FROM inventario
            LEFT JOIN fornecedor ON inventario.fornecedor_id = fornecedor.id
        """
        cur.execute(query)
        return cur.fetchall()

# atualizar dados no inventário
def atualiza(i):
    with con:
        cur = con.cursor()
        query = """
            UPDATE inventario SET
                nome=?, descricao=?, marca=?, quantidade=?, data_da_compra=?,
                valor_da_compra=?, serie=?, imagem=?, fornecedor_id=?
            WHERE id=?
        """
        cur.execute(query, i)

# deletar dados do inventário
def deletar_inventario(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, (i,))

# ver item único do inventário
def ver_item(id):
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, (id,))
        return cur.fetchall()

# inserir dados no fornecedor
def inserir_fornecedor(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO fornecedor(nome, cnpjcpf) VALUES (?, ?)"
        cur.execute(query, i)

# ver todos os dados dos fornecedores
def ver_fornecedor():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM fornecedor"
        cur.execute(query)
        return cur.fetchall()

# atualizar dados do fornecedor
def atualiza_fornecedor(i):
    with con:
        cur = con.cursor()
        query = "UPDATE fornecedor SET nome=?, cnpjcpf=? WHERE id=?"
        cur.execute(query, i)

# deletar dados do fornecedor
def deletar_fornecedor(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM fornecedor WHERE id=?"
        cur.execute(query, (i,))

# ver item único do fornecedor
def ver_item_fornecedor(id):
    with con:
        cur = con.cursor()
        query = "SELECT * FROM fornecedor WHERE id=?"
        cur.execute(query, (id,))
        return cur.fetchall()
### totais 
def ver_totais():
    with con:
        cur = con.cursor()
        query = """
            SELECT 
                SUM(quantidade) AS total_quantidade,
                SUM(quantidade * valor_da_compra) AS valor_total_estoque
            FROM inventario
        """
        cur.execute(query)
        resultado = cur.fetchone()
        return resultado