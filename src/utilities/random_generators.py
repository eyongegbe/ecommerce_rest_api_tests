import logging as logger
import random
import string


def generate_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating a random email and password. ")
    if not domain:
        domain = "testsite.com"
    if not email_prefix:
        email_prefix = "newtestuser"

    random_email_string_length = 15
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password_str = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_str}
    logger.debug(f"generated email and password: {random_info}")

    return random_info
