import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="conveniencestore",
        port = "3306"
    )


def execute_query(sql):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def select_query(sql):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_id(table, prefix, id_column):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT {id_column} FROM {table} ORDER BY {id_column} DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    if result:
        last_id = result[0]
        number = int(last_id[1:]) + 1
    else:
        number = 1

    return f"{prefix}{number:05d}"
