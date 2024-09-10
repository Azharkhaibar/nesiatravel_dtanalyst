from flask import request, jsonify
from db.nesia_travel_db import NesiaTravelDb

db_instance = NesiaTravelDb('localhost', 'root', '', 'nesiatravel')

def get_data_financial():
    get_connection = None
    try:
        get_connection = db_instance.get_connection()
        with get_connection.cursor() as cursors:
            cursors.execute("""
                            SELECT * FROM 
                            financial_data_nesiatravel
                            """)
            result_data_financial = cursors.fetchall()
            if result_data_financial:
                print(f'fetch berhasil : {result_data_financial}')
                return jsonify({
                    'success': True,
                    'data': result_data_financial
                })
            else:
                return jsonify({
                    'success': False,
                    'messages': 'failed to fetch data'  
                }), 404
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        if get_connection and get_connection.open:
            get_connection.close()
            print('connection closed')
