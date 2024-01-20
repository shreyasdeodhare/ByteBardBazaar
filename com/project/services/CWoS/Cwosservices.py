from com.project.daos.Customer_wise_orders_DTO.Customer_wise_orders_DTO import Customer_wise_orders_DTO
from com.project.entities.Orders.Orders import Orders
from com.project.logger.logger import Logger

class Cwoss:
    def __init__(self):
        self.cwos=Customer_wise_orders_DTO()
        self.logger = Logger.get_instance()

    def select_all_cwos(self):
        try:
            return self.cwos.get_customer_wise_orders_data()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")


# from com.project.daos.Customer_wise_orders_DTO.Customer_wise_orders_DTO import Customer_wise_orders_DTO
# from com.project.logger.logger import Logger
#
# class Cwoss:
#     def __init__(self):
#         self.cwos = Customer_wise_orders_DTO()
#         self.logger = Logger.get_instance()
#
#     def select_cwos_by_year(self, year=None):
#         try:
#             return self.cwos.get_customer_wise_orders_data(year)
#         except Exception as e:
#             self.logger.log_error(f"Error in select_cwos_by_year: {e}")
