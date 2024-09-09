from controllers.karyawan_controller import get_karyawan, ETLone
from flask import Blueprint

karyawan_bp = Blueprint('karyawan_bp', __name__)

karyawan_bp.add_url_rule('/karyawan', 'get_karyawan', get_karyawan)
karyawan_bp.add_url_rule('/karyawan/ETL', 'ETLone', ETLone)
