import pytest
from datetime import datetime, timedelta
from helpers.product_helpers import ProductHelper
import logging as logger
from db_connectors.products_dao import ProductDAO


@pytest.mark.regression
class TestListProductsWithFilter:
    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        x_days_from_today = 30
        after_given_date = (
            datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        ).isoformat()

        payload = dict()
        payload["after"] = after_given_date

        logger.info(payload)
        prod_helper = ProductHelper()
        rs_api = prod_helper.list_products(payload)
        logger.info(payload)
        logger.debug(rs_api)

        assert rs_api, f"Empty response for list of products with filter"
        product_dao = ProductDAO()
        db_products = product_dao.get_product_created_after_given_date(after_given_date)

        assert len(db_products) == len(
            rs_api
        ), f"Number of products returned by API and from DB query is not the same. API: {len(rs_api )}, DB: {len(db_products)}"

        ids_in_api = [i["id"] for i in rs_api]
        ids_in_db = [i["ID"] for i in db_products]

        assert set(ids_in_db) == set(ids_in_api), f"List of IDs are not equal"
