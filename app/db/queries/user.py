from app.db import conn
from ..models.user import UserModel
import psycopg2


class UserQueries:
    @staticmethod
    def select():
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        cur.close()

        return rows

    @staticmethod
    def insert(user):
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO USERS (ssn, first_name, last_name, user_name, password, description) \
                  VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %
                (user.ssn, user.firstname, user.lastname, user.username, user.password, user.description))
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()

    @staticmethod
    def get_user(ssn):
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE ssn='%s'" % ssn)
        row = cur.fetchone()
        cur.close()

        if row:
            return UserModel(row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            return None
