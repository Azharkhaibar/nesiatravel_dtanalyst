from controllers.destinasi_controller import get_destinasi, update_destinasi, delete_destinasi
from flask import Blueprint

destinasi_bp = Blueprint('destinasi_bp', __name__)
destinasi_bp.add_url_rule('/destinasi', 'get_destinasi', get_destinasi, methods=['GET'])
destinasi_bp.add_url_rule('/destinasi/update', 'update_destinasi', update_destinasi, methods=['PUT'])
destinasi_bp.add_url_rule('/destinasi/delete', 'delete_destinasi', delete_destinasi, methods=['DELETE'])
