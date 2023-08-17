import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
clientes = cursor.execute("""SELECT * FROM clientes""")

for cliente in clientes.fetchall():
    print(f"Cliente: {cliente['nome']}")
    print(f"Cliente: {cliente[1]}, email: {cliente[4]}")

print("----------------------------------------------------")

clientes_10 = cursor.execute(
    """SELECT * FROM clientes LIMIT 3"""
)

for cliente in clientes_10.fetchall():
    print(f"Cliente: {cliente[1]}, email: {cliente[4]}")

print("----------------------------------------------------")

clientes_rio = cursor.execute(
    """SELECT * FROM clientes WHERE cidade = 'Rio das Pedras'"""
)

for cliente in clientes_rio.fetchall():
    print(f"Cliente: {cliente[1]}, cidade: {cliente[6]}")

print("----------------------------------------------------")

cliente_rio_55 = cursor.execute(
    """SELECT * FROM clientes 
        WHERE cidade = 'Rio das Pedras' 
        AND idade = 55"""
)

for cliente in cliente_rio_55.fetchall():
    print(f"Cliente: {cliente[1]}, idade: {cliente[2]}, "
          f"cidade: {cliente[6]}")

print("----------------------------------------------------")

clientes_nome_email = cursor.execute(
    """
    SELECT nome, email FROM clientes 
    WHERE cidade = 'Rio das Pedras'
    """
)

for cliente in clientes_nome_email.fetchall():
    print(f"Cliente: {cliente[0]}, email: {cliente[1]}")

conn.close()
