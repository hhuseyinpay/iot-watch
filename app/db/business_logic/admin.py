from werkzeug.security import generate_password_hash

from app.db.queries.admin import AdminQueries
from app.db.models.admin import AdminModel


class AdminBusinessLogic:
    @staticmethod
    def create(ssn, firstname, lastname, username, password, description):
        if 16 > len(username) > 5:
            admin = AdminModel(ssn, firstname, lastname, username,
                               generate_password_hash(password, method='sha256'), description)

            AdminQueries.insert(admin)
            return None
        else:
            return "user name length must be between 5 and 16"

    @staticmethod
    def get_user(ssn):
        return AdminQueries.get_admin(ssn)
