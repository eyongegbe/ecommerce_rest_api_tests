from src.utilities.random_generators import generate_email_and_password


class CustomerHelper(object):

    def __init__(self):
        pass

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            email_passsword = generate_email_and_password()
            email = email_passsword['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
