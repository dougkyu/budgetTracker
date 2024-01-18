import sqlite3

class SQLdbAction:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn_object = sqlite3.connect(db_name + '.db')
        self.cursor_object = self.conn_object.cursor()

        self.cursor_object.execute("DROP TABLE IF EXISTS {self.db_name}")

        #TODO Create SQL table
        self.table = """
        
        """

        self.cursor_object.execute(self.table)

        print("Initialized DB and table is created")

        self.conn_object.close()
        
        print("Closing connection object")

