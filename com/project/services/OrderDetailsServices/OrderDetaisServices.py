from com.project.daos.OrderDetails.OrderDetailsDao import  OrderDetailsDao
from com.project.entities.OrderDetails.OrderDetails import OrderDetails
from com.project.logger.logger import Logger
class OrderDetaisServices:
    def __init__(self):
        self.orderdetailsdao = OrderDetailsDao()
        self.logger = Logger.get_instance()
    def select_all_orderdetails(self):
        try:
            return self.orderdetailsdao.fetch_all_orderDetails()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_orderdetails: {e}")

    def insert_orderdetails(self, orderDetails):
        try:
            self.orderdetailsdao.insert_orderDetails(orderDetails)
        except Exception as e:
            self.logger.log_error(f"Error in insert_orderdetails: {e}")

    def update_orderdetails(self, orderdetails):
        try:
            self.orderdetailsdao.update_orderDetails(orderdetails)
        except Exception as e:
            self.logger.log_error(f"Error in update_employee_salary: {e}")

    # def update_employee_name(self, employee):
    #     try:
    #         self.employee_dao.update_employee_name(employee)
    #     except Exception as e:
    #         self.logger.log_error(f"Error in update_employee_name: {e}")
    #
    # def update_employee(self, employee):
    #     try:
    #         self.employee_dao.update_employee(employee)
    #     except Exception as e:
    #         self.logger.log_error(f"Error in update_employee: {e}")

    def delete_orderdetails(self, orderDetails):
        try:
            self.orderdetailsdao.delete_orderDetails(orderDetails)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

