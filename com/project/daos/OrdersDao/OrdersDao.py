from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Orders.Orders import Orders
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class OrdersDao:
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

    def fetch_all_orders(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Orders)
            orders= self.mycursor.fetchall()
            for order in orders:
                self.logger.log_info(order)
            return orders
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_orders(self, orders):
        try:
            insert_query = QUERY_INSERT_Orders
            insert_values = (orders.oid,orders.cid,orders.orderdate,orders.payid)
            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_orders(self, orders):
        try:
            update_query = QUERY_UPDATE_Orders
            update_values = (orders.orderdate,orders.oid)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_orders(self, orders):
        try:
            delete_query = DELETE_Orders
            delete_values = (orders.oid,)
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

# class OrdersDB(OrdersDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#      orders_db = OrdersDB()
#      orders_db.fetch_all_orders()
# #      oid=2
# #      cid=3
# #      orderdate="2023-12-15 18:11:00"
# #      payid=2
# #      orders=Orders(oid,cid,orderdate,payid)
# #      orders_db.insert_orders(orders)