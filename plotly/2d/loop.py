import plotly
import plotly.graph_objects as go
import numpy as np
import imageio
import json
from PIL import Image

from scipy.ndimage import gaussian_filter

N = 1000
smoothness = 0.1


theta = np.linspace(0, 2*np.pi, N)
disturbance = gaussian_filter(np.random.randn(N), sigma= N*smoothness, mode='wrap')

r = 5+np.cos(4*theta+2*np.pi/12) + 20*disturbance

x = r*np.cos(theta)
y = r*np.sin(theta)

x = np.hstack([x, x[0:1]])
y = np.hstack([y, y[0:1]])


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))


fig.show()
with imageio.get_writer(file_name, mode='I') as writer:
    for fi, fig in enumerate(figs):
        new_fig = plotly.io.from_json(json.dumps(fig.to_plotly_json()))
        print('a')
        new_fig.write_image(temp_file)
        print('b')
        writer.append_data( imageio.imread(temp_file))
        print(f'Finished with figure number: {fi}')





