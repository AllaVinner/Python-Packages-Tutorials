import plotly.graph_objects as go
from plotly.subplots import make_subplots


import plotly
import plotly.graph_objects as go
import numpy as np
import imageio
import json
from PIL import Image

from scipy.ndimage import gaussian_filter
##############################################################################
# Plotly sources
##############################################################################


N = 1000
smoothness = 0.04 


theta = np.linspace(0, 2*np.pi, N)
rho = np.linspace(0, 1, N)

disturbance = gaussian_filter(np.random.randn(N,1), sigma= N*smoothness, mode='wrap')

Rho, Theta = np.meshgrid(rho, theta)
R = Rho*(5+np.cos(5*Theta+2*np.pi/12) + 10*disturbance)

X = R*np.cos(Theta)
Y = R*np.sin(Theta)

Z = np.sin(X) + np.cos(Y/10)*Y


fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Domain', 
                                    'Image'],
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
    eye=dict(x=0, y=0, z=1)
)

camera2 = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1, y=-1, z=0.6)
)


fig.update_layout(scene=dict(camera=camera),
                  scene2=dict(camera=camera2))
fig.update_traces(showscale=False)
fig.update_traces(colorscale=[[0.0, "rgba(26,150,64, 0.7)"], [1, "rgba(26,150,65, 0.7)"]], row=1, col=1)
fig.update_traces(colorscale=a, row=1, col=2)
fig.show()

write_fig_tree(fig, 'sample.json')
