from app.db.models.device_type import DeviceTypeModel
from app.db.queries.device_type import DeviceTypeQueries


class DeviceTypeBusinessLogic:
    @staticmethod
    def get(id):
        return DeviceTypeQueries.get(id)

    @staticmethod
    def get_all():
        return DeviceTypeQueries.get_all()

    @staticmethod
    def create(name="", description=""):
        if 30 > len(name) > 3:
            devicetype = DeviceTypeModel(name, description)
            DeviceTypeQueries.insert(devicetype)
            return None
        else:
            return "Name length must be between 3 and 16"
