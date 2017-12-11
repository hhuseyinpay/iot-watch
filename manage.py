#!/usr/bin/env python

from flask_script import Manager

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
            ssn INTEGER PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            user_name VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL, 
            description VARCHAR(255) NOT NULL)""")

        # admin
        cur.execute("""
        CREATE TABLE admins (
        SSN INT NOT NULL,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        user_name VARCHAR(40) NOT NULL,
        password VARCHAR(40) NOT NULL,
        description VARCHAR(100),
        PRIMARY KEY(SSN)
        )""")

        # location
        cur.execute("""
        CREATE TABLE location (
        id INT NOT NULL,
        name VARCHAR(40) NOT NULL,
        description VARCHAR(100),
        PRIMARY KEY(id)
        )""")

        # measurement_type
        cur.execute("""
        CREATE TABLE measurement_type (
        id INT NOT NULL,
        name VARCHAR(40) NOT NULL,
        description VARCHAR(100),
        PRIMARY KEY(id)
        )""")

        # device_type
        cur.execute("""
        CREATE TABLE device_type (
        id INT NOT NULL,
        name VARCHAR(40) NOT NULL,
        description VARCHAR(100),
        PRIMARY KEY(id)
        )""")

        # reporting_device
        cur.execute("""
        CREATE TABLE reporting_device (
        id INT NOT NULL,
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
        id INT NOT NULL,
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
    from app.db.models.user import UserModel
    from app.db.business_logic.user import UserBusinessLogic

    user = UserModel()

    user.ssn = "1111"
    user.username = "test_username"
    user.password = "test_password"
    user.firstname = "test_firstname"
    user.lastname = "test_lasname"
    user.description = "test_description"

    UserBusinessLogic.create(user)

    # rows = FUsers.select()
    """
    for row in rows:
        print("SSN = ", row[0])
        print("FIRST NAME = ", row[1])
        print("LAST NAME = ", row[2])
        print("USER NAME = ", row[3])
        print("PASSWORD = ", row[4])
        print("DESCRIPTON = ", row[5], "\n")
    """


@manager.command
def test():
    from app.db.queries.user import UserQueries
    from app.db.models.user import UserModel

    # print(UserQueries.get_user(1111).firstname)

    UserQueries.insert(
        UserModel(12345, "deneme first", "last deneme", "biraz uzun lazım", "123412344", "açıklama yok birader"))


if __name__ == '__main__':
    manager.run()
