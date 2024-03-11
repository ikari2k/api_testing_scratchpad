from woocommerce import API
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

url = os.getenv("SITE_URL")
key = os.getenv("WOOCOMMERCE_API_KEY")
secret = os.getenv("WOOCOMMERCE_API_SECRET")

woocommerce_api = API(
    url=url, consumer_key=key, consumer_secret=secret, version="wc/v3"
)

products_request = woocommerce_api.get("products")
orders_request = woocommerce_api.get("orders")


pprint.pprint(products_request.json())
pprint.pprint(orders_request.json())
