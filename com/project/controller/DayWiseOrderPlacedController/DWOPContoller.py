from flask import Flask, jsonify
from com.project.services.DaywiseOrderPlacedServices.DWOPServices import DWOPServices

from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class DwopController:
    Dwop=DWOPServices()

    @staticmethod
    @app.route('/dwop', methods=['GET'])
    def get_all_dwop():
        try:
            dwop_data = DwopController.Dwop.select_all_dwop()
            # address = [Address(*address_data).__dict__ for address_data in address_data]
            return jsonify(dwop_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
