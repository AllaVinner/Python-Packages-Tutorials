
import h5py
import numpy as np


def create_weather(file_path: str):
    with h5py.File(file_path, 'w') as f:
        f['/temp'] = np.random.random(365)
        f['/temp'].attrs['location'] = 'Tullinge'




if __name__ == '__main__':
    create_weather('weather.h5')










