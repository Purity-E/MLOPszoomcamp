import pickle
import pandas as pd
import numpy as np
import sys

with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)

categorical = ['PUlocationID', 'DOlocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

#creating a function for getting the path
def get_path():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    path = f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02}.parquet'

    return path

def predict(path):
    #reading data
    df = read_data(path)
    #predicting
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    #mean prediction
    print(np.mean(y_pred))


def run():
    path = get_path()
    predict(path)


if __name__ == "__main__":
    run()
