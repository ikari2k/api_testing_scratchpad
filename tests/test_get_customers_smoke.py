import pytest
from utils.requests_utils import RequestUtility
import logging as logger


@pytest.mark.tcid30
def test_get_all_customers():
    request_helper = RequestUtility()
    rs_api = request_helper.get("customers").json()
    logger.debug(f"TEST: Response of list all: {rs_api}")
    assert rs_api, f"Response to get customers all is empty"
