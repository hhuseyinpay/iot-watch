from app.db.models.reporting_device import ReportingDeviceModel
from app.db.queries.reporting_device import ReportingDeviceQueries


class ReportingDeviceBusinessLogic:
    @staticmethod
    def create(name, description, lastipaddress, device_type_id, location_id):
        if 30 > len(name) > 3:
            if 16 > len(lastipaddress) > 6:
                device = ReportingDeviceModel(0, name, description, lastipaddress,
                                              device_type_id, location_id)
                ReportingDeviceQueries.insert(device)
                return None

            else:
                return "Incorret IP address!"
        else:
            return "Name length must greater than 3 and less than 30!"

    @staticmethod
    def get_all():
        return ReportingDeviceQueries.get_all()
