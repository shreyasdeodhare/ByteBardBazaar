import json
from flask import Flask, request, jsonify
from com.project.services.InventoryServices.InventoryServices import InventoryServices
from com.project.entities.Inventory.Inventory import Inventory
from com.project.logger.logger import Logger
from mysql.connector.errors import  IntegrityError
app = Flask(__name__)

logger = Logger.get_instance()


class InvController:
    inService =InventoryServices()

    @staticmethod
    @app.route('/items', methods=['GET'])
    def get_all_items():
        try:
            inv_data = InvController.inService.select_all_items()
            items = [Inventory(*inv_data).__dict__ for inv_data in inv_data]
            return jsonify(items)
        except Exception as e:
            logger.log_error(f"Error in get_all_customers: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/additem', methods=['POST'])
    def add_item():
        try:
            inv_data = Inventory(**request.get_json())
            inv_dict = inv_data.to_dict()
            result =InvController.inService.insert_items(inv_data)
            # response = json.loads(result)
            # if response.get("status") == "error":
            #     return jsonify({"error":f'Duplicate value :{response["message"]}'}),400
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
    @app.route('/updateitem', methods=['PUT'])
    def update_item():
        try:
            inv_data = Inventory(**request.get_json())
            inv_dict = inv_data.to_dict()
            result = InvController.inService.update_inventory(inv_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_customer: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_customer: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deleteitem', methods=['DELETE'])
    def delete_item():
        try:
            inv_data = Inventory(**request.get_json())
            inv_dict = inv_data.to_dict()
            result = InvController.inService.delete_inventory(inv_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_customer: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_customer: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
