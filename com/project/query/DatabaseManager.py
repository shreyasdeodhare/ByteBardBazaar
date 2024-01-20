from com.project.common.constants import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from com.project.utils.ApplicationConnection import ApplicationConnection

class DatabaseManager:
    def __init__(self):
        self.connection = ApplicationConnection()._instance

    def execute_query(self, query, params=None):
        if params:
            self.connection.mycursor.execute(query, params)
        else:
            self.connection.mycursor.execute(query)

        result = self.connection.mycursor.fetchall()
        self.connection.mydb.commit()
        return result

    def generate_insert_query(self, data_obj):
        init_params = list(data_obj.__init__.__code__.co_varnames[1:])  # Exclude 'self' parameter
        columns = [param for param in init_params if hasattr(data_obj, f"_{param}")]
        values = [getattr(data_obj, f"_{param}") for param in columns]
        query = f"INSERT INTO {data_obj.__class__.__name__} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"
        return query, values

    def generate_update_query(self, data_obj, condition_column, condition_value):
        init_params = list(data_obj.__init__.__code__.co_varnames[1:])  # Exclude 'self' parameter
        columns = [param for param in init_params if hasattr(data_obj, f"_{param}")]
        values = [getattr(data_obj, f"_{param}") for param in columns]
        set_clause = ', '.join([f"{col} = %s" for col in columns])
        query = f"UPDATE {data_obj.__class__.__name__} SET {set_clause} WHERE {condition_column} = %s"
        return query, values + [condition_value]

    def generate_delete_query(self, data_obj, condition_column, condition_value):
        query = f"DELETE FROM {data_obj.__class__.__name__} WHERE {condition_column} = %s"
        return query, [condition_value]

    def generate_select_query(self, data_obj, condition_column, condition_value):
        query = f"SELECT * FROM {data_obj.__class__.__name__} WHERE {condition_column} = %s"
        return query, [condition_value]

# Example usage:
# class Customer:
#     def __init__(self, cid, cname, cnumber, cemail):
#         self._cid = cid
#         self._cname = cname
#         self._cnumber = cnumber
#         self._cemail = cemail
#
#     # ... (rest of the class remains the same)
#
# # Create instances of Customer
# customer_data = Customer(cid=1, cname="John Doe", cnumber="1234567890", cemail="john@example.com")
#
# # Use DatabaseManager to perform CRUD operations
# db_manager = DatabaseManager()
#
# # Insert
# insert_query, insert_params = db_manager.generate_insert_query(customer_data)
# db_manager.execute_query(insert_query, insert_params)
#
# # Update
# update_query, update_params = db_manager.generate_update_query(customer_data, condition_column="cid", condition_value=1)
# db_manager.execute_query(update_query, update_params)
#
# # Delete
# delete_query, delete_params = db_manager.generate_delete_query(customer_data, condition_column="cid", condition_value=1)
# db_manager.execute_query(delete_query, delete_params)
#
# # Select
# select_query, select_params = db_manager.generate_select_query(customer_data, condition_column="cid", condition_value=1)
# result = db_manager.execute_query(select_query, select_params)
# print(result)
