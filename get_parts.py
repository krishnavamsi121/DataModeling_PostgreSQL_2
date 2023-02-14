import psycopg2
from config import config

    # Function call
    # """
    # CREATE OR REPLACE FUNCTION get_parts_by_vendor(id integer)
    #     RETURNS TABLE(part_id INTEGER, part_name VARCHAR) AS
    # $$
    # BEGIN
    #     RETURN QUERY
    #
    #     SELECT parts.part_id, parts.part_name
    #     from parts
    #     inner join vendor_parts on vendor_parts.part_id=parts.part_id
    #     where vendor_id=id;
    #
    # END;$$
    #
    # LANGUAGE plpgsql;
    # """


def get_parts(vendor_id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.callproc('get_parts_by_vendor',(vendor_id,))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except(Exception,psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_parts(1)
