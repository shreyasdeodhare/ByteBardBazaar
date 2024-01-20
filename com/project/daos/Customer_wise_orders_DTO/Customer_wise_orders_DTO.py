from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.logger.logger import Logger
from com.project.common.constants import *
class Customer_wise_orders_DTO:
    def __init__(self):
        self.db_connector = ApplicationConnection()
        self.mycursor = self.db_connector.mycursor
        self.logger = Logger.get_instance()

        # customer=Q()
    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def get_customer_wise_orders_data(self):
        # query=Customer_wise_product_purchases
        # self.mycursor.execute(query)
        try:
            self.mycursor.execute(Customer_wise_orders)
            result = self.mycursor.fetchall()
            for res in result:
                self.logger.log_info(res)
            return result
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")



# #Test
# class AddressDB(Customer_wise_orders_DTO, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
#
# if __name__ == "__main__":
#     address_db = AddressDB()
#     address_db.get_customer_wise_orders_data()


# from com.project.utils.ApplicationConnection import ApplicationConnection
# from com.project.logger.logger import Logger
# from com.project.common.constants import *
#
# class Customer_wise_orders_DTO:
#     def __init__(self):
#         self.db_connector = ApplicationConnection()
#         self.mycursor = self.db_connector.mycursor
#         self.logger = Logger.get_instance()
#
#     def execute_query(self, query, values=None):
#         try:
#             self.mycursor.execute(query, values)
#             self.db_connector.mydb.commit()
#             self.logger.log_info(f"Query executed successfully: {query}")
#         except Exception as e:
#             self.db_connector.mydb.rollback()
#             self.logger.log_error(f"Error executing query: {query}\nError: {e}")
#
#     def get_customer_wise_orders_data(self, year=None):
#         try:
#             if year:
#                 sql_query = f"SELECT cust.cname, st.status_name, pd.p_name, ord.orderDate \
#                               FROM customer cust \
#                               INNER JOIN orders ord ON ord.cid = cust.cid  \
#                               INNER JOIN orderdetails ordd ON ordd.oid = ord.oid \
#                               INNER JOIN status st ON ordd.odid = st.odid \
#                               INNER JOIN product pd ON pd.p_id = ordd.pid \
#                               INNER JOIN product pr ON ordd.pid = pr.p_id \
#                               WHERE YEAR(ord.orderDate) = {year}"
#             else:
#                 sql_query = "SELECT cust.cname, st.status_name, pd.p_name, ord.orderDate \
#                              FROM customer cust \
#                              INNER JOIN orders ord ON ord.cid = cust.cid  \
#                              INNER JOIN orderdetails ordd ON ordd.oid = ord.oid \
#                              INNER JOIN status st ON ordd.odid = st.odid \
#                              INNER JOIN product pd ON pd.p_id = ordd.pid \
#                              INNER JOIN product pr ON ordd.pid = pr.p_id"
#
#             self.mycursor.execute(sql_query)
#             result = self.mycursor.fetchall()
#             for res in result:
#                 self.logger.log_info(res)
#             return result
#         except AttributeError as e:
#             self.logger.log_error(f"AttributeError: {e}")