import os

import pymysql
from utils.credentials_utils import CredentialsUtilities
import logging as logger
from config.configurations import DB_HOST
from dotenv import load_dotenv


class DBUtility:
    def __init__(self) -> None:
        load_dotenv()
        self.machine = os.environ.get("MACHINE")
        assert self.machine, f"MACHINE env variable not set"
        self.env = os.environ.get("ENV", "test_env")
        self.wp_host = os.environ.get("WP_HOST")
        assert self.wp_host, f"WP_HOST not set"
        # if self.machine == "docker" and self.wp_host == "local":
        #    raise Exception(f"Cannot run tests in docker")

        self.db_user, self.db_pass = CredentialsUtilities().get_db_credentials()

        self.host = DB_HOST[self.machine][self.env]["host"]
        self.socker = DB_HOST[self.machine][self.env]["socket"]
        self.port = DB_HOST[self.machine][self.env]["port"]
        self.database = DB_HOST[self.machine][self.env]["database"]
        self.table_prefix = DB_HOST[self.machine][self.env]["table_prefix"]

    def create_connection(self):
        connection = None
        if self.wp_host == "local":
            connection = pymysql.connect(
                host=self.host, user=self.db_user, password=self.db_pass, port=self.port
            )
            logger.info(
                f"DB: Connection status: Connected to MySQL v{connection.get_server_info()}:{connection.host}"
            )
        return connection

    def execute_select(self, sql: str):
        connection = self.create_connection()
        try:
            cur = connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql} \n Error: {str(e)}")
        finally:
            connection.close()

        return rs_dict


if __name__ == "__main__":
    db = DBUtility()
    conn = db.create_connection()
    sql = f"SELECT * FROM wordpress_v1.wp_users WHERE user_email = 'pluta.m@gmail.com';"
    rs_dict = db.execute_select(sql)
    print(rs_dict)
