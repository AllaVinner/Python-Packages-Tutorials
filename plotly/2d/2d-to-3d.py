import plotly.graph_objects as go
from plotly.subplots import make_subplots


import plotly
import plotly.graph_objects as go
import numpy as np
import imageio
import json
from PIL import Image

from scipy.ndimage import gaussian_filter
import numpy as np

##############################################################################
# Generate data
##############################################################################

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

r = (5+np.cos(4*theta+2*np.pi/12) + 20*disturbance)
x = r*np.cos(theta)
y = r*np.sin(theta)


fig = go.Figure()
fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorbar_x=-0.07))
fig.show()



fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': False}, {'is_3d': True}]],
                    subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
                    )
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=X+Y), 1, 2)
fig.update_layout(title_text="Ring cyclide")
fig.show()


fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
                    )
fig.add_trace(go.Surface(x=X, y=Y, z=np.zeros(X.shape), surfacecolor=X+Y), 1, 1)
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=X+Y), 1, 2)
fig.update_layout(title_text="Ring cyclide")
fig.show()




##############################################################################
# 2d domain
##############################################################################
