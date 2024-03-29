import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connect():
    try:
        conn = psycopg2.connect(host="localhost", database="hw03", user="postgres", password="12345")
        try:
            yield conn
        finally:
            conn.close()
    except psycopg2.OperationalError:
        print("Connection failed")
