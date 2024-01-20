import json
from flask import Flask, request, jsonify
from com.project.services.OrderDetailsServices.OrderDetaisServices import OrderDetaisServices
from com.project.entities.OrderDetails.OrderDetails import OrderDetails
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class OrderDetailsController:
    orderDetailsService=OrderDetaisServices()

    @staticmethod
    @app.route('/orderdetails', methods=['GET'])
    def get_all_payment():
        try:
            oddata = OrderDetailsController.orderDetailsService.select_all_orderdetails()
            odd = [OrderDetails(*oddata).__dict__ for oddata in oddata]
            return jsonify(odd)
        except Exception as e:
            logger.log_error(f"Error in get_all_orderdetails: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addod', methods=['POST'])
    def add_orderdetails():
        try:
            oddata = OrderDetails(**request.get_json())
            oddata_dict = oddata.to_dict()
            result = OrderDetailsController.orderDetailsService.insert_orderdetails(oddata)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updateorderdetails', methods=['PUT'])
    def update_ordetails():
        try:
            oddata = OrderDetails(**request.get_json())
            payment_dict = oddata.to_dict()
            result = OrderDetailsController.orderDetailsService.update_orderdetails(oddata)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deleteorderdetails', methods=['DELETE'])
    def delete_orderDetails():
        try:
            oddata = OrderDetails(**request.get_json())
            payment_dict = oddata.to_dict()
            result = OrderDetailsController.orderDetailsService.delete_orderdetails(oddata)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
