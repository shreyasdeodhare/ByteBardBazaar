import json
from flask import Flask, request, jsonify
from com.project.services.AddressServices.AddressService import AddressServices
from com.project.entities.Address.Address import Address
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class AddressController:
    addressService = AddressServices()

    @staticmethod
    @app.route('/address', methods=['GET'])
    def get_all_address():
        try:
            address_data = AddressController.addressService.select_all_address()
            address = [Address(*address_data).__dict__ for address_data in address_data]
            return jsonify(address)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addaddress', methods=['POST'])
    def add_address():
        try:
            address_data = Address(**request.get_json())
            address_dict = address_data.to_dict()
            result = AddressController.addressService.insert_address(address_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_address: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_address: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updateaddress', methods=['PUT'])
    def update_address():
        try:
            address_data = Address(**request.get_json())
            address_dict = address_data.to_dict()
            result = AddressController.addressService.update_address(address_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_address: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_address: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deleteaddress', methods=['DELETE'])
    def delete_address():
        try:
            address_data = Address(**request.get_json())
            address_dict = address_data.to_dict()
            result = AddressController.addressService.delete_address(address_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_address: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_address: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
