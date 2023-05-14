import plotly.graph_objects as go
from plotly.subplots import make_subplots


import plotly
import plotly.graph_objects as go
import numpy as np
import imageio
import json
from PIL import Image

from scipy.ndimage import gaussian_filter

# Equation of ring cyclide
# see https://en.wikipedia.org/wiki/Dupin_cyclide
import numpy as np
a, b, d = 1.32, 1., 0.8
c = a**2 - b**2
u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]

N = 1000
smoothness = 0.1


theta = np.linspace(0, 2*np.pi, N)
rho = np.linspace(0, 1, N)

disturbance = gaussian_filter(np.random.randn(N), sigma= N*smoothness, mode='wrap')

Rho, Theta = np.meshgrid(rho, theta)
R = Rho*(5+np.cos(4*Theta+2*np.pi/12) + 20*disturbance)

X = R*np.cos(Theta)
Y = R*np.sin(Theta)

Z = np.sin(X) + np.cos(Y/10)*Y


fig = go.Figure()
fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorbar_x=-0.07))
fig.show()

