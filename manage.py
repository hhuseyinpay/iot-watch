#!/usr/bin/env python

from flask_script import Manager
from werkzeug.security import generate_password_hash

from app import create_app
import psycopg2

app = create_app()

manager = Manager(app)


@manager.command
def createdb():
    """Creates the db tables."""
    from app.db import conn
    try:
        cur = conn.cursor()

        # user
        cur.execute("""
                CREATE TABLE users (
                ssn BIGINT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                user_name VARCHAR(255) NOT NULL, 
                password VARCHAR(255) NOT NULL, 
                description VARCHAR(255) NOT NULL)""")

        # admin
        cur.execute("""
                CREATE TABLE admins (
                SSN BIGINT NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                user_name VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                PRIMARY KEY(SSN)
                )""")

        # location
        cur.execute("""
                CREATE TABLE location (
                id SERIAL NOT NULL,
                name VARCHAR(40) NOT NULL,
                description VARCHAR(100),
                PRIMARY KEY(id)
                )""")

        # measurement_type
        cur.execute("""
                    CREATE TABLE measurement_type (
                    id SERIAL NOT NULL,
                    name VARCHAR(40) NOT NULL,
                    description VARCHAR(100),
                    PRIMARY KEY(id)
                    )""")

        # device_type
        cur.execute("""
                CREATE TABLE device_type (
                id SERIAL NOT NULL,
                name VARCHAR(40) NOT NULL,
                description VARCHAR(100),
                PRIMARY KEY(id)
                )""")

        # reporting_device
        cur.execute("""
                CREATE TABLE reporting_device (
                id SERIAL NOT NULL,
                name VARCHAR(40) NOT NULL,
                description VARCHAR(100),
                lastIpaddress VARCHAR(50),
                device_type_id INT NOT NULL,
                location_id INT NOT NULL,
                PRIMARY KEY(id),
                FOREIGN KEY(device_type_id) REFERENCES device_type(id),
                FOREIGN KEY(location_id) REFERENCES location(id)
                )""")

        # measurrment
        cur.execute("""
                CREATE TABLE measurement (
                id SERIAL NOT NULL,
                measurement_type_id INT NOT NULL,
                reporting_device_id INT NOT NULL,
                location_id INT NOT NULL,
                measured_value FLOAT,
                measured_date TIMESTAMP,
                PRIMARY KEY(id),
                FOREIGN KEY(measurement_type_id) REFERENCES measurement_type(id),
                FOREIGN KEY(reporting_device_id) REFERENCES reporting_device(id),
                FOREIGN KEY(location_id) REFERENCES location(id)
                )""")

        # location
        cur.execute("""
                CREATE TABLE user_create_log (
                id SERIAL NOT NULL ,
                ssn BIGINT,
                date TIMESTAMP NOT NULL,
                PRIMARY KEY(id)
                )""")

        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


@manager.command
def dropdb():
    """Drops the db tables."""
    pass


@manager.command
def fakedata():
    from app.db.business_logic.user import UserBusinessLogic
    from app.db.business_logic.admin import AdminBusinessLogic
    from app.db.business_logic.device_type import DeviceTypeBusinessLogic
    from app.db.business_logic.location import LocationBusinessLogic
    from app.db.business_logic.reporting_device import ReportingDeviceBusinessLogic
    from app.db.business_logic.measurement_type import MeasurementTypeBusinessLogic
    from app.db.business_logic.measurement import MeasurementBusinessLogic
    # UserBusinessLogic.create("123456789", "test_firstname", "test_lsatname", "test_username", "password","test_description")

    # AdminBusinessLogic.create("123456789", "test_firstname", "test_lsatname", "test_username", "password","test_description")

    DeviceTypeBusinessLogic.create("_test_device_type", "no description")
    DeviceTypeBusinessLogic.create("_test_device_type2", "no description")
    LocationBusinessLogic.create("_test_location", "no description")
    LocationBusinessLogic.create("_test_location2", "no description")

    ReportingDeviceBusinessLogic.create("_test_report_device", "sıcaklık vs işte ya", "192.168.1.2", 1, 1)

    ReportingDeviceBusinessLogic.create("_test_report_device2", "sıcaklık vs işte ya", "192.168.1.2", 1, 1)

    ReportingDeviceBusinessLogic.create("_test_report_device3", "sıcaklık vs işte ya", "192.168.1.2", 1, 1)

    MeasurementTypeBusinessLogic.create("test_measurementType_name", "no description")
    MeasurementTypeBusinessLogic.create("test_measurementType_name2", "no description")

    # MeasurementBusinessLogic.create(1, 1, 1, 50.5)
    # MeasurementBusinessLogic.create(1, 1, 1, 25)
    # MeasurementBusinessLogic.create(2, 2, 2, 35.5)
    # MeasurementBusinessLogic.create(1, 2, 1, 20.5)
    # MeasurementBusinessLogic.create(1, 1, 2, 98)
    # MeasurementBusinessLogic.create(2, 1, 2, 18)
    MeasurementBusinessLogic.create(1, 1, 1, 25)


@manager.command
def test():
    from app.db.queries.user import UserQueries
    from app.db.models.user import UserModel
    from app.db.business_logic.user import UserBusinessLogic
    from app.db.business_logic.admin import AdminBusinessLogic
    from app.db.business_logic.reporting_device import ReportingDeviceBusinessLogic
    # print(UserQueries.get_user(1111).firstname)

    # UserQueries.insert(UserModel(12345, "deneme first", "last deneme", "biraz uzun lazım", "123412344", "açıklama yok birader"))

    print(UserBusinessLogic.get_user(123456789).firstname)
    print(AdminBusinessLogic.get_user(123456789).firstname)
    rows = ReportingDeviceBusinessLogic.get_all()
    # print(rows)
    # for row in rows:
    #    print(str(row.id) + " - " + row.name + " - " + row.description + " - " + row.lastipaddress + " - " + str(
    #       row.device_type_id) + " - " + str(row.location_id))


if __name__ == '__main__':
    manager.run()
