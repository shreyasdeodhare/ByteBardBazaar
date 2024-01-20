from com.project.daos.TopfiveSellingProductsDao.TopfivesellingDao import TopfivesellingDao
from com.project.logger.logger import Logger

class Tfss:
    def __init__(self):
        self.tfss= TopfivesellingDao()
        self.logger = Logger.get_instance()

    def select_all_tfss(self):
        try:
            return self.tfss.get_top_five_sell()
        except Exception as e:
            self.logger.log_error(f"Error in select_all_employees: {e}")

