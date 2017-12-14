from app.db import conn
from ..models.measurement import MeasurementModel
import psycopg2


class MeasurementQueries:
    @staticmethod
    def get(id):
        cur = conn.cursor()
        try:
            cur.callproc('public.measurement_get', [id])
        except psycopg2.Error as e:
            print(e)
        row = cur.fetchall()
        cur.close()

        if row:
            return MeasurementModel(row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            return None

    @staticmethod
    def insert(measurement):
        cur = conn.cursor()
        try:
            cur.callproc('public.measurement_insert', [measurement.measurement_type_id,
                                                       measurement.reporting_device_id,
                                                       measurement.location_id,
                                                       measurement.measured_value,
                                                       measurement.measured_date])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
