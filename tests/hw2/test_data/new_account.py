from srv.pages.account.data.account_data import RegistrationData, LoginData
from srv.random_values import random_string, random_email, random_phone

CORRECT_REGISTRATION_DATA = RegistrationData(
    firstname=random_string(),
    lastname=random_string(10),
    email=random_email(),
    phone=random_phone(),
    password='test',
    password_confirm='test'
)

LOGIN_DATA = LoginData(
        email=CORRECT_REGISTRATION_DATA.email,
        password=CORRECT_REGISTRATION_DATA.password
)
