from db.nesia_travel_db import NesiaTravelDb
from flask import jsonify, request

db_instance = NesiaTravelDb('localhost', 'root', '', 'nesiatravel')

def get_karyawan():
    get_connection = None
    try:
        get_connection = db_instance.get_connection()
        with get_connection.cursor() as cursor:
            cursor.execute('SELECT * FROM karyawan')
            fetch_karyawan_result = cursor.fetchall()
            
            print(f'karyawan result: {fetch_karyawan_result}')
            if fetch_karyawan_result:
                return jsonify({
                    'success': True,
                    'data': fetch_karyawan_result
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
            print('Connection closed')

def ETLone():
    get_connection = None
    try:
        get_connection = db_instance.get_connection()
        with get_connection.cursor() as cursor:
            query = """
                SELECT nama_karyawan, gaji, role, tempat_kerja 
                FROM karyawan 
                WHERE gaji < %s AND tunjangan < %s AND tempat_kerja IN (%s, %s, %s)
                """
            cursor.execute(query, (3500, 900, 'officer 1', 'officer 2', 'officer 3'))
            result_fecth_custom = cursor.fetchall()
            
            print(f'Result data yg terpisahkan: {result_fecth_custom}')
            
            if result_fecth_custom:
                return jsonify({
                    'success': True,
                    'data': result_fecth_custom
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
            print('Connection closed')
