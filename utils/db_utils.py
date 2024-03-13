import pymysql
from utils.credentials_utils import CredentialsUtilities
import logging as logger


class DBUtility:
    def __init__(self) -> None:
        self.db_user, self.db_pass = CredentialsUtilities().get_db_credentials()
        self.host = "localhost"

    def create_connection(self):
        connection = pymysql.connect(
            host=self.host, user=self.db_user, password=self.db_pass, port=8889
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
