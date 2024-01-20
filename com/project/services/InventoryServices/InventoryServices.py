from com.project.daos.InventoryDao.InventoryDao import InventoryDao
from com.project.entities.Inventory.Inventory import Inventory
from com.project.logger.logger import Logger

class InventoryServices:
    def __init__(self):
        self.inventory_dao = InventoryDao()
        self.logger = Logger.get_instance()

    def select_all_items(self):
        try:
            return self.inventory_dao.fetch_all_inventory()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_items(self, inventory):
        try:
            self.inventory_dao.insert_inventory(inventory)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_inventory(self, inventory):
        try:
            self.inventory_dao.update_inventory(inventory)
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

    def delete_inventory(self, inventory):
        try:
            self.inventory_dao.delete_inventory(inventory)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

