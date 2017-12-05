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

        cur.execute(
            "CREATE TABLE users (ssn INTEGER PRIMARY KEY,first_name VARCHAR(255) NOT NULL,last_name VARCHAR(255) NOT NULL,user_name VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL)")

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
    from app.db.queries.user import UserQueries

    user = UserModel()

    user.ssn = "1111234"
    user.username = "test_username"
    user.password = "test_password"
    user.firstname = "test_firstname"
    user.lastname = "test_lasname"
    user.description = "test_description"

    UserQueries.insert(user)

    #rows = FUsers.select()
    """
    for row in rows:
        print("SSN = ", row[0])
        print("FIRST NAME = ", row[1])
        print("LAST NAME = ", row[2])
        print("USER NAME = ", row[3])
        print("PASSWORD = ", row[4])
        print("DESCRIPTON = ", row[5], "\n")
    """

if __name__ == '__main__':
    manager.run()
