# controllers/destinasi_controller.py
from db.nesia_travel_db import NesiaTravelDb
from flask import jsonify, request

db_instance = NesiaTravelDb('localhost', 'root', '', 'nesiatravel')

def get_destinasi():
    try:
        connection = db_instance.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM destinasi')
            fetch_result = cursor.fetchall()
            
            print(f'hasil data: {fetch_result}')
            
            if fetch_result:
                return jsonify({
                    'success': True,
                    'data': fetch_result
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'data ditemukan'
                }), 404
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        if connection and not connection.open:
            connection.close()
            print('Connection closed')

def update_destinasi():
    try:
        data = request.json
        id = data.get('id')
        new_value = data.get('new_value')

        if not id or not new_value:
            return jsonify({
                'success': False,
                'message': 'Missing parameters'
            }), 400
        
        connection = db_instance.get_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE destinasi 
                SET some_column = %s 
                WHERE id = %s
            """, (new_value, id))
            connection.commit()
            
            if cursor.rowcount > 0:
                return jsonify({
                    'success': True,
                    'message': 'Data updated successfully'
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'No data found to update'
                }), 404
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        if connection and not connection.open:
            connection.close()
            print('Connection closed')

def delete_destinasi():
    try:
        data = request.json
        id = data.get('id')

        if not id:
            return jsonify({
                'success': False,
                'message': 'Missing parameters'
            }), 400
        
        connection = db_instance.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM destinasi WHERE id = %s', (id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                return jsonify({
                    'success': True,
                    'message': 'Data deleted successfully'
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'No data found to delete'
                }), 404
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        if connection and not connection.open:
            connection.close()
            print('Connection closed')
