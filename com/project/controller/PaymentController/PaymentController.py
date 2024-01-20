import json
from flask import Flask, request, jsonify
from com.project.services.PaymentServices.PaymentServices import PaymentServices
from com.project.entities.Payment.Payment import Payment
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class PaymentController:
    paymentService = PaymentServices()

    @staticmethod
    @app.route('/payment', methods=['GET'])
    def get_all_payment():
        try:
            payment_data = PaymentController.paymentService.select_all_payment()
            payment = [Payment(*payment_data).__dict__ for payment_data in payment_data]
            return jsonify(payment)
        except Exception as e:
            logger.log_error(f"Error in get_all_payments: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addpayment', methods=['POST'])
    def add_payment():
        try:
            payment_data = Payment(**request.get_json())
            payment_dict = payment_data.to_dict()
            result = PaymentController.paymentService.insert_payment(payment_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updatepayment', methods=['PUT'])
    def update_payment():
        try:
            payment_data = Payment(**request.get_json())
            payment_dict = payment_data.to_dict()
            result = PaymentController.paymentService.update_payment(payment_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deletepayment', methods=['DELETE'])
    def delete_payment():
        try:
            payment_data = Payment(**request.get_json())
            payment_dict = payment_data.to_dict()
            result = PaymentController.paymentService.delete_payment(payment_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_payment: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_payment: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
