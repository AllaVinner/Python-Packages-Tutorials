import plotly
import plotly.graph_objects as go
import numpy as np

##############################################################################
# Plot filled shape
##############################################################################



N = 1000

theta = np.linspace(0, 2*np.pi, N)
r = 5+np.cos(4*theta+2*np.pi/12)

window_size = int(19)
disturbance_sample = np.random.randn(N)


for _ in range(10):
    disturbance_sample = np.hstack([disturbance_sample[-int(window_size/2):], disturbance_sample, disturbance_sample[0: int(window_size/2)]])
    disturbance_sample = np.convolve(disturbance_sample, np.ones(window_size)/window_size, mode='valid')

disturbance = disturbance_sample

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=disturbance, # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()



r = r + 3*disturbance

x = r*np.cos(theta)
y = r*np.sin(theta)


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()





