from typing import Dict

API_HOSTS: dict[str, str] = {
    "test_env": "http://localhost:8888/wordpress_v2/wp-json/wc/v3/"
}
WOO_API_HOSTS: dict[str, str] = {"test_env": "http://localhost:8888/wordpress_v2/"}

DB_HOST = {
    "machine1": {
        "test_env": {
            "host": "127.0.0.1",
            "database": "wordpress_v2",
            "table_prefix": "wp2p_",
            "socket": None,
            "port": 8889,
        }
    },
    "docker": {
        "test_env": {
            "host": "host.docker.internal",
            "database": "wp398",
            "table_prefix": "wp2p_",
            "socket": None,
            "port": 3306,
        }
    },
}
