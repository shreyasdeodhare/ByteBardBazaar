from com.project.daos.AddressDao.AddressDao import AddressDao
from com.project.entities.Address.Address import Address
from com.project.logger.logger import Logger

class AddressServices:
    def __init__(self):
        self.address_dao = AddressDao()
        self.logger = Logger.get_instance()

    def select_all_address(self):
        try:
            return self.address_dao.fetch_all_address()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_address(self, address):
        try:
            self.address_dao.insert_address(address)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_address(self, address):
        try:
            self.address_dao.update_address(address)
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

    def delete_address(self, address):
        try:
            self.address_dao.delete_address(address)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

