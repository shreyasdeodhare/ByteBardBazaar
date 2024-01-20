from com.project.daos.Payments.PaymentDao import PaymentDao
from com.project.entities.Payment.Payment import Payment
from com.project.logger.logger import Logger

class PaymentServices:
    def __init__(self):
        self.payment_dao = PaymentDao()
        self.logger = Logger.get_instance()

    def select_all_payment(self):
        try:
            return self.payment_dao.fetch_all_payment()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_payment(self, payment):
        try:
            self.payment_dao.insert_payment(payment)
        except Exception as e:
            self.logger.log_error(f"Error in insert_employee: {e}")

    def update_payment(self, payment):
        try:
            self.payment_dao.update_payment(payment)
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

    def delete_payment(self, payment):
        try:
            self.payment_dao.delete_payment(payment)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

