from controllers.customer_data_controller import get_customer_data
from flask import Blueprint

customer_data_bp = Blueprint('customer_data_bp', __name__)
customer_data_bp.add_url_rule('/customer', 'get_customer_data', get_customer_data)