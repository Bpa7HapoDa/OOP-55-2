import sqlite3

connect = sqlite3.connect('movies.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    genre TEXT,
    year INTEGER,
    rating REAL
)
''')
connect.commit()

def add_movie(title, genre, year, rating):
    cursor.execute(
        'INSERT INTO movies(title, genre, year, rating) VALUES (?, ?, ?, ?)',
        (title, genre, year, rating)
    )
    connect.commit()
    print(f'Фильм "{title}" добавлен.')

def get_all_movies():
    cursor.execute('SELECT rowid, * FROM movies')
    movies = cursor.fetchall()
    print('Список фильмов:')
    for movie in movies:
        print(movie)

def update_movie(rowid, field, new_value):
    if field not in ['title', 'genre', 'year', 'rating']:
        print('Ошибка: Неверное имя поля.')
        return
    cursor.execute(f'UPDATE movies SET {field} = ? WHERE rowid = ?', (new_value, rowid))
    connect.commit()
    print(f' Фильм с rowid={rowid} обновлён: поле "{field}" → {new_value}')

def delete_movie(rowid):
    cursor.execute('DELETE FROM movies WHERE rowid = ?', (rowid,))
    connect.commit()
    print(f' Фильм с rowid={rowid} удалён.')

# add_movie('D&D', 'Fantastic', 2024, 8.8)
# get_all_movies()
update_movie(1, 'rating', 9.0)
# delete_movie(1)
