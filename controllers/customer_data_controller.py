from db.nesia_travel_db import NesiaTravelDb
from flask import request, jsonify

db_instance = NesiaTravelDb('localhost', 'root', '', 'nesiatravel')

def get_customer_data():
    get_connection = None
    try:
        get_connection = db_instance.get_connection()
        with get_connection.cursor() as cursor:
            cursor.execute('SELECT * FROM customer_data_travel')
            result_data_customer = cursor.fetchall()
            if result_data_customer:
                print(f'Result fetch data customer: {result_data_customer}')
                return jsonify({
                    'success': True,
                    'data': result_data_customer
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Data not found'
                }), 404
    except Exception as e:
        print(f'Error Occurred: {e}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        if get_connection:
            get_connection.close() 
            print('Connection is closed now')
