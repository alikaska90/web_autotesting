class RegistrationData:
    def __init__(self,
                 firstname: str = None,
                 lastname: str = None,
                 email: str = None,
                 phone: str = None,
                 password: str = None,
                 password_confirm: str = None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.password = password
        self.password_confirm = password_confirm


class LoginData:
    def __init__(self,
                 email: str = None,
                 password: str = None):
        self.email = email
        self.password = password
