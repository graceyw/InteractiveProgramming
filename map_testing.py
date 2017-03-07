"""
SoftDes miniproject interactive programming

Noah Rivkin

This file is intended to be used for testing the plotly package without
altering the original file. It is stored on github for purposes of sharing
experiments with Gracey, rather than to be part of the final submission

Some of the code here is extremely similar to example code for plotly, and the
use of sample code from https://plot.ly/python is acknowledged, and credit given
e.i. we are not plaguarizing. If segment of code are exact copies it will be
mentioned in the comments

NOTE: THIS FILE IS NOT INTENDED FOR GRADING
"""

import plotly


globe = [ dict(
        type = 'choropleth',
        locations = ['ATA'], # uses ISO ALPHA-3 codes
        z = [21.71],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
      ) ]

layout = dict(
    title = 'TEST MAP',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
        )
    )
)


fig = dict(data=globe, layout=layout)
plotly.offline.plot(fig, validate=False, filename='test_map.html')