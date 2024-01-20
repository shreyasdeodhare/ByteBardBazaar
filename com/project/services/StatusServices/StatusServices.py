from com.project.daos.StatusDao.StatusDao import StatusDao
from com.project.entities.Status.Status import Status
from com.project.logger.logger import Logger

class StatusServices:
    def __init__(self):
        self.status_dao = StatusDao()
        self.logger = Logger.get_instance()

    def select_all_status(self):
        try:
            return self.status_dao.fetch_all_statuss()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_status(self, status):
        try:
            self.status_dao.insert_status(status)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_status(self, status):
        try:
            self.status_dao.update_status(status)
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

    def delete_status(self, status):
        try:
            self.status_dao.delete_status(status)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

