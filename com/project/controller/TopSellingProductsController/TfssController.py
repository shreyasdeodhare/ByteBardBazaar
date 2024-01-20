from flask import Flask, jsonify
from com.project.services.TopfiveSellingProductsServices.Tfss import Tfss

from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class TfssController:
    Tfss=Tfss()

    @staticmethod
    @app.route('/tfss', methods=['GET'])
    def get_all_tfss():
        try:
            tfss_data = TfssController.Tfss.select_all_tfss()

            # address = [Address(*address_data).__dict__ for address_data in address_data]
            return jsonify(tfss_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
