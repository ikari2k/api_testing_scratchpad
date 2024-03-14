from typing import List

from utils.requests_utils import RequestUtility
from utils.generic_utils import generate_random_string
import logging as logger


class ProductHelper:
    def __init__(self) -> None:
        self.request_utility = RequestUtility()

    @staticmethod
    def create_product_payload(
        name: str = None, type: str = "simple", regular_price: float = 10.99
    ) -> dict:
        if not name:
            name = generate_random_string()

        payload = {"name": name, "type": type, "regular_price": regular_price}
        return payload

    def list_products(self, payload: dict = None) -> List[str]:
        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number: {i}")

            if not payload:
                payload = {}

            if not "per_page" in payload.keys():
                payload["per_page"] = 100

            # add the current page number to the call
            payload["page"] = i
            rs_api = self.request_utility.get("products", payload).json()

            # if there is not response then stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)

        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")
        logger.info(f"All Products: {len(all_products)}")
        return all_products
