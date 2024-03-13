import os
from typing import Tuple

from dotenv import load_dotenv


class CredentialsUtilities:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_woo_commerce_credentials() -> Tuple[str, str]:
        load_dotenv()

        wc_key = os.environ.get("WOOCOMMERCE_API_KEY")
        wc_secret = os.environ.get("WOOCOMMERCE_API_SECRET")

        if not wc_key or not wc_secret:
            raise Exception("The API credentials where not set as env variables")
        else:
            return wc_key, wc_secret

    @staticmethod
    def get_db_credentials() -> Tuple[str, str]:
        load_dotenv()

        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")

        if not db_user or not db_pass:
            raise Exception("The DB credentials where not set as env variables")
        else:
            return db_user, db_pass
