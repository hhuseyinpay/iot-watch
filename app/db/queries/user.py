from app.db import conn


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

        cur.execute(
            "INSERT INTO USERS (ssn, first_name, last_name, user_name, password, description) VALUES (%s,%s,%s,%s,%s,%s)",
            (user.ssn, user.firstname, user.lastname, user.username, user.password, user.description))

        conn.commit()
        cur.close()
