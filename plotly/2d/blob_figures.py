import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.ndimage import gaussian_filter

##############################################################################
# Define Script Paramters
##############################################################################
N = 1000
smoothness = 0.04
blob_radius = 5
blob_num_arms = 5
blob_offset = 2 * np.pi / 12
disturbance_power = 10
z_fun = lambda x, y: np.sin(x) + np.cos(y / 10) * y
axis_range = 11

##############################################################################
# Create Blob
##############################################################################
theta = np.linspace(0, 2 * np.pi, N)
rho = np.linspace(0, 1, N)
disturbance = disturbance_power * gaussian_filter(np.random.randn(N, 1), sigma=N * smoothness, mode='wrap')

Rho, Theta = np.meshgrid(rho, theta)
R = Rho * (blob_radius + np.cos(blob_num_arms * Theta + blob_offset) + disturbance)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

Z = z_fun(X, Y)

##############################################################################
# Create Figures
##############################################################################

fig = make_subplots(rows=2, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}],
                           [{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Original Domain', 'Nonuniform Image',
                                    'Altered Domain', 'Normalized Image']
                    )

Z_zero = np.zeros(X.shape)
fig.add_trace(go.Surface(x=X, y=Y, z=Z_zero, surfacecolor=X + Y), 1, 1)
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=X + Y), 1, 2)
fig.add_trace(go.Surface(x=X, y=Y, z=Z_zero, surfacecolor=X + Y), 2, 1)
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=X + Y), 2, 2)

##############################################################################
# Setting up scene and colors
##############################################################################
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
camera3 = dict(
    up=dict(x=0, y=1, z=0),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0, y=0, z=1)
)

camera4 = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1, y=-1, z=0.6)
)

scene = dict(
    xaxis=dict(visible=False, range=[-axis_range, axis_range]),
    yaxis=dict(visible=False, range=[-axis_range, axis_range]),
    zaxis=dict(visible=True, showticklabels=False, title=''),
    camera=camera
)
scene2 = dict(
    xaxis=dict(visible=True, showticklabels=False, title=''),
    yaxis=dict(visible=True, showticklabels=False, title=''),
    zaxis=dict(visible=True, showticklabels=False, title=''),
    camera=camera2
)
scene3 = dict(
    xaxis=dict(visible=False, range=[-axis_range, axis_range]),
    yaxis=dict(visible=False, range=[-axis_range, axis_range]),
    zaxis=dict(visible=True, showticklabels=False, title=''),
    camera=camera3
)

scene4 = dict(
    xaxis=dict(visible=True, showticklabels=False, title=''),
    yaxis=dict(visible=True, showticklabels=False, title=''),
    zaxis=dict(visible=True, showticklabels=False, title=''),
    camera=camera4
)

##############################################################################
# Color definitions
##############################################################################
alpha_original = [[0.0, "rgba(13,8,135,0.01098694263059318)"],
                  [0.1111111111111111, "rgba(70,3,159,0.029312230751356316)"],
                  [0.2222222222222222, "rgba(114,1,168,0.07585818002124356)"],
                  [0.3333333333333333, "rgba(156,23,158,0.1824255238063563)"],
                  [0.4444444444444444, "rgba(189,55,134,0.37754066879814546)"],
                  [0.5555555555555556, "rgba(216,87,107,0.6224593312018546)"],
                  [0.6666666666666666, "rgba(237,121,83,0.8175744761936437)"],
                  [0.7777777777777778, "rgba(251,159,58,0.9241418199787564)"],
                  [0.8888888888888888, "rgba(253,202,38,0.9706877692486436)"],
                  [1.0, "rgba(240,249,33,0.9890130573694068)"]]

reversed_alpha_original = [[0.0, "rgba(13,8,135,0.9890130573694068)"],
                           [0.1111111111111111, "rgba(70,3,159,0.9706877692486436)"],
                           [0.2222222222222222, "rgba(114,1,168,0.9241418199787564)"],
                           [0.3333333333333333, "rgba(156,23,158,0.8175744761936437)"],
                           [0.4444444444444444, "rgba(189,55,134,0.6224593312018546)"],
                           [0.5555555555555556, "rgba(216,87,107,0.37754066879814546)"],
                           [0.6666666666666666, "rgba(237,121,83,0.1824255238063563)"],
                           [0.7777777777777778, "rgba(251,159,58,0.07585818002124356)"],
                           [0.8888888888888888, "rgba(253,202,38,0.029312230751356316)"],
                           [1.0, "rgba(240,249,33,0.01098694263059318)"]]

fig.update_layout(scene=scene,
                  scene2=scene2,
                  scene3=scene3,
                  scene4=scene4)

fig.update_traces(showscale=False)
# fig.update_traces(colorscale=alpha_original, row=1, col=1)
fig.update_traces(colorscale=alpha_original, row=1, col=2)
fig.update_traces(colorscale=reversed_alpha_original, row=2, col=1)
# fig.update_traces(colorscale=hex_alpha, row=2, col=2)

fig.show()



##############################################################################
# One By one (Change the scene etc)
##############################################################################
fig = go.Figure()
fig.add_trace(go.Surface(x=X, y=Y, z=Z_zero, surfacecolor=X + Y))
fig.update_traces(colorscale=reversed_alpha_original)

fig.update_layout(scene=dict(
    xaxis=dict(visible=False, range=[-axis_range, axis_range]),
    yaxis=dict(visible=False, range=[-axis_range, axis_range]),
    zaxis=dict(visible=True, showticklabels=False, title=''),
    camera = dict(
        up=dict(x=0, y=1, z=0),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=0, y=0, z=1)
    )
))

fig.show()