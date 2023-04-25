import json

from app.dabase.client import Database
from app.interfaces.users import UserCreateInput, UsersListOutPut


class UseCaseServiceUsers:
    def __init__(self) -> None:
        self.__database = Database()

    def insert_user(self, user: UserCreateInput) -> bool:
        try:
            query = f"""INSERT INTO users
            (name, last_name, cpf, identity_register, age, birthdate , mother_name, email)
            VALUES('{user.name}', '{user.last_name}', 
                                               '{user.cpf}', 
                                               '{user.identity_register}',
                                               '{user.age}',
                                               '{user.birthdate}',
                                               '{user.mother_name}',
                                               '{user.email}'
                                            )"""

            self.__database.command_execute(query=query.strip(), query_type="INSERT")
            return True

        except Exception as error:
            print(f"ERROR: {error}")
            return False

    def get_users(self) -> UsersListOutPut:
        try:
            query = f"SELECT * FROM USERS"

            response = self.__database.command_execute(
                query=query.strip(), query_type="SELECT"
            )

            return UsersListOutPut(users=response)

        except Exception as error:
            print(f"ERROR: {error}")
