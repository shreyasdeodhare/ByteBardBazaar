from com.project.daos.CustomerDao.CustomerDao import CustomerDao
from com.project.entities.Customer.Customer import Customer
from com.project.logger.logger import Logger
import json
from mysql.connector.errors import  IntegrityError
class CustomerServices:
    def __init__(self):
        self.customer_dao = CustomerDao()
        self.logger = Logger.get_instance()

    def select_all_customer(self):
        try:
            return self.customer_dao.fetch_all_customers()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

    def insert_customer(self, customer):
        try:
            result= self.customer_dao.insert_customer(customer)
            if result is None:
                error_msg='Error: Unable to process the request.'
                self.logger.log_error(error_msg)
                response={"status": "error" ,"message" : error_msg}
                return json.dumps(response)
            return result

            # success_message = f"Customer with c_number '{customer.c_number}' inserted successfully."
            # response = {"status": "success", "message": success_message}
            # return json.dumps(response)
        # except IntegrityError as ie:
        #
        #     error_message = f"Error: c_number '{customer.c_number}' already exists.:{ie}"
        #     self.logger.log_error(error_message)
        #
        #     response = {"status": "error", "message": error_message}
        #     return json.dumps(response)
        except Exception as e:

            self.logger.log_error(f"Error in insert_customer: {e}")

            response = {"status": "error", "message": "Internal Server Error"}
            return json.dumps(response)

    def update_customer(self, customer):
        try:
            self.customer_dao.update_cusotmer(customer)
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

    def delete_customer(self, customer):
        try:
            self.customer_dao.delete_customer(customer)
        except Exception as e:
            self.logger.log_error(f"Error in delete_employee: {e}")

