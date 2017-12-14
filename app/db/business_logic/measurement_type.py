from app.db.models.measurement_type import MeasurementTypeModel
from app.db.queries.measurement_type import MeasurementTypeQueries


class MeasurementTypeBusinessLogic:
    @staticmethod
    def get(id):
        return MeasurementTypeQueries.get(id)

    @staticmethod
    def create(name="", description=""):
        if 30 > len(name) > 3:
            measurementtype = MeasurementTypeModel(name, description)
            MeasurementTypeQueries.insert(measurementtype)
            return None
        else:
            return "Name length must be between 3 and 16"
