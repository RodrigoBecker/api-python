
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
            self.__connect = sqlite3.connect(self.__file_path)
        return self.__connect
        
    @property
    def close(self):
        if self.__connect != None:
            return self.__connect.close()

    
    def command_execute(self, query:str, query_type:str):
       
        try:
            con = self.connect.cursor()
        
            if query_type == "INSERT" or "UPDATE" or "DELETE":
                con.execute(query)
                self.connect.commit()

            else:
                con.execute(query)
                return con.fetchone()
            
        except Exception as error:
            print(f"ERROR: {error}")
        
        finally:
            self.close

