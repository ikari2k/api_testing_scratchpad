from utils.db_utils import DBUtility
import logging as logger


class CustomersDAO:

    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email: str):
        sql = f"SELECT * FROM wordpress_v1.wp_users WHERE user_email = '{email}';"
        logger.info(f"DAO: Executing sql: {sql}")
        rs_sql = self.db_helper.execute_select(sql)
        logger.info(f"DAO: Returned data: {rs_sql}")
        return rs_sql


if __name__ == "__main__":
    cdao = CustomersDAO()
    result_sql = cdao.get_customer_by_email("pluta.m@gmail.com")
    print(result_sql)
