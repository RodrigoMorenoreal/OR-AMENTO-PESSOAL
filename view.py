import sqlite3 as lite

con = lite.connect('dados.db')


# Inserir Categorias

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, (i))


# Inserir Receitas

def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i))


# Inserir Gastos    

def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i))


# deletar Categoria

def deletar_categoria(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Categoria WHERE id = ?"
        cur.execute(query, (i,))

# deletar Receita

def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query, (i,))

# deletar Gasto

def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id = ?"
        cur.execute(query, (i,))

# visualizar Categorias

def visualizar_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Categoria"
        cur.execute(query)
        resultado = cur.fetchall()
        for l in resultado:
            lista_itens.append(l)

    return lista_itens

# visualizar Receitas

def visualizar_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Receitas"
        cur.execute(query)
        resultado = cur.fetchall()
        for l in resultado:
            lista_itens.append(l)

    return lista_itens  

# visualizar Gastos

def visualizar_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Gastos"
        cur.execute(query)
        resultado = cur.fetchall()
        for l in resultado:
            lista_itens.append(l)

    return lista_itens  

# editar Categoria

def editar_categoria(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Categoria SET nome = ? WHERE id = ?"
        cur.execute(query, (i)) 