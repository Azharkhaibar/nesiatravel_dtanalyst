import pymysql.cursors

class NesiaTravelDb:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def get_connection(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print('Successfully connected to the database')
            return connection
        except pymysql.MySQLError as e:
            print(f'Error occurred: {e}')
            raise
