from flask import Flask, jsonify
from com.project.services.DayWiseOrderCanceledServices.DWOCServices import DWOCServices

from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class DwocController:
    Dwoc=DWOCServices()

    @staticmethod
    @app.route('/dwoc', methods=['GET'])
    def get_all_dwoc():
        try:
            dwoc_data = DwocController.Dwoc.select_all_dwoc()

            # address = [Address(*address_data).__dict__ for address_data in address_data]
            return jsonify(dwoc_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
