import pytest
import logging as logger

from db_connectors.products_dao import ProductDAO

from helpers.orders_helper import OrdersHelper
from helpers.customer_helpers import CustomerHelper
from utils.requests_utils import RequestUtility


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductDAO()
    order_helper = OrdersHelper()
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]["ID"]
    customer_id = 0
    info = {"line_items": [{"product_id": product_id, "quantity": 1}]}

    order = order_helper.create_order(additional_args=info)
    logger.debug(f"ORDER:{order}")

    expected_products = [{"product_id": product_id}]
    order_helper.verify_order_is_created(order, customer_id, expected_products)


@pytest.mark.tcid49
def test_create_paid_order_new_create_customer():
    product_dao = ProductDAO()
    order_helper = OrdersHelper()
    cust_helper = CustomerHelper()
    ru = RequestUtility()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]["ID"]
    customer_info_payload = cust_helper.create_customer_payload()

    customer_info = ru.post(
        "customers", customer_info_payload, expected_status_code=201
    ).json()
    customer_id = customer_info["id"]
    info = {
        "line_items": [{"product_id": product_id, "quantity": 1}],
        "customer_id": customer_id,
    }

    order = order_helper.create_order(additional_args=info)
    logger.debug(f"ORDER:{order}")

    expected_products = [{"product_id": product_id}]
    order_helper.verify_order_is_created(order, customer_id, expected_products)
