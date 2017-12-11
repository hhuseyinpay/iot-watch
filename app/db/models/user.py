class UserModel:
    def __init__(self, ssn: object = 0, firstname: object = "", lastname: object = "", username: object = "",
                 password: object = "", description: object = "") -> object:
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.description = description

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.ssn)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
