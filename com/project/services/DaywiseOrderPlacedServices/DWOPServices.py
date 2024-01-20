from com.project.daos.DaywiseOrderPlacedDao.DWOPDTO import DWOPDTO
from com.project.logger.logger import Logger

class DWOPServices:
    def __init__(self):
        self.dwop= DWOPDTO()
        self.logger = Logger.get_instance()

    def select_all_dwop(self):
        try:
            return self.dwop.get_customer_wise_purchase_data()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

