import pandas as pd
import os
import json


def report(json_data, parent_dir):
    with open(os.path.join(parent_dir, 'report.txt'), "w") as file:
        file.write(json.dumps(json_data, indent=4))
    print('Done!')