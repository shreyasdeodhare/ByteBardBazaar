from flask import Flask, jsonify
from com.project.services.CWoS.Cwosservices import Cwoss
from com.project.services.CustomerWIseProductPurchaseServices.CustomerWiseProductPurchaseServices import CustomerWiseProductPurchaseServices
from com.project.services.DaywiseOrderPlacedServices.DWOPServices import DWOPServices
from com.project.services.DayWiseOrderCanceledServices.DWOCServices import DWOCServices
from com.project.services.TopfiveSellingProductsServices.Tfss import Tfss
from com.project.logger.logger import Logger

app = Flask(__name__)
logger = Logger.get_instance()

class ApiController:
    cwos = Cwoss()
    cwpp = CustomerWiseProductPurchaseServices()
    dwop = DWOPServices()
    dwoc = DWOCServices()
    tfss = Tfss()

    @staticmethod
    @app.route('/cwos', methods=['GET'])
    def get_all_cwos():
        try:
            cwos_data = ApiController.cwos.select_all_cwos()
            return jsonify(cwos_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_cwos: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/cwpp', methods=['GET'])
    def get_all_cwpp():
        try:
            cwpp_data = ApiController.cwpp.select_all_cwpp()
            return jsonify(cwpp_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_cwpp: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/dwop', methods=['GET'])
    def get_all_dwop():
        try:
            dwop_data = ApiController.dwop.select_all_dwop()
            return jsonify(dwop_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_dwop: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/dwoc', methods=['GET'])
    def get_all_dwoc():
        try:
            dwoc_data = ApiController.dwoc.select_all_dwoc()
            return jsonify(dwoc_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_dwoc: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/tfss', methods=['GET'])
    def get_all_tfss():
        try:
            tfss_data = ApiController.tfss.select_all_tfss()
            return jsonify(tfss_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_tfss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8000, debug=True)
