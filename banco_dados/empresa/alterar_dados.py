import sqlite3
from constantes import DATABASE_NAME

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
cursor.execute(
    """
    UPDATE clientes SET cidade = ?, uf = ?
    """, ("Patos de Minas", "MG")
)


cursor.execute(
    """
    UPDATE clientes SET nome = ?, email = ?
    WHERE id = ?
    """, ("Sebastião Santos", "sebastiao@gmail.com", 6)
)

ids = [1, 3, 6, 8]
cursor.execute(
    """
    UPDATE clientes SET uf = ? WHERE id IN (?)
    """, ("RJ", ", ".join(ids))
)

cursor.execute(
    """
    DELETE FROM clientes WHERE id = ?
    """, (6,)
)

connection.commit()
connection.close()
