import os
import json
import logging
import pandas as pd
import numpy as np


def report(json_data, parent_dir):

    # text file for safety
    with open(os.path.join(parent_dir, 'report.txt'), "w") as file:
        file.write(json.dumps(json_data, indent=4))
    logging.info(f'Text report created at {parent_dir}')
    
    dfs = []

    for name, data in json_data.items():
        array = np.array([[k] + (list(v.values())) for k,v in data.items()])
        columns = list(list(data.values())[0].keys())
        df = pd.DataFrame(array, columns=['question'] + columns)
        
        df['name'] = name
        
        cols = list(df.columns[-1:]) + list(df.columns[:-1])
        df = df[cols]
        dfs.append(df)

    df = dfs[0]
    for i in range(1, len(dfs)):
        df = df.append(dfs[i])

    df.reset_index(inplace=True)
    df.drop(axis=1, labels='index', inplace=True)

    df['errors'] = df['errors'].apply(lambda n: ' | '.join(n))

    report_path = os.path.join(parent_dir, 'Lab Report.xlsx')
    
    with pd.ExcelWriter(report_path) as writer:
        df.to_excel(writer, sheet_name='data')
        # df2.to_excel(writer, sheet_name='analysis')

