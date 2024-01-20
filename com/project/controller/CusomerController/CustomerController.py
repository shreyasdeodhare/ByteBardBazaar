import json
from flask import Flask, request, jsonify
from com.project.services.CustomerServices.CustomerServices import CustomerServices
from com.project.entities.Customer.Customer import Customer
from com.project.logger.logger import Logger
from mysql.connector.errors import  IntegrityError
app = Flask(__name__)

logger = Logger.get_instance()


class CustomerController:
    customerService = CustomerServices()

    @staticmethod
    @app.route('/customers', methods=['GET'])
    def get_all_customers():
        try:
            customer_data = CustomerController.customerService.select_all_customer()
            customers = [Customer(*customer_data).__dict__ for customer_data in customer_data]
            return jsonify(customers)
        except Exception as e:
            logger.log_error(f"Error in get_all_customers: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addcustomer', methods=['POST'])
    def add_customer():
        try:
            customer_data = Customer(**request.get_json())
            customer_dict = customer_data.to_dict()
            result = CustomerController.customerService.insert_customer(customer_data)
            response = json.loads(result)
            if response.get("status") == "error":
                return jsonify({"error":f'Duplicate value :{response["message"]}'}),400
            return jsonify(result)
        # except IntegrityError as ie:
        #     error_message=f'Duplicate value:{ie}'
        #     return jsonify({"error":error_message}),400
        except ValueError as ve:
            logger.log_error(f"ValueError in add_customer: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_customer: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updatecustomer', methods=['PUT'])
    def update_customer():
        try:
            customer_data = Customer(**request.get_json())
            customer_dict = customer_data.to_dict()
            result = CustomerController.customerService.update_customer(customer_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_customer: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_customer: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deletecustomer', methods=['DELETE'])
    def delete_customer():
        try:
            customer_data = Customer(**request.get_json())
            customer_dict = customer_data.to_dict()
            result = CustomerController.customerService.delete_customer(customer_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_customer: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_customer: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
