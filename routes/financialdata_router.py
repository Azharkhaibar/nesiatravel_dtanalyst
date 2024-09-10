from controllers.financial_data_controller import get_data_financial
from flask import Blueprint

financial_data_bp = Blueprint('financial_bp', __name__)
financial_data_bp.add_url_rule('/financialdata', 'get_financial_data', get_data_financial)