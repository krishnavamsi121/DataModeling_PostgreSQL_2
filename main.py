import psycopg2
from config import config
from create_tables import create_tables

def connect():
    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('Select version()')

        db_version = cur.fetchone()
        print(db_version)

        conn.close()

    except (Exception,psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

if __name__ == "__main__":
    connect()
    create_tables()
