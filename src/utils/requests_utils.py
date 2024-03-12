import json
import requests
from api_framework.src.configs.hosts_config import API_HOSTS
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv


class RequestUtility:
    def __init__(self) -> None:
        load_dotenv()
        self.env = os.environ.get("ENV", "test_env")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(
            os.environ.get("WOOCOMMERCE_API_KEY"),
            os.environ.get("WOOCOMMERCE_API_SECRET"),
        )

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
        rs_api = requests.post(url, json.dumps(payload), headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert (
            self.status_code == expected_status_code
        ), f"Expected status code {expected_status_code}, but was {self.status_code}"

        return rs_api

    def get(self): ...
