# Source: https://twiki.cern.ch/twiki/pub/Sandbox/JaredDavidLittleSandbox/PythonandHDF5.pdf
# Next Section: Chapter 2 - Getting Started
import h5py
import numpy as np


def create_weather(file_path: str):
    with h5py.File(file_path, 'w') as f:
        f['/temp'] = np.random.random(365)
        f['/temp'].attrs['location'] = 'Tullinge'


def investigate_h5ad_file(file_path: str, dataset_path: str):
    with h5py.File(file_path, 'r') as f:
        for k, v  in f[dataset_path].attrs.items():
            print(f"{k}: '{v}'")



def subsetting_datasets(file_path: str, dataset_path: str):
    # H5DF files can subset the data without reading it all into memory
    with h5py.File(file_path, 'r') as f:
        loaded_data = f[dataset_path][0:10]
        print('Loaded data', loaded_data)


def creating_sparse_dataset(file_path: str):
    with h5py.File(file_path, 'w') as f:
        big_dataset = f.create_dataset('big', shape=(10, 10, 10, 10), dtype='float32')
        big_dataset[1, 1, 1, 1] = 3.14


def investigate_sparse_dataset(file_path: str, dataset_path):
    with h5py.File(file_path, 'r') as f:
        print(f[dataset_path])
        print(f[dataset_path].shape)




if __name__ == '__main__':
    file_path = 'weather.h5'
    #create_weather(file_path)
    #investigate_h5ad_file(file_path, 'temp')
    creating_sparse_dataset('big.h5')
    investigate_sparse_dataset('big.h5', 'big')








