from controllers.destinasi_controller import get_destinasi, update_destinasi, delete_destinasi
from flask import Flask
from routes.destinasi_router import destinasi_bp
from routes.karyawan_router import karyawan_bp
from routes.pembimbing_router import pembimbing_bp
from routes.financialdata_router import financial_data_bp

app = Flask(__name__)

app.register_blueprint(destinasi_bp, url_prefix='/api')
app.register_blueprint(karyawan_bp, url_prefix='/api')
app.register_blueprint(pembimbing_bp, url_prefix='/api')
app.register_blueprint(financial_data_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
