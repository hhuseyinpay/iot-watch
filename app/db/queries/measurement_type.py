from app.db import conn
from ..models.measurement_type import MeasurementTypeModel
import psycopg2


class MeasurementTypeQueries:
    @staticmethod
    def get(id):
        cur = conn.cursor()
        try:
            cur.callproc('public.measurement_type_get', [id])
        except psycopg2.Error as e:
            print(e)
        row = cur.fetchall()
        cur.close()

        if row:
            return MeasurementTypeModel(row[0], row[1], row[2])
        else:
            return None

    @staticmethod
    def get_all():
        cur = conn.cursor()
        try:
            cur.callproc('public.measurement_type_get_all')
        except psycopg2.Error as e:
            print(e)
        rows = cur.fetchall()
        cur.close()

        if rows:
            ret = []
            for row in rows:
                ret.append(MeasurementTypeModel(row[1], row[2], row[0]))
            return ret
        else:
            return None

    @staticmethod
    def insert(measurementtype):
        cur = conn.cursor()
        try:
            cur.callproc('public.measurement_type_insert', [measurementtype.name, measurementtype.description])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
