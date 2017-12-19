from app.db import conn
from ..models.device_type import DeviceTypeModel
import psycopg2


class DeviceTypeQueries:
    @staticmethod
    def get(id):
        cur = conn.cursor()
        try:
            cur.callproc('public.device_type_get', [id])
        except psycopg2.Error as e:
            print(e)
        row = cur.fetchall()
        cur.close()

        if row:
            return DeviceTypeModel(row[0], row[1], row[2])
        else:
            return None

    @staticmethod
    def get_all():
        cur = conn.cursor()
        try:
            cur.callproc('public.device_type_get_all')
        except psycopg2.Error as e:
            print(e)
        rows = cur.fetchall()
        cur.close()

        if rows:
            ret = []
            for row in rows:
                ret.append(DeviceTypeModel(row[1], row[2], row[0]))
            return ret
        else:
            return None

    @staticmethod
    def insert(devicetype):
        cur = conn.cursor()
        try:
            cur.callproc('public.device_type_insert', [devicetype.name, devicetype.description])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
