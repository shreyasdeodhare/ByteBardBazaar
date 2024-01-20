from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Status.Status import Status
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class StatusDao:
    def __init__(self):
       self.db_connector=ApplicationConnection()
       self.mycursor=self.db_connector.mycursor
       self.logger=Logger.get_instance()
    # status=Status()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_statuss(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Status)
            statuss = self.mycursor.fetchall()
            for status in statuss:
                self.logger.log_info(status)
            return statuss
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_status(self, status):
        try:
            insert_query = QUERY_INSERT_Status
            insert_values = (status.status_id,status.status_name,status.odid)
            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_status(self, status):
        try:
            update_query = QUERY_UPDATE_Status
            update_values = (status.status_name,status.status_id)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_status(self, status):
        try:
            delete_query = DELETE_Status
            delete_values = (status.status_id,)
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

# class StatusDB(StatusDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#     status_db = StatusDB()
#     # status_db.fetch_all_employees()
#     id=4
#
#     status=Status(id,None,None,None)
#     status_db.delete_status(status)