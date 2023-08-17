import sqlite3
from constantes import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO clientes 
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES 
    ('Alfredo Santos', 22, '123123123', 'alfredo@gmailcom',
    '19-91212-8989', 'Piracicaba', 'SP', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes 
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES 
    ('Maria Santos', 55, '567567567', 'maria@gmailcom',
    '19-95678-8989', 'Rio das Pedras', 'SP', '2023-07-18')
    """
)
cursor.execute(
    """
    INSERT INTO clientes 
    (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES 
    ('Danilo Santos', 35, '987345123', 'danilo@gmailcom',
    '19-91234-6578', 'Americana', 'SP', '2023-07-18')
    """
)
conn.commit()
conn.close()
