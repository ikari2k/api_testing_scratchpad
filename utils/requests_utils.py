import requests
import os
from requests_oauthlib import OAuth1
from utils.credentials_utils import CredentialsUtilities

from config.configurations import API_HOSTS


class RequestUtility:
    def __init__(self) -> None:
        self.wc_key, self.wc_secret = (
            CredentialsUtilities.get_woo_commerce_credentials()
        )
        self.env = os.environ.get("ENV", "test_env")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(self.wc_key, self.wc_secret)

    def post(
        self,
        endpoint: str | None = None,
        payload: dict | None = None,
        headers: dict | None = None,
        expected_status_code: int = 200,
    ) -> requests.Response:
        url = "".join(filter(None, [self.base_url, endpoint]))
        if not headers or headers == "":
            headers = {"Content-Type": "application/json"}
        rs_api = requests.post(url, payload, headers, auth=self.auth)
        status_code = rs_api.status_code
        assert (
            status_code == expected_status_code
        ), f"Expected status code {expected_status_code}, but was {status_code}"

        return rs_api

    def get(
        self,
        endpoint: str | None = None,
        headers: dict | None = None,
        expected_status_code: int = 200,
    ):
        url = "".join(filter(None, [self.base_url, endpoint]))
        if not headers or headers == "":
            headers = {"Content-Type": "application/json"}
        rs_api = requests.get(url, headers, auth=self.auth)
        status_code = rs_api.status_code
        assert (
            status_code == expected_status_code
        ), f"Expected status code {expected_status_code}, but was {status_code}"

        return rs_api


if __name__ == "__main__":
    ru = RequestUtility()
    data = {"email": "testuser_cuolhji1ybg@test.com", "password": "Password1"}
    print(ru.post(endpoint="customers", payload=data, expected_status_code=201))
