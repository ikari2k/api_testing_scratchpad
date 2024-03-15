import json
import os.path

from db_connectors.orders_dao import OrdersDAO
from utils.woo_api_utils import WooAPIUtility


class OrdersHelper:
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args=None):
        payload_template = os.path.join(
            self.cur_file_dir, "..", "data", "create_order_payload.json"
        )
        with open(payload_template) as file:
            payload = json.load(file)

        if additional_args:
            assert isinstance(additional_args, dict), f"Param mus be dict"
            payload.update(additional_args)

        rs_api = self.woo_helper.post("orders", data=payload, expected_status_code=201)
        return rs_api

    def verify_order_is_created(self, order_json, expected_customer_id, exp_products):
        order_dao = OrdersDAO()
        assert order_json, f"Create order response is empty"
        assert (
            order_json["customer_id"] == expected_customer_id
        ), f"Customer ID mismatch"
        assert len(order_json["line_items"]) == len(
            exp_products
        ), f"Expected only {len(exp_products)} order"

        line_info = order_dao.get_order_lines_by_order_id(order_json["id"])
        assert line_info, f"Create order, line item not found in DB"
        line_items = [i for i in line_info if i["order_item_type"] == "line_item"]
        assert len(line_items) == 1, f"Expected 1 line item"

        api_product_ids = [i["product_id"] for i in order_json["line_items"]]
        for product in exp_products:
            assert (
                product["product_id"] in api_product_ids
            ), "Create order does not have at least 1 expected product in DB"
