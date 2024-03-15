import os

from woocommerce import API

from config.configurations import WOO_API_HOSTS
from utils.credentials_utils import CredentialsUtilities


class WooAPIUtility:
    def __init__(self) -> None:
        self.wc_key, self.wc_secret = (
            CredentialsUtilities.get_woo_commerce_credentials()
        )
        self.env = os.environ.get("ENV", "test_env")
        self.base_url = WOO_API_HOSTS[self.env]
        self.woocommerce_api = API(
            url=self.base_url,
            consumer_key=self.wc_key,
            consumer_secret=self.wc_secret,
            version="wc/v3",
        )

    def get(self, wc_endpoint, param=None, expected_status_code=200):
        rs_api = self.woocommerce_api.get(
            wc_endpoint,
            params=param,
        )
        assert (
            rs_api.status_code == expected_status_code
        ), f"Expected status code {expected_status_code} differs from actual one {rs.status_code}"

        return rs_api.json()

    def post(self, wc_endpoint, data=None, expected_status_code=200):
        rs_api = self.woocommerce_api.post(
            wc_endpoint,
            data=data,
        )
        assert (
            rs_api.status_code == expected_status_code
        ), f"Expected status code {expected_status_code} differs from actual one {rs.status_code}"

        return rs_api.json()

    def put(self, wc_endpoint, params, expected_status_code=200):
        rs_api = self.woocommerce_api.put(
            wc_endpoint,
            data=params,
        )
        assert (
            rs_api.status_code == expected_status_code
        ), f"Expected status code {expected_status_code} differs from actual one {rs.status_code}"

        return rs_api.json()


if __name__ == "__main__":
    woo = WooAPIUtility()
    rs = woo.get("products")
    print(rs)
