import json
from flask import Flask, request, jsonify
from com.project.services.OrderServices.OrderServices import OrderServices
from com.project.entities.Orders.Orders import Orders
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class OrderController:
    orderService = OrderServices()

    @staticmethod
    @app.route('/orders', methods=['GET'])
    def get_all_orders():
        try:
            order_data = OrderController.orderService.select_all_order()
            orders = [Orders(*order_data).__dict__ for order_data in order_data]
            return jsonify(orders)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addorders', methods=['POST'])
    def add_orders():
        try:
            order_data = Orders(**request.get_json())
            order_dict = order_data.to_dict()
            result = OrderController.orderService.insert_order(order_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_address: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_address: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updateorders', methods=['PUT'])
    def update_orders():
        try:
            orders_data = Orders(**request.get_json())
            orders_dict = orders_data.to_dict()
            result = OrderController.orderService.update_order(orders_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_address: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_address: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deleteorders', methods=['DELETE'])
    def delete_orders():
        try:
            orders_data = Orders(**request.get_json())
            orders_dict = orders_data.to_dict()
            result = OrderController.orderService.delete_order(orders_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_orders: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_orders: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
