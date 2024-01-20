from com.project.daos.ProductDao.ProductDao import ProductDao
from com.project.entities.Product.Product import Product
from com.project.logger.logger import Logger

class ProductServices:
    def __init__(self):
        self.product_dao = ProductDao()
        self.logger = Logger.get_instance()

    def select_all_product(self):
        try:
            return self.product_dao.fetch_all_products()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_product(self, product):
        try:
            self.product_dao.insert_product(product)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_product(self, product):
        try:
            self.product_dao.update_product(product)
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

    def delete_product(self, product):
        try:
            self.product_dao.delete_product(product)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

