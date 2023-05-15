import plotly
import plotly.graph_objects as go
import numpy as np

##############################################################################
# Plot filled shape
##############################################################################
import plotly
import plotly.graph_objects as go
import numpy as np

##############################################################################
# Plot filled shape
##############################################################################

N = 100
x = np.random.randn(N)
y = np.random.randn(N)

b = 2
x = np.linspace(-b, b, 100)
y = np.linspace(-b, b, 100)

X, Y = np.meshgrid(x, y)

fig = go.Figure()
fig.add_trace(go.Surface(x=X, y=Y, z=np.zeros(X.shape)))
axis_range = 1.15*b
fig.update_layout(
    scene = dict(
        xaxis = dict(visible=False),
        yaxis = dict(visible=False),
        zaxis =dict(visible=True,showticklabels=False, title='')
    )
)

camera = dict(
    up=dict(x=0, y=1, z=0),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0, y=0, z=2)
)
fig.update_layout(scene_camera=camera)
fig.show()




