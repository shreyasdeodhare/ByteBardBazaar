import json
from flask import Flask, request, jsonify
from com.project.services.ProductServices.ProductServices import ProductServices
from com.project.entities.Product.Product import Product
from com.project.logger.logger import Logger

app = Flask(__name__)

logger = Logger.get_instance()


class ProductController:
    productService = ProductServices()

    @staticmethod
    @app.route('/product', methods=['GET'])
    def get_all_product():
        try:
            product_data = ProductController.productService.select_all_product()
            product = [Product(*product_data).__dict__ for product_data in product_data]
            return jsonify(product)
        except Exception as e:
            logger.log_error(f"Error in get_all_products: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/addproduct', methods=['POST'])
    def add_product():
        try:
            product_data = Product(**request.get_json())
            product_dict = product_data.to_dict()
            result = ProductController.productService.insert_product(product_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in add_product: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in add_product: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/updateproduct', methods=['PUT'])
    def update_product():
        try:
            product_data = Product(**request.get_json())
            product_dict = product_data.to_dict()
            result = ProductController.productService.update_product(product_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in update_product: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in update_product: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @app.route('/deleteproduct', methods=['DELETE'])
    def delete_product():
        try:
            product_data = Product(**request.get_json())
            product_dict = product_data.to_dict()
            result = ProductController.productService.delete_product(product_data)
            return jsonify(result)
        except ValueError as ve:
            logger.log_error(f"ValueError in delete_product: {ve}")
            return jsonify({"error": f'Invalid data format: {ve}'}), 400
        except Exception as e:
            logger.log_error(f"Error in delete_product: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
