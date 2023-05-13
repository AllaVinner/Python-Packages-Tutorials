import plotly
import plotly.graph_objects as go
import numpy as np

##############################################################################
# 1D disturbance
##############################################################################



num_samples = 1000
# invs
shortterm_variance = 100
longterm_variance = 20



window_size = int(2*longterm_variance+1)
disturbance_sample = np.random.randn(num_samples)

for _ in range(shortterm_variance):
    disturbance_sample = np.hstack([disturbance_sample[-int(window_size/2):], disturbance_sample, disturbance_sample[0: int(window_size/2)]])
    disturbance_sample = np.convolve(disturbance_sample, np.ones(window_size)/window_size, mode='valid')

disturbance = disturbance_sample

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=disturbance, # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()