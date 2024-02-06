import sqlite3

class SQLdbAction:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = db_name + '.db'
        conn_object = sqlite3.connect(self.db_file)
        cursor_object = conn_object.cursor()

        cursor_object.execute("DROP TABLE IF EXISTS {db_name}".format(db_name=db_name))

        #TODO Create SQL table
        self.table = """
            CREATE TABLE {db_name} (
            Transaction_Date DATE NOT NULL,
            Description VARCHAR(255) NOT NULL,
            Category VARCHAR(30) NOT NULL,
            Amount NUMERIC NOT NULL
        );""".format(db_name=db_name)

        print("Initialized DB and table is created")
        cursor_object.execute(self.table)

        print("Closing connection object")
        conn_object.close()

    
    def insert_transaction_data(self, transaction_inst):
        """
        @param: transaction_inst (class <Transactions>)
        """
        pass
    
    def insert_transaction_list(self, transaction_df_list):
        conn_object = sqlite3.connect(self.db_file)
        cursor_object = conn_object.cursor()

        for transaction in transaction_df_list:
            print(transaction.get_tuple_data())
            conn_object.execute(
                "INSERT INTO {db_name} (Transaction_Date, Description, Category, Amount) VALUES (?,?,?,?)".format(db_name=self.db_name), (transaction.trans_date, transaction.description, transaction.category, transaction.amount))
        conn_object.commit()
        conn_object.close()

    def fetch_data(self, query):
        conn_object = sqlite3.connect(self.db_file)
        cursor_object = conn_object.cursor()
        cursor_object.execute(query)
        output = cursor_object.fetchall()

        conn_object.commit()
        conn_object.close()
        
        return output