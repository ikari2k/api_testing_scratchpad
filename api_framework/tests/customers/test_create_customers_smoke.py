import pytest
import logging as logger
from api_framework.src.utils.generic import generate_random_email_and_password


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")
    email, password = generate_random_email_and_password()
    logger.debug(f"TEST: Email and Password generated: {email}, {password}")

    # create payload
    payload = {"email": email, "password": password}

    # make the call

    # verify status code

    # verify email in the response

    # verify customer is created in database
