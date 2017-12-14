from app.db.models.user import UserModel
from app.db.queries.user import UserQueries
from werkzeug.security import generate_password_hash


class UserBusinessLogic:
    @staticmethod
    def create(ssn=0, firstname="", lastname="", username="", password="", description=""):
        if 16 > len(username) > 5:
            user = UserModel(ssn, firstname, lastname, username,
                             generate_password_hash(password, method='sha256'), description)

            UserQueries.insert(user)
            return None
        else:
            return "user name length must be between 5 and 16"

    @staticmethod
    def get_user(ssn):
        return UserQueries.get_user(ssn)
