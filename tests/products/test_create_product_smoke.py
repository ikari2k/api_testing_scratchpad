import pytest
from helpers.product_helpers import ProductHelper
from utils.requests_utils import RequestUtility
from db_connectors.products_dao import ProductDAO


@pytest.mark.tcid26
@pytest.mark.products
def test_create_simple_product():
    product_payload = ProductHelper.create_product_payload()
    reqs_utils = RequestUtility()
    product_response = reqs_utils.post(
        "products", product_payload, expected_status_code=201
    ).json()
    assert product_response, f"Create product API response successful"
    assert (
        product_response["name"] == product_payload["name"]
    ), f"Name of the product matches"
    prod_dao = ProductDAO()
    db_product = prod_dao.get_product_by_id(product_response["id"])[0]
    assert (
        product_response["name"] == db_product["post_title"]
    ), "Name of the product matches between API call and DB"
