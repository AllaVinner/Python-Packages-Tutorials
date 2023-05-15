##############################################################################
# Plotly sources
##############################################################################
# Properties
# https://plotly.com/python/reference/layout/xaxis/
# Classes
#https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Heatmap.html

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
R = Rho*(5+np.cos(4*Theta+2*np.pi/12) + 40*disturbance)

X = R*np.cos(Theta)
Y = R*np.sin(Theta)

Z = np.sin(X) + np.cos(Y/10)*Y


fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
                    )
fig.add_trace(go.Surface(x=X, y=Y, z=np.zeros(X.shape), surfacecolor=X+Y), 1, 1)
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=X+Y), 1, 2)

axis_range = 10
fig.update_layout(
    scene = dict(
        xaxis = dict(visible=False, range=[-axis_range, axis_range]),
        yaxis = dict(visible=False, range=[-axis_range, axis_range]),
        zaxis =dict(visible=True,showticklabels=False, title='')
    ),
    scene2 = dict(
        xaxis = dict(visible=True,showticklabels=False, title=''),
        yaxis = dict(visible=True,showticklabels=False, title=''),
        zaxis =dict(visible=True,showticklabels=False, title='')
    )
)

camera = dict(
    up=dict(x=0, y=1, z=0),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0, y=0, z=2)
)

fig.update_layout(scene_camera=camera, title='name')
fig.show()

fig.layout.scene2

