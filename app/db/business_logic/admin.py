from app.db.queries.admin import AdminQueries


class AdminBusinessLogic:
    @staticmethod
    def select():
        return AdminQueries.select()

    @staticmethod
    def create(admin):
        if 16 > len(admin.username) > 5:
            AdminQueries.insert(admin)
            return None
        else:
            return "user name length must be between 5 and 16"

    @staticmethod
    def get_user(ssn):
        return AdminQueries.get_admin(ssn)
