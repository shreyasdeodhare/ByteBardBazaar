from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.Product.Product import Product
from com.project.logger.logger import Logger
from com.project.query.DatabaseManager import DatabaseManager
from com.project.common.constants import *


class ProductDao:
    def __init__(self):
        self.db_connector = ApplicationConnection()
        self.mycursor = self.db_connector.mycursor
        self.logger = Logger.get_instance()

    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db_connector.mydb.commit()
            self.logger.log_info(f"Query executed successfully: {query}")
        except Exception as e:
            self.db_connector.mydb.rollback()
            self.logger.log_error(f"Error executing query: {query}\nError: {e}")

    def fetch_all_products(self):
        try:
            self.mycursor.execute(QUERY_SELECT_ALL_Product)
            products = self.mycursor.fetchall()
            for product in products:
                self.logger.log_info(product)
            return products
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def insert_product(self, product):
        try:
            insert_query = QUERY_INSERT_Product
            insert_values = (product.p_name, product.p_available_stock, product.p_sell_stock, product.p_price_per_item,
                             product.p_is_available, product.p_category_id,product.inv_id)
            self.execute_query(insert_query, insert_values)
            print(self.mycursor.lastrowid)
            if self.mycursor.lastrowid==0:
               product.p_id = 1
            else:
                product.p_id = self.mycursor.lastrowid

        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def update_product(self, product):
        try:
            update_query = QUERY_UPDATE_Product
            update_values = (product.p_price_per_item, product.p_available_stock,product.p_id)
            self.execute_query(update_query, update_values)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")

    def delete_product(self, product):
        try:
            delete_query = DELETE_Product
            auto_query = AUTO_INCR_PRODUCT
            delete_values = (product.p_id,)
            d_prod_id=product.p_id
            table_name=TABEL_NAME
            self.execute_query(delete_query, delete_values)
            # reset_auto_incr=f"SET @max_id := (SELECT MAX(p_id) FROM {table_name}); " \
            #                    f"SET @new_id := IF({d_prod_id} <= @max_id, {d_prod_id}, @max_id + 1); " \
            #                    f"ALTER TABLE {table_name} AUTO_INCREMENT = @new_id;"
            self.execute_query(auto_query)
        except AttributeError as e:
            self.logger.log_error(f"AttributeError: {e}")


# Example usage:
if __name__ == "__main__":
    product_db = ProductDao()

    # Insert example
    # new_product = Product(None, "Laptop", 150, 30, 15, True, 5)
    # product_db.insert_product(new_product)
    #
    # # Update example
    updated_product = Product(8, None, 60, None, 700, None, None)
    product_db.update_product(updated_product)

    # # Delete example
    # product_to_delete = Product(3, None, None, None, None, None, None)
    # product_db.delete_product(product_to_delete)
