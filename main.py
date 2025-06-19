import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# cria a tabela
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cuidado: fazer delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

#delete mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# criar a tabela
cursor.execute(
    f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
    '''
)
connection.commit()

# registrar valores nas colunas da tabela
# cuidado: sql injection
sql = (
    F'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)
# cursor.execute(sql, ['Robson', 5])
# cursor.executemany(
#     sql, 
#     (
#         ('Robson', 5), ('Maria', 10)
#     )
# )
cursor.execute(sql, {'name': 'Robson', 'weight': 5})
cursor.executemany(sql, (
    {'name': 'gustavo', 'weight': 1},
    {'name': 'maria', 'weight': 2},
    {'name': 'miguel', 'weight': 3},
    {'name': 'augusto', 'weight': 4},
))
connection.commit()


if __name__== '__main__':
    print(sql)
    
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QQR", weight=67.89 '
        'WHERE id = 1'
    )
    connection.commit()
    
    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)
        
    cursor.close()
    connection.close()