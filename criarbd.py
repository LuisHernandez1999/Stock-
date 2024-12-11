import sqlite3 as lite


con = lite.connect("dados.bd")

with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE  inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            local TEXT,
            descricao TEXT,
            marca TEXT,
            data_da_compra DATE,
            quantidade INTEGER,
            valor_da_compra DECIMAL,
            serie TEXT,
            imagem TEXT
        )
    """)
