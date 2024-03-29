import pytest
import logging as logger

from db_connectors.customers_dao import CustomersDAO
from helpers.customer_helpers import CustomerHelper

from utils.generic_utils import generate_random_email_and_password
from utils.requests_utils import RequestUtility


@pytest.mark.tcid29
@pytest.mark.customers
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
    response_to_json = ru.post("customers", payload, expected_status_code=201).json()
    logger.info(f"TEST: Response for testing: {response_to_json}")

    # verify email in the response
    assert response_to_json["email"] == email, (
        f"Create customer API returns wrong email address. Expected: {email}, "
        f'got: {response_to_json["email"]}'
    )
    assert response_to_json["first_name"] == "", (
        f"Create customer API returns wrong name which should be empty, "
        f'got: {response_to_json["first_name"]}'
    )
    # verify customer is created in database
    customer_dao = CustomersDAO()
    cust_info = customer_dao.get_customer_by_email(email)
    logger.debug(f"TEST customer infor from DB: {cust_info}")

    id_in_api = response_to_json["id"]
    id_in_db = cust_info[0]["ID"]
    assert (
        id_in_api == id_in_db
    ), f'Create customer response "id" not the same as the one in DB'


@pytest.mark.tcid47
@pytest.mark.customers
def test_create_customer_fail_for_existing_email():
    # get existing email
    cust_dao = CustomersDAO()
    existing_customer = cust_dao.get_random_customer_from_db()
    existing_email = existing_customer[0]["user_email"]

    req_helper = RequestUtility()
    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(
        endpoint="customers", payload=payload, expected_status_code=400
    )
    assert (
        cust_api_info.json()["code"] == "registration-error-email-exists"
    ), f"Create customer with existing email - error code is incorrect"
