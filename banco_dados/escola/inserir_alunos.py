import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO alunos (nome, ra, email, disciplina, nota1, nota2) VALUES 
    ('Silas Silva', 123123, 'silas@gmail.com', 'POO', 4.5, 2.3)
    """
)
cursor.execute(
    """
    INSERT INTO alunos (nome, ra, email, disciplina, nota1, nota2) VALUES 
    ('Maria Silva', 123123, 'maria@gmail.com', 'POO', 6.5, 5.5)
    """
)

conn.commit()
conn.close()
