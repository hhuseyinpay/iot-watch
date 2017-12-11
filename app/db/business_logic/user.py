from app.db.queries.user import UserQueries


class UserBusinessLogic:
    @staticmethod
    def select():
        return UserQueries.select()

    @staticmethod
    def create(user):
        if 16 > len(user.username) > 5:
            UserQueries.insert(user)
            return None
        else:
            return "user name length must be between 5 and 16"

    @staticmethod
    def get_user(ssn):
        return UserQueries.get_user(ssn)
