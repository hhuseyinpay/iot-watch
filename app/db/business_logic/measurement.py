from app.db.models.measurement import MeasurementModel
from app.db.queries.measurement import MeasurementQueries
from datetime import datetime


class MeasurementBusinessLogic:
    @staticmethod
    def get(id):
        return MeasurementQueries.get(id)

    @staticmethod
    def get_all():
        return MeasurementQueries.get_all()

    @staticmethod
    def get_data_by_device(device_id):
        return MeasurementQueries.get_data_by_device(device_id)

    @staticmethod
    def get_last_measured_ipaddress():
        return MeasurementQueries.get_last_measured_ipaddress()

    @staticmethod
    def create(measurement_type_id, reporting_device_id, location_id, measured_value):
        measure = MeasurementModel(0, measurement_type_id, reporting_device_id, location_id, measured_value,
                                   datetime.now())
        MeasurementQueries.insert(measure)
