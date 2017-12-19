from app.db import conn
from ..models.reporting_device import ReportingDeviceModel
import psycopg2


class ReportingDeviceQueries:
    @staticmethod
    def get_all():
        cur = conn.cursor()

        # cur.execute("SELECT * FROM users WHERE ssn='%s'" % ssn)
        try:
            cur.callproc('public.reporting_device_get_all')
        except psycopg2.Error as e:
            print(e)
        rows = cur.fetchall()
        cur.close()

        if rows:
            ret = []
            for row in rows:
                ret.append(ReportingDeviceModel(row[0], row[1], row[2], row[3], row[4], row[5]))
            return ret
        else:
            return None

    @staticmethod
    def get_by_location(location_id):
        cur = conn.cursor()

        # cur.execute("SELECT * FROM users WHERE ssn='%s'" % ssn)
        try:
            cur.callproc('public.reporting_device_get_by_location', [location_id])
        except psycopg2.Error as e:
            print(e)
        rows = cur.fetchall()
        cur.close()

        if rows:
            ret = []
            for row in rows:
                print(row[0])
                ret.append(ReportingDeviceModel(row[0], row[1], row[2], row[3], row[4], row[5]))
            return ret
        else:
            return None

    @staticmethod
    def insert(device):
        cur = conn.cursor()

        try:
            cur.callproc('public.reporting_device_insert',
                         [device.name, device.description, device.lastipaddress, device.device_type_id,
                          device.location_id])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
