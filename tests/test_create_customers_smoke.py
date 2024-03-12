import pytest
import logging as logger
from helpers.customer_helpers import CustomerHelper

from utils.generic_utils import generate_random_email_and_password
from utils.requests_utils import RequestUtility


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")
    email, password = generate_random_email_and_password()
    logger.debug(f"TEST: Email and Password generated: {email}, {password}")

    # create payload
    ch = CustomerHelper()
    payload = ch.create_customer_payload(email, password)
    logger.debug(f"TEST: Payload for testing: {payload}")
    # make the call
    ru = RequestUtility()
    response = ru.post("customers", payload, expected_status_code=201)
    logger.info(f"TEST: Response for testing: {response}")
    # verify status code

    # verify email in the response

    # verify customer is created in database
