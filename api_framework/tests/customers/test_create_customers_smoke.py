import pytest
import logging as logger
from api_framework.src.helpers.customer_helpers import CustomerHelper
from api_framework.src.utils.generic import generate_random_email_and_password
from api_framework.src.utils.requests_utils import RequestUtility


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")
    email, password = generate_random_email_and_password()
    logger.debug(f"TEST: Email and Password generated: {email}, {password}")

    # create payload
    ch = CustomerHelper()
    payload = ch.create_customer(email, password)
    logger.debug(f"TEST: Payload for testing: {payload}")
    # make the call
    ru = RequestUtility()
    response = ru.post("customer", payload)
    logger.debug(f"TEST: Response for testing: {response}")
    # verify status code

    # verify email in the response

    # verify customer is created in database
