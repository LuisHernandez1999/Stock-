import sqlite3 as lite

con = lite.connect("dados.bd")

# criando a tabela 'fornecedor'
with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE fornecedor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cnpjcpf TEXT
        )
    """)

# criando a tabela 'inventario' com chave estrangeira para 'fornecedor'
with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            fornecedor_id INTEGER,
            local TEXT,
            descricao TEXT,
            marca TEXT,
            data_da_compra DATE,
            quantidade INTEGER,
            valor_da_compra DECIMAL,
            serie TEXT,
            imagem TEXT,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedor (id)
        )
    """)
