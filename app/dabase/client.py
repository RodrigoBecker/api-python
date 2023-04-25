import os
import sqlite3
from typing import Optional


class Database:
    def __init__(self, file_path: Optional[str] = None) -> None:
        self.__file_path = file_path or os.environ["FILE_PATH_DB"]
        self.__connect = None

    @property
    def connect(self):
        if self.__connect is None:
            self.__connect = sqlite3.Connection(self.__file_path)
        return self.__connect

    @property
    def close(self):
        if self.__connect != None:
            return self.__connect.close()

    def command_execute(self, *, query: str, query_type: str):
        try:
            con = self.connect.cursor()

            if (
                query_type == "INSERT"
                or query_type == "UPDATE"
                or query_type == "DELETE"
            ):
                con.execute(query)
                self.connect.commit()

            else:
                con = self.connect
                con.row_factory = sqlite3.Row
                response = con.execute(query).fetchall()

                list_item = []
                for item in response:
                    list_item.append({k: item[k] for k in item.keys()})
                return list_item

        except Exception as error:
            print(f"ERROR: {error}")

        finally:
            self.close
