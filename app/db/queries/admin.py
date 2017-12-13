from app.db import conn
from ..models.admin import AdminModel
import psycopg2


class AdminQueries:

    @staticmethod
    def insert(admin):
        cur = conn.cursor()
        try:
            """
            cur.execute(
                "INSERT INTO USERS (ssn, first_name, last_name, user_name, password, description) \
                  VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %
                (user.ssn, user.firstname, user.lastname, user.username, user.password, user.description))
            """
            cur.callproc('public.insert_admin',
                         [admin.ssn, admin.firstname, admin.lastname, admin.username, admin.password,
                          admin.description])
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()

    @staticmethod
    def get_admin(ssn):
        cur = conn.cursor()

        # cur.execute("SELECT * FROM users WHERE ssn='%s'" % ssn)

        cur.callproc('public.get_admin', [ssn])
        row = cur.fetchone()
        cur.close()

        if row:
            return AdminModel(row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            return None
