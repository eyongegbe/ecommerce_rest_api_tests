import pytest
import logging as logger
from src.utilities.random_generators import generate_email_and_password


def test_create_customer_only():
    logger.info('basic test')
    rand_info = generate_email_and_password()
    logger.info(rand_info)
