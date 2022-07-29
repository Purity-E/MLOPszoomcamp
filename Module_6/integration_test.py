import pandas as pd
from datetime import datetime
import batch
import os

# creating dataframe
def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

data = [
(None, None, dt(1, 2), dt(1, 10)),
(1, 1, dt(1, 2), dt(1, 10)),
(1, 1, dt(1, 2, 0), dt(1, 2, 50)),
(1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
]

columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
df_input = pd.DataFrame(data, columns=columns)

# defining input file path
input_file = batch.get_input_path(2021, 1)
#input_file = os.getenv('INPUT_FILE_PATTERN')

options = {
    'client_kwargs': {
        'endpoint_url': 'http://localhost:4566'
    }
}

# saving dataframe
df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)
# saving data

# running batch.py for January 2021
os.system('python batch.py 2021 1')

# reading output file
output_file = batch.get_output_path(2021, 1)

df_result = batch.read_data(output_file)
print(df_result['predicted_duration'].sum())