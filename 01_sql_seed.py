import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connect

fake = Faker("en_US")
COUNT = 200
STATUSES = [('new',), ('in progress',), ('completed',)]
USERS = 10

def insert_data(conn):
    c = conn.cursor()
    try:
        for _ in range(USERS):
            fullname = fake.name()
            email = fake.email()
            c.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        
        
        for i in range(len(STATUSES)):
            c.execute('INSERT INTO status (name) values (%s)', STATUSES[i]) 
        
        for _ in range(COUNT):
            title = fake.word()
            description = fake.sentence()
            status_id = randint(1, len(STATUSES))
            user_id = randint(1, USERS)
            c.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    # sql_stmt = """
    # INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s)
    
    # """

    try:
        with create_connect() as conn:
            insert_data(conn)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
