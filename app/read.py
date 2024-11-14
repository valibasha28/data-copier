# import os
# import pandas as pd
#
# def get_json_reader(BASE_DIR, table_name, chunksize=1000):
#     directory = os.path.join(BASE_DIR.strip(), table_name.strip())
#     file_name = os.listdir(directory)[0]
#     fp = os.path.join(directory, file_name)
#     return pd.read_json(fp, lines=True, chunksize=chunksize)
#
# if __name__ == '__main__':
#     BASE_DIR = os.environ.get('BASE_DIR', '').strip()
#     table_name = os.environ.get('TABLE_NAME', '').strip()
#     json_reader = get_json_reader(BASE_DIR, table_name)
#
#     for idx, df in enumerate(json_reader):
#         print(f'Number of records in chunks with index {idx} is {df.shape[0]}')

import os
import pandas as pd


def get_json_reader(BASE_DIR, table_name, chunksize=1000):
    # Use os.path.join and strip spaces from BASE_DIR and table_name
    directory = os.path.join(BASE_DIR.strip(), table_name.strip())

    # Check if the directory exists
    if not os.path.isdir(directory):
        raise FileNotFoundError(
            f"The directory '{directory}' does not exist. Please check the BASE_DIR and table_name.")

    # List files in the directory
    files = os.listdir(directory)
    if not files:
        raise FileNotFoundError(f"No files found in the directory '{directory}'.")

    file_name = files[0]
    fp = os.path.join(directory, file_name)
    return pd.read_json(fp, lines=True, chunksize=chunksize)


if __name__ == '__main__':
    # Fetch environment variables and strip any leading/trailing spaces
    BASE_DIR = os.environ.get('BASE_DIR', '').strip()
    table_name = os.environ.get('TABLE_NAME', '').strip()

    # Check if BASE_DIR and table_name are set correctly
    if not BASE_DIR or not table_name:
        print("Error: BASE_DIR and TABLE_NAME environment variables must be set.")
    else:
        try:
            json_reader = get_json_reader(BASE_DIR, table_name)

            for idx, df in enumerate(json_reader):
                print(f'Number of records in chunks with index {idx} is {df.shape[0]}')
        except FileNotFoundError as e:
            print(e)