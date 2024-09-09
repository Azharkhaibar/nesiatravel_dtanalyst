from db.nesia_travel_db import NesiaTravelDb
from flask import jsonify, request

db_instance = NesiaTravelDb('localhost', 'root', '', 'nesiatravel')

def get_pembimbing():
    get_connection = None
    try:
        get_connection = db_instance.get_connection()
        with get_connection.cursor() as cursors:
            cursors.execute('SELECT * FROM pembimbing')
            result_fetch_pembimbing = cursors.fetchall()
            print(f'hasil fetch: {result_fetch_pembimbing}')
            if result_fetch_pembimbing:
                return jsonify({
                    'success': True,
                    'data': result_fetch_pembimbing
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'No data found'
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