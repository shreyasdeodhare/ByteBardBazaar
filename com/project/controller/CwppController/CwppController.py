from flask import Flask, jsonify
from com.project.services.CustomerWIseProductPurchaseServices.CustomerWiseProductPurchaseServices import CustomerWiseProductPurchaseServices
from com.project.entities.Cwpp.Cwpp import Cwpp
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class CwppController:
    cwpp=CustomerWiseProductPurchaseServices()

    @staticmethod
    @app.route('/cwpp', methods=['GET'])
    def get_all_cwpp():
        try:
            cwpp_data = CwppController.cwpp.select_all_cwpp()
            cwpp1 = [Cwpp(*cwpp_data).__dict__ for cwpp_data in cwpp_data]
            return jsonify(cwpp1)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
