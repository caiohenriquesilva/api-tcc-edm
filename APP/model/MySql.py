import pymysql


class MySqlr:
    """ Mysqlr
    """

    MySQLError = pymysql.MySQLError
    ProgrammingError = pymysql.ProgrammingError

    def __init__(self):
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

        raise Exception('Conexao read only')

        return False


class MySql:
    """ Mysql
    """

    MySQLError = pymysql.MySQLError
    ProgrammingError = pymysql.ProgrammingError

    def __init__(self):
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
