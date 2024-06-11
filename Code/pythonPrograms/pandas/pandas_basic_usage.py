import pandas as pd
import numpy as np
import time


def get_dataset(size):
    # Create Fake Dataset
    df = pd.DataFrame()
    df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['team'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win'] = np.random.choice(['yes', 'no'], size)
    dates = pd.date_range('2020-01-01', '2022-12-31')
    df['date'] = np.random.choice(dates, size)
    df['prob'] = np.random.uniform(0, 1, size)
    return df


def set_dtypes(df):
    df['size'] = df['size'].astype('category')
    df['team'] = df['team'].astype('category')
    df['age'] = df['age'].astype('int16')
    df['win'] = df['win'].map({'yes': True, 'no': False})
    df['prob'] = df['prob'].astype('float32')
    return df


"""
CSV
"""
output_folder = 'file_test_folder/pandas/'
print('Reading and writing CSV')
df = get_dataset(5_000_000)
df = set_dtypes(df)

start_time = time.time()
df.to_csv(output_folder + 'test.csv')
end_time = time.time()
print(f"Function 'to_csv' took {end_time - start_time} seconds to execute.")

start_time = time.time()
df_csv = pd.read_csv(output_folder + 'test.csv')
end_time = time.time()
print(f"Function 'read_csv' took {end_time - start_time} seconds to execute.")

"""
Pickle
"""

print('Reading and writing Pickle')
df = get_dataset(5_000_000)
df = set_dtypes(df)

start_time = time.time()
df.to_pickle(output_folder + 'test.pickle')
end_time = time.time()
print(f"Function 'to_pickle' took {end_time - start_time} seconds to execute.")

start_time = time.time()
df_pickle = pd.read_pickle(output_folder + 'test.pickle')
end_time = time.time()
print(f"Function 'read_pickle' took {
      end_time - start_time} seconds to execute.")

"""
Parquet
"""
print('Reading and writing Parquet')
df = get_dataset(5_000_000)
df = set_dtypes(df)

start_time = time.time()
df.to_parquet(output_folder+'test.parquet')
end_time = time.time()
print(f"Function 'to_parquet' took {
      end_time - start_time} seconds to execute.")

start_time = time.time()
df_parquet = pd.read_parquet(output_folder+'test.parquet')
end_time = time.time()
print(f"Function 'read_parquet' took {
      end_time - start_time} seconds to execute.")

"""
Feather
"""
print('Reading and writing Feather')
df = get_dataset(5_000_000)
df = set_dtypes(df)

start_time = time.time()
df.to_feather(output_folder+'test.feather')
end_time = time.time()
print(f"Function 'to_feather' took {
      end_time - start_time} seconds to execute.")

start_time = time.time()
df_feather = pd.read_feather(output_folder+'test.feather')
end_time = time.time()
print(f"Function 'read_feather' took {
      end_time - start_time} seconds to execute.")
