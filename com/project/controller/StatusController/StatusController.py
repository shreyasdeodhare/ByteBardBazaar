import json
from flask import Flask, request, jsonify
from com.project.services.StatusServices.StatusServices import StatusServices
from com.project.entities.Status.Status import Status
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class StatusController:
    statusService = StatusServices()

    @staticmethod
    @app.route('/status', methods=['GET'])
    def get_all_statuss():
        try:
            status_data = StatusController.statusService.select_all_status()
            statuss = [Status(*status_data).__dict__ for status_data in status_data]
            return jsonify(statuss)
        except Exception as e:
            logger.log_error(f"Error in get_all_statuss: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addstatus', methods=['POST'])
    def add_status():
        try:
            status_data = Status(**request.get_json())
            status_dict = status_data.to_dict()
            result = StatusController.statusService.insert_status(status_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_status: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_status: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updatestatus', methods=['PUT'])
    def update_status():
        try:
            status_data = Status(**request.get_json())
            status_dict = status_data.to_dict()
            result = StatusController.statusService.update_status(status_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_status: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_status: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deletestatus', methods=['DELETE'])
    def delete_status():
        try:
            status_data = Status(**request.get_json())
            status_dict = status_data.to_dict()
            result = StatusController.statusService.delete_status(status_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_status: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_status: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
