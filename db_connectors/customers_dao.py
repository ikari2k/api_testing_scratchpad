from utils.db_utils import DBUtility
import logging as logger
import random


class CustomersDAO:

    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email: str):
        sql = f"SELECT * FROM wordpress_v1.wp_users WHERE user_email = '{email}';"
        logger.info(f"DAO: Executing sql: {sql}")
        rs_sql = self.db_helper.execute_select(sql)
        logger.info(f"DAO: Returned data: {rs_sql}")
        return rs_sql

    def get_random_customer_from_db(self, qty: int = 1):
        sql = "SELECT * FROM wordpress_v1.wp_users ORDER BY id DESC LIMIT 500;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, qty)


if __name__ == "__main__":
    cdao = CustomersDAO()
    result_sql = cdao.get_customer_by_email("pluta.m@gmail.com")
    print(result_sql)
