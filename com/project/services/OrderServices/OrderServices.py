from com.project.daos.OrdersDao.OrdersDao import OrdersDao
from com.project.entities.Orders.Orders import Orders
from com.project.logger.logger import Logger

class OrderServices:
    def __init__(self):
        self.order_dao = OrdersDao()
        self.logger = Logger.get_instance()

    def select_all_order(self):
        try:
            return self.order_dao.fetch_all_orders()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_order(self, order):
        try:
            self.order_dao.insert_orders(order)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_order(self, order):
        try:
            self.order_dao.update_orders(order)
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

    def delete_order(self, order):
        try:
            self.order_dao.delete_orders(order)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

