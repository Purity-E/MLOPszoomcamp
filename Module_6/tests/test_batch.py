import batch
import pandas as pd
from datetime import datetime
from pandas.testing import assert_frame_equal

def test_prepare_data():

    def dt(hour, minute, second=0):
        return datetime(2021, 1, 1, hour, minute, second)

    data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
]

    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
    df = pd.DataFrame(data, columns=columns)

    actual_df = batch.prepare_data(df, ['PUlocationID', 'DOlocationID'])

    # defining expected
    expected_data = [
        ('-1','-1',dt(1, 2), dt(1, 10), 8.0),
        ('1', '1', dt(1, 2), dt(1, 10), 8.0)
        ]

    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime', 'duration']
    expected_df = pd.DataFrame(expected_data, columns=columns)

    #comparing expected vs actual
    assert_frame_equal(actual_df, expected_df)

