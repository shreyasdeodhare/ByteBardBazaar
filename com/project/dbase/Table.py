import inspect
from com.project.utils.ApplicationConnection import ApplicationConnection
from com.project.entities.OrderDetails.OrderDetails import OrderDetails


class Table:
    def __init__(self, connection):
        self.mydb = connection.connect_to_database()

    def create_table_from_class(self, class_type, table_name, type_mapping=None, primary_key=None, foreign_keys=None):
        attributes = inspect.getmembers(class_type, lambda a: not (inspect.isroutine(a)))
        attribute_names = [a[0] for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]

        # Generate the dynamic table creation query with specified data types, primary key, and foreign keys
        table_query = f"CREATE TABLE {table_name} ("
        for attribute_name in attribute_names:
            mysql_type = type_mapping.get(attribute_name, "VARCHAR(255)") if type_mapping else "VARCHAR(255)"
            table_query += f"{attribute_name} {mysql_type}, "

        # Add primary key with AUTO_INCREMENT if specified
        if primary_key:
            table_query += f"PRIMARY KEY ({primary_key}) , "

        if foreign_keys:
            for fk_column, references in foreign_keys.items():
                table_query += f"FOREIGN KEY ({fk_column}) REFERENCES {references}, "
        table_query = table_query[:-2]  # Remove the trailing comma and space
        table_query += ");"

        # Execute the query to create the table
        self.mydb.cursor().execute(table_query)

        # Commit the changes
        self.mydb.commit()

    def close_connection(self):
        # Disconnect from the database
        self.mydb.close()


# Example usage:
# Create an instance of ApplicationConnection
db_connector = ApplicationConnection()

# Create a Table instance with the connection
table = Table(connection=db_connector)
# odid,oid,pid,quantity,payid
# Define a mapping for data types, primary key, and foreign keys if needed
type_mapping = {
    'odid': 'INT',
    'oid' : 'INT',
    'pid': 'INT',
    'quantity': 'VARCHAR(100)',
    'payid':'INT'

}

# Set the primary key column name and specify it for auto-increment
primary_key = 'odid'

foreign_keys = {
    # Add foreign key definitions if needed
    'oid':'orders(oid)',
    'pid':'product(p_id)',
    'payid':'payments(payid)'

}

# Call the create_table_from_class method
table.create_table_from_class(OrderDetails, 'orderdetails', type_mapping, primary_key, foreign_keys)

# Close the database connection
table.close_connection()
