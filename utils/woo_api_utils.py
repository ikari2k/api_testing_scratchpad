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
        rs = self.woocommerce_api.get(
            wc_endpoint,
            params=param,
        )
        assert (
            rs.status_code == expected_status_code
        ), f"Expected status code {expected_status_code} differs from actual one {rs.status_code}"

        return rs.json()


if __name__ == "__main__":
    woo = WooAPIUtility()
    rs = woo.get("products")
    print(rs)
