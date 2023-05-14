from typing import List
import math
from scipy.ndimage import gaussian_filter
import plotly
import plotly.graph_objects as go
import numpy as np

##############################################################################
# 1D disturbance
##############################################################################
num_samples = 10000
smoothness = 10

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=gaussian_filter(np.random.randn(num_samples), smoothness, mode='wrap'), # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()



sigmas = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
stds = []
ms = []
for s in sigmas:
    stds.append(np.std(gaussian_filter(np.random.randn(num_samples), s, mode='wrap')))
    ms.append(np.mean(gaussian_filter(np.random.randn(num_samples), s, mode='wrap')))

stds
ms