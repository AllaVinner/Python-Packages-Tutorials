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

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y))
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
fig.update_traces(name = 'My Name', selector=dict(mode='markers'))
#fig.update_layout(template=None)
write_fig_tree(fig, 'sample.json')

fig.show()



