from controllers.pembimbing_controller import get_pembimbing
from flask import Blueprint

pembimbing_bp = Blueprint('pembimbing_bp', __name__)
pembimbing_bp.add_url_rule('/pembimbing', 'get_pembimbing', get_pembimbing)
