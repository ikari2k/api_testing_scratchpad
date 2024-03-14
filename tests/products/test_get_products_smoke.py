import pytest
from utils.requests_utils import RequestUtility
from db_connectors.products_dao import ProductDAO
import logging as logger

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    request_helper = RequestUtility()
    rs_api = request_helper.get("products").json()
    logger.debug(f"TEST: Response of list all: {rs_api}")
    assert rs_api, f"Response to get customers all is empty"


@pytest.mark.tcid25
def test_get_product_by_id():
    prod_dao = ProductDAO()
    rand_prod_from_db = prod_dao.get_random_product_from_db()[0]
    logger.debug(rand_prod_from_db)
    rand_product_id_from_db = rand_prod_from_db["ID"]
    request_helper = RequestUtility()
    rs_api = request_helper.get(f"products/{rand_product_id_from_db}").json()
    logger.debug(rs_api)
    assert (
        rand_prod_from_db["post_title"] == rs_api["name"]
    ), f"Name of the products are mismatched between API call and DB"
