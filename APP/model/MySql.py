import pymysql
import os


class MySql:
    """ Mysql
    """

    MySQLError = pymysql.MySQLError
    ProgrammingError = pymysql.ProgrammingError

     def __init__(self):
        
        host = os.environ['DB_HOSTNAME']
        user = os.environ['DB_USER']
        pwd = os.environ['DB_PASSWORD']
        db = os.environ['DB_NAME']
        port = os.environ['DB_PORT'] || 3306

        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=pwd,
            db=db,
            cursorclass=pymysql.cursors.DictCursor)

    def open(self):
        """ open
        """
        return self.conn.cursor()

    def close(self):
        """ close
        """
        return self.conn.close()

    def commit(self):
        """ commit
        """
        return self.conn.commit()

    def rollback(self):
        """ rollback
        """
        return self.conn.rollback()
