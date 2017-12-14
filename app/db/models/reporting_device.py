class ReportingDeviceModel:
    def __init__(self, id: object = 0, name: object = "", description: object = "", lastipaddress: object = "", device_type_id: object = 0, location_id: object = 0) -> object:
        self.id = id
        self.name = name
        self.description = description
        self.lastipaddress = lastipaddress
        self.device_type_id = device_type_id
        self.location_id = location_id
