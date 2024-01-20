from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.OrderDetails.OrderDetails import OrderDetails
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class OrderDetailsDao:
    def __init__(self):
       self.db_connector=ApplicationConnection()
       self.mycursor=self.db_connector.mycursor
       self.logger=Logger.get_instance()
    # customer=Q()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_orderDetails(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_OrderDetails)
            orderDetails= self.mycursor.fetchall()
            for orderdetails in orderDetails:
                self.logger.log_info(orderdetails)
            return orderDetails
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_orderDetails(self, orderDetails):
        try:
            insert_query = QUERY_INSERT_OrderDetails
            insert_values = (orderDetails.odid,orderDetails.oid,orderDetails.payid,orderDetails.pid,orderDetails.quantity)
            self.execute_query(insert_query, insert_values)
            if self.mycursor.lastrowid==0:
               orderDetails.odid = 1
            else:
                orderDetails.odid = self.mycursor.lastrowid

        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_orderDetails(self, orderDetails):
        try:
            update_query = QUERY_UPDATE_OrderDetails
            update_values = (orderDetails.quantity,orderDetails.odid)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_orderDetails(self, orderDetails):
        try:
            delete_query = DELETE_OrderDetails
            delete_values = (orderDetails.odid,)
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



# Test
# class OrderDetailsDB(OrderDetailsDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#      orderDetails_db = OrderDetailsDB()
#      orderDetails_db.fetch_all_orderDetails()
#      odid=4
#      oid=2
#      pid=4
#
#      payid=3
#      amount=30
#      orderDetails=OrderDetails(odid,oid,pid,amount,payid)
#      orderDetails_db.delete_orderDetails(orderDetails)