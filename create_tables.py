import psycopg2
from config import config


def create_tables():
    create_table_queries = ("""
    CREATE TABLE PARTS(
    part_id serial primary key,
    part_name varchar(255) not null
    )
    """,
    """
    CREATE TABLE VENDORS(
    vendor_id serial Primary key,
    vendor_name varchar(255) not null
    )
    """,
    """
    CREATE TABLE VENDOR_PARTS(
    vendor_id INTEGER NOT NULL,
    part_id integer not null,
    PRIMARY KEY (vendor_id,part_id),
    FOREIGN KEY (vendor_id)
        REFERENCES vendors (vendor_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (part_id)
        REFERENCES parts (part_id)
        ON UPDATE CASCADE ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE PART_DRAWINGS(
    part_id INTEGER NOT NULL,
    file_extension varchar(5) NOT NULL,
    drawing_data BYTES NOT NULL,
    FOREIGN KEY (part_id)
        REFERENCES parts (part_id)
        ON UPDATE CASCADE ON DELETE CASCADE
    )
    """
    )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for query in create_table_queries:
            cur.execute(query)

        cur.close()
        conn.commit()
    except (Exception,psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
