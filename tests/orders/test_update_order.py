import pytest
import logging as logger

from helpers.orders_helper import OrdersHelper


@pytest.mark.parametrize(
    "new_status",
    [
        pytest.param("cancelled", marks=pytest.mark.tcid55),
        pytest.param("completed", marks=pytest.mark.tcid56),
        pytest.param("on-hold", marks=pytest.mark.tcid57),
    ],
)
def test_update_order_status(new_status):
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    cur_status = order_json["status"]
    logger.debug(f"CUR STATUS: {cur_status}")

    assert cur_status != new_status, f"Current status is the one we want to update to"

    order_id = order_json["id"]
    payload = {"status": new_status}
    order_helper.update_order(order_id, payload)
    order_api = order_helper.get_order_by_id(order_id)
    assert order_api["status"] == new_status, f"Status was not updated"
