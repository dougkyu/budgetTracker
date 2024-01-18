import os
import argparse
import pandas as pd
from excelTransactionsAccess import ExcelTransactions
from transactionClass import Transactions

def main():
    #enable argument parsers
    parser = argparse.ArgumentParser(
            prog='budgetTrackerMain',
            description='Program helps to track transactions and budgeting'
    )
    parser.add_argument('-p', '--plaid', action='store_true')
    parser.add_argument('-e', '--excel', action='store_true')
    args = parser.parse_args()
    if args.plaid == True and args.excel == True:
        raise Exception('Both -p and -e flags are enabled. Please enable only one')
    
    #define user
    user = 'dougyu'


    #access bank information (two options: Plaid API or using excel sheets)
    if args.excel == True:
        user_transactions = ExcelTransactions(user)
        user_transactions.find_transactions_files_list()
        transaction_file_list = user_transactions.get_transactions_files_list()

        transaction_df_list = []
        for transaction_file in transaction_file_list:
            pd_dataframe = user_transactions.get_transaction_data(transaction_file)
            #Important transaction columns: Transaction Date, Desciption, Category, Type, Amount
            
            for ct, elem in pd_dataframe.iterrows():
                trans_class = Transactions(elem['Transaction Date'], elem['Description'], elem['Category'], elem['Amount'])
                transaction_df_list.append(trans_class)
        print(transaction_df_list)




if __name__ == "__main__":
    main()


