import psycopg2

def connection():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='lorelin',
        host='localhost',
        port='5432'
    )
    return conn

def create_table():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(id SERIAL PRIMARY KEY, name VARCHAR, age VARCHAR, phone VARCHAR)''')
    conn.commit()
    return conn, cursor

def save_user(name, age, phone):
    conn, cursor = create_table()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO orders(name, age, phone) VALUES (%s, %s, %s)''', [name, age, phone])
    conn.commit()
    conn.close()
