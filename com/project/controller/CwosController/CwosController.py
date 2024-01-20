import json
from flask import Flask, request, jsonify
from com.project.services.CWoS.Cwosservices import Cwoss

from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class CwosController:
    cwos=Cwoss()

    @staticmethod
    @app.route('/cwos', methods=['GET'])
    def get_all_cwos():
        try:
            cwos_data = CwosController.cwos.select_all_cwos()
            # address = [Address(*address_data).__dict__ for address_data in address_data]
            return jsonify(cwos_data)
        except Exception as e:
            logger.log_error(f"Error in get_all_addresss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)



# import json
# from flask import Flask, request, jsonify
# from com.project.services.CWoS.Cwosservices import Cwoss
# from com.project.logger.logger import Logger
#
# app = Flask(__name__)
#
# logger = Logger.get_instance()
#
# class CwosController:
#     cwos = Cwoss()
#
#     @staticmethod
#     @app.route('/cwos', methods=['POST'])  # Change the method to POST
#     def get_all_cwos():
#         try:
#             # Extract the year parameter from the POST request
#             year = request.form.get('year')
#
#             # Call the service method with the extracted year parameter
#             cwpp_data = CwosController.cwos.select_all_cwos(year)
#
#             # Return the result as JSON
#             return jsonify(cwpp_data)
#         except Exception as e:
#             logger.log_error(f"Error in get_all_addresss: {e}")
#             return jsonify({"error": "Internal Server Error"}), 500
#
# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8000, debug=True)



# import json
# from flask import Flask, request, jsonify
# from com.project.services.CWoS.Cwosservices import Cwoss
# from com.project.logger.logger import Logger
#
# app = Flask(__name__)
#
# logger = Logger.get_instance()
#
# class CwosController:
#     cwos = Cwoss()
#
#     @staticmethod
#     @app.route('/cwos', methods=['POST'])
#     def get_cwos_by_year():
#         try:
#             # Get the year parameter from the POST request
#             year = request.form.get('year')
#
#             # Validate that the year is provided
#             if not year:
#                 return jsonify({"error": "Year parameter is missing"}), 400
#
#             cwpp_data = CwosController.cwos.select_cwos_by_year(year)
#             return jsonify(cwpp_data)
#         except Exception as e:
#             logger.log_error(f"Error in get_cwos_by_year: {e}")
#             return jsonify({"error": "Internal Server Error"}), 500
#
# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8000, debug=True)
