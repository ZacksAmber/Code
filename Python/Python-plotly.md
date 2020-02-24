---
title: Python plotly
date: 2020-02-22 22:04:39
tags:
mathjax: true
hidden: true
---

> [Getting Started with Plotly in Python](https://plot.ly/python/getting-started/)
> [Plotly Express in Python](https://plot.ly/python/plotly-express/)
> [Plotly Python Open Source Graphing Library Basic Charts](https://plot.ly/python/basic-charts/)
> 

## Overview
> [Getting Started with Plotly in Python](https://plot.ly/python/getting-started/)

The plotly Python library ([plotly.py](https://plot.ly/python/)) is an interactive, [open-source](https://github.com/plotly/plotly.py) plotting library that supports over 40 unique chart types covering a wide range of statistical, financial, geographic, scientific, and 3-dimensional use-cases.

---

### Installation & Loading
1. [Download Anaconda Environment](https://www.anaconda.com/distribution/), otherwise you will not have package `pandas` and `numpy`.
2. Download package `plotly` through `conda`. If you never heard pip, [click here](https://zacks.one/2019/06/16/Python-Tutorial/#18).
```shell Shell
conda install -c plotly "plotly>=4.5.1"
```

---

### JupyterLab Support (Python 3.5+)
For use in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), install the `jupyterlab` and `ipywidgets` packages using pip...

```sh Shell
conda update --all

conda install "ipywidgets>=7.5"
```

Then run the following commands to install the required JupyterLab extensions (note that this will require `node` to be installed):

```shell Shell
node --version
```

For Mac OS only:
If it shows `command not found: node`, you should install `node` first:

```sh Shell
conda install -c conda-forge nodejs
conda install -c conda-forge yarn
```

For Mac OS only:
Then run the following commands to install the required JupyterLab extensions (note that this will require node to be installed):
```sh Shell
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.5.1 --no-build
jupyter labextension install @jupyterlab/plotly-extension --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.5.1 --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build

# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
```

```sh Shell
jupyter lab
```

```py Python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()
```

![](https://raw.githubusercontent.com/ZacksAmber/PicGo/master/img/20200223061922.png)

See [Displaying Figures in Python](https://plot.ly/python/renderers/) for more information on the renderers framework, and see [Plotly FigureWidget Overview](https://plot.ly/python/figurewidget/) for more information on using `FigureWidget`.

---

### Static Image Export Support
plotly.py supports static image export using the `to_image` and `write_image` functions in the `plotly.io` package. This functionality requires the installation of the plotly [orca](https://github.com/plotly/orca) command line utility and the `psutil` and `requests` Python packages.

Note: The requests library is used to communicate between the Python process and a local orca server process, it is not used to communicate with any external services.

These dependencies can all be installed using conda:

```sh Shell
conda install -c plotly plotly-orca psutil requests
```

These packages contain everything you need to save figures as static images.

```py Python
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig.write_image('figure.png')
```

![](https://raw.githubusercontent.com/ZacksAmber/PicGo/master/img/20200223062744.png)

See [Static Image Export in Python](https://plot.ly/python/static-image-export/) for more information on static image export.

---

### Extended Geo Support
Some plotly.py features rely on fairly large geographic shape files. The county choropleth figure factory is one such example. These shape files are distributed as a separate plotly-geo package. This package can be installed using conda.

```sh Shell
conda install -c plotly plotly-geo
```

See [USA County Choropleth Maps in Python](https://plot.ly/python/county-choropleth/) for more information on the county choropleth figure factory.

---

### Chart Studio Support
The `chart-studio` package can be used to upload plotly figures to Plotly's Chart Studio Cloud or On-Prem services. This package can be installed using conda.

```sh Shell
conda install -c plotly chart-studio
```

Note: This package is optional, and if it is not installed it is not possible for figures to be uploaded to the Chart Studio cloud service.

---

## Plotly Express
### Introduction
Plotly Express is a terse, consistent, high-level API for rapid data exploration and figure generation.

