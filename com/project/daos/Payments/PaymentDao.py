from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Payment.Payment  import Payment
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *

class PaymentDao:
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

    def fetch_all_payment(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Payment)
            payments = self.mycursor.fetchall()
            for p in payments :
                self.logger.log_info(p)
            return payments
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_payment (self, payment):
        try:
            insert_query = QUERY_INSERT_Payment
            insert_values = (payment.payid,payment.pdate,payment.amount,payment.paymethod,payment.oid)
            self.execute_query(insert_query, insert_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_payment (self, payment):
        try:
            update_query = QUERY_UPDATE_Payment
            update_values = (payment.amount,payment.pdate,payment.paymethod,payment.payid)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_payment (self, payment):
        try:
            delete_query = DELETE_Payment
            delete_values = (payment.payid,)
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

# class PaymentDB(PaymentDao, Logger):
#     def __init__(self):
#         super().__init__()
#         self.db_connector = ApplicationConnection()
#
# # Testcase
# if __name__ == "__main__":
#      payment_db = PaymentDB()
#      payment_db.fetch_all_payment()
#      payid=5
#      oid=1
#      amount=65000
#      pdate="2023-12-19"
#      paymethod="gpay"
#
#      payment=Payment(payid,pdate,amount,paymethod,oid)
#      payment_db.insert_payment(payment)