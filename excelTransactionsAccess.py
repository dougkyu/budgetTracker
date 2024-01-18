import os
import pandas as pd

class ExcelTransactions:
    def __init__(self, user):
        self.user = user
        self.transaction_files_list = None
        self.path = os.path.join(os.getcwd(), 'transactions', user)
    
    def find_transactions_files_list(self):
        transaction_files_list = os.listdir(self.path)
        self.transaction_files_list = transaction_files_list

    #Input: transaction file path (.csv)
    #Output: A Pandas data frame with the transaction data from csv file (pd)
    def get_transaction_data(self, transaction_file):
        transaction_file_path = os.path.join(self.path, transaction_file)
        df = pd.read_csv(transaction_file_path)
        return df

    def get_transactions_files_list(self):
        return self.transaction_files_list

if __name__ == "__main__":
    pass