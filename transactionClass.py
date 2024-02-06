import pandas as pd
import datetime as dt
import re

class Transactions:
    def __init__(self, trans_date, description, category, amount):
        self.trans_date = trans_date
        self.description = description
        self.category = category
        self.type = ''
        self.amount = abs(float(amount))

        if re.match('\d\d/\d\d/\d\d\d\d', trans_date):
            dt_obj = dt.datetime.strptime(trans_date, "%m/%d/%Y")
            self.trans_date = dt_obj.strftime("%Y-%m-%d")
        else:
            raise ValueError("Not expecting this date format '{}'. Please have input date format to 'MM/DD/YYYY'".format(trans_date))
        
        #TODO - need to figure out how to branch categories from both AMEX and Chase side
        self.category = ''

        if 'payment' in description.lower() and 'thank you' in description.lower():
            self.type = 'Payment'
        else:
            self.type = 'Sale'

    def __repr__(self):
        return "Transaction('{}', '{}', '{}', '{}', '{}')".format(self.trans_date, self.description, self.category, self.type, self.amount)

    def get_tuple_data(self):
        return (self.trans_date, self.description, self.category, self.amount)