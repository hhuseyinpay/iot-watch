from app.db.models.location import LocationModel
from app.db.queries.location import LocationQueries


class LocationBusinessLogic:
    @staticmethod
    def get(id):
        return LocationQueries.get(id)

    @staticmethod
    def get_all() -> object:
        return LocationQueries.get_all()

    @staticmethod
    def create(name="", description=""):
        if 30 > len(name) > 3:
            location = LocationModel(name, description)
            LocationQueries.insert(location)
            return None
        else:
            return "Name length must be between 3 and 16"

    @staticmethod
    def update(id_, name, description):
        return LocationQueries.update(id_, name, description)

    @staticmethod
    def delete(id_):
        return LocationQueries.delete(id_)
