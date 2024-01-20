from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.logger.logger import Logger
from com.project.common.constants import *





class DWOPDTO:

    def __init__(self):
        # self.db_connector = ApplicationConnection()
        # self.cid = cid
        # self.cname = cname
        # self.oid = oid
        # self.sodid = sodid
        # self.odid = odid

        # def __init__(self):
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

    def get_customer_wise_purchase_data(self):
        # query=Customer_wise_product_purchases
        # self.mycursor.execute(query)
        try:
            self.mycursor.execute(Daywise_total_orders_placed)
            result = self.mycursor.fetchall()
            for res in result:
                self.logger.log_info(res)
            return result
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")


#TEst

class AddressDB(DWOPDTO, Logger):
    def __init__(self):
        super().__init__()
        self.db_connector = ApplicationConnection()


if __name__ == "__main__":
    address_db = AddressDB()
    address_db.get_customer_wise_purchase_data()


