import json

from com.project.utils.ApplicationConnection import ApplicationConnection
# from com.project.entities.Customer.Customer import Customer
from com.project.logger.logger import Logger
# from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class CustomerDao:
    def __init__(self):
       self.db_connector=ApplicationConnection()
       self.mycursor=self.db_connector.mycursor
       self.logger=Logger.get_instance()
    # customer=Customer()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_customers(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Customer)
            customers = self.mycursor.fetchall()
            for customer in customers:
                self.logger.log_info(customer)
            return customers
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_customer(self, customer):
        try:
            check_query=DUPLICATE_CHECK
            check_value=(customer.c_number,)
            self.mycursor.execute(check_query,check_value)
            count=self.mycursor.fetchone()[0]
            if count>0:
                erro_msg=f"Error : c_number '{customer.c_number}' already exists."
                self.logger.log_error(erro_msg)
                response={"status":"error","message":erro_msg}
                return json.dumps(response)
            insert_query = QUERY_INSERT_Customer
            insert_values = (customer.cid,customer.cname,customer.c_email,customer.c_number)
            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_cusotmer(self, customer):
        try:
            update_query = QUERY_UPDATE_Customer
            update_values = (customer.c_number,customer.cname,customer.c_email,customer.cid)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_customer(self, customer):
        try:
            delete_query = DELETE_QUERY
            delete_values = (customer.cid,)
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

# class CustomerDB(CustomerDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#     customer_db = CustomerDB()
#     # customer_db.fetch_all_employees()
#     id=4
#
#     customer=Customer(id,None,None,None)
#     customer_db.delete_customer(customer)