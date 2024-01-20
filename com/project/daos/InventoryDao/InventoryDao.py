from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Inventory.Inventory import Inventory
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class InventoryDao:
    def __init__(self):
       self.db_connector=ApplicationConnection()
       self.mycursor=self.db_connector.mycursor
       self.logger=Logger.get_instance()
    # inventory=Inventory()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_inventory(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Inventory)
            inventorys = self.mycursor.fetchall()
            for inventory in inventorys:
                self.logger.log_info(inventory)
            return inventorys
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_inventory(self, inventory):
        try:
            insert_query = QUERY_INSERT_Inventory
            insert_values = (inventory.quantity,inventory.created_at,inventory.modified_at,inventory.deleted_at,inventory.inv_id,inventory.pid)

            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_inventory(self, inventory):
        try:
            update_query = QUERY_UPDATE_Inventory
            update_values = (inventory.quantity,inventory.inv_id)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_inventory(self, inventory):
        try:
            delete_query = DELETE_Inventory
            delete_values = (inventory.inv_id,)
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

# class InventoryDB(InventoryDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#     inventory_db = InventoryDB()
#     # inventory_db.fetch_all_inventory()
#     q=5000
#     created_at="2022-11-09 09:10"
#     pid=8
#     inv_id= 3
#     inventory=Inventory(None,None,None,None,None,inv_id)
#     inventory_db.delete_inventory(inventory)