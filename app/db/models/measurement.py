from time import time


class MeasurementModel:
    def __init__(self, id=0, measurement_type_id=0, reporting_device_id=0, location_id=0, measured_value=0.0,
                 measured_date=time()):
        self.id = id
        self.measurement_type_id = measurement_type_id
        self.reporting_device_id = reporting_device_id
        self.location_id = location_id
        self.measured_value = measured_value
        self.measured_date = measured_date
