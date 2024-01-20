from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Address.Address import Address
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class AddressDao:
    def __init__(self):
       self.db_connector=ApplicationConnection()
       self.mycursor=self.db_connector.mycursor
       self.logger=Logger.get_instance()
    # address=Address()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_address(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Address)
            addresss = self.mycursor.fetchall()
            for address in addresss:
                self.logger.log_info(address)
            return addresss
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_address(self, address):
        try:
            insert_query = QUERY_INSERT_Address
            insert_values = (address.aid,address.cid,address.city,address.country,address.state,address.street,address.zipcode)

            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_address(self, address):
        try:
            update_query = QUERY_UPDATE_Address
            update_values = (address.city,address.aid)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_address(self, address):
        try:
            delete_query = DELETE_Address
            delete_values = (address.aid,)
            self.execute_query(delete_query, delete_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    # def fetch_employee_salary_less_than_tenk(self):
    #     try:
    #         self.mycursor.execute(QUERY_SELECT_RANGE)
    #         employees_data = self.mycursor.fetchall()
    #         employees = [PydanticEmployee(**emp) for emp in employees_data]
    #
    #         for emp in employees:
    #             self.logger.log_info(emp)
    #
    #         return employees
    #     except AttributeError as e:
    #         self.logger.log_error(f"AttributeError: {e}")
    #
    # def fetch_employee_salary_greater_than_tenk(self):
    #     try:
    #         self.mycursor.execute(GREATER_THAN_TEN)
    #         employees_data = self.mycursor.fetchall()
    #         employees = [PydanticEmployee(**emp) for emp in employees_data]
    #
    #         for emp in employees:
    #             self.logger.log_info(emp)
    #
    #         return employees
    #     except AttributeError as e:
    #         self.logger.log_error(f"AttributeError: {e}")

# class AddressDB(AddressDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#     address_db = AddressDB()
#     # address_db.fetch_all_address()
#     aid=2
#     cid=3
#     city="Solapur"
#     country="India"
#     state="Maharashtra"
#     street="Magarpatta"
#     zipcode="41967"
#
#     address=Address(aid,None,city,None,None,None,None)
#     address_db.update_address(address)