from app.db import conn
from ..models.location import LocationModel
import psycopg2


class LocationQueries:
    @staticmethod
    def get(id):
        cur = conn.cursor()

        # cur.execute("SELECT * FROM users WHERE ssn='%s'" % ssn)
        try:
            cur.callproc('public.location_get', [id])
        except psycopg2.Error as e:
            print(e)
        row = cur.fetchall()
        cur.close()

        if row:
            return LocationModel(row[0], row[1], row[2])
        else:
            return None

    @staticmethod
    def get_all():
        cur = conn.cursor()
        try:
            cur.callproc('public.location_get_all')
        except psycopg2.Error as e:
            print(e)
        rows = cur.fetchall()
        cur.close()

        if rows:
            ret = []
            for row in rows:
                ret.append(LocationModel(row[1], row[2], row[0]))
            return ret
        else:
            return None

    @staticmethod
    def insert(location):
        cur = conn.cursor()
        try:
            cur.callproc('public.location_insert', [location.name, location.description])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
