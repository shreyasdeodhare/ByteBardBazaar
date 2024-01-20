from com.project.daos.DayWiseOrderCanceledDao.DWOCDTO import DWOCDTO
from com.project.logger.logger import Logger

class DWOCServices:
    def __init__(self):
        self.dwoc= DWOCDTO()
        self.logger = Logger.get_instance()

    def select_all_dwoc(self):
        try:
            return self.dwoc.get_customer_wise_purchase_data()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

