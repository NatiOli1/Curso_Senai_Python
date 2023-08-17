import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute(
    """
    DELETE FROM alunos;
    """
)
conn.commit()
conn.close()