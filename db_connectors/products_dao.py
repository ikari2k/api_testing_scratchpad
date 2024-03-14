import random

from utils.db_utils import DBUtility


class ProductDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty: int = 1):
        sql = "SELECT * FROM wordpress_v1.wp_posts WHERE post_type = 'product' ORDER BY id DESC LIMIT 500;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, qty)

    def get_product_by_id(self, product_id: int):
        sql = f"SELECT * FROM wordpress_v1.wp_posts WHERE ID = {product_id} LIMIT 500;"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_product_created_after_given_date(self, date):
        sql = f"SELECT * FROM wordpress_v1.wp_posts WHERE post_type = 'product' AND post_date > '{date}' LIMIT 500;"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
