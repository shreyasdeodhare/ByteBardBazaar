from com.project.daos.CustomerWiseProductPurchasesDao.CustomerWiseProductPurchases import CustomerWiseProductPurchases
from com.project.logger.logger import Logger

class CustomerWiseProductPurchaseServices:
    def __init__(self):
        self.cwpp= CustomerWiseProductPurchases()
        self.logger = Logger.get_instance()

    def select_all_cwpp(self):
        try:
            return self.cwpp.get_customer_wise_purchase_data()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

