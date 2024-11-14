# import pandas as pd
# from read import dummy

import os
import sys
from read import get_json_reader
from write import load_db_table

def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])

def main():
    # The file name is hardcoded and assigned to fp.
    # fp = r"C:\Users\BASHA\Research\data\retail_db_json\order_items\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e"
    # df = pd.read_json(fp, lines=True)
    # print(df.count())
    # print(df.describe())
    # print(df.columns)
    # print(df.dtypes)
    # print(df[['order_item_order_id', 'order_item_subtotal']])
    # print(df[df['order_item_order_id'] == 2])
    # print('Hello from APP file')
    # DB_NAME = os.environ.get('DB_NAME')
    # print(f'Hello from {DB_NAME}')

    BASE_DIR = os.environ.get('BASE_DIR', '').strip()
    table_names = sys.argv[1].split(',')

    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)

if __name__ == '__main__':
    main()