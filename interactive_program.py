"""
Software Design Spring 2017
Mini Project 4: Interactive Programing
Noah Rivkin & Gracey Wilson

Visualize data from imf.org to create interesting interactive infographic

NOTE: REQUIRES PLOTLY PACKAGE
to install plotly library run:

$ sudo pip3 install plotly
$ sudo pip3 install plotly --upgrade

"""

import requests
import pickle
import os
import string
import plotly
import pandas as pd
import colorlover as cl

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

class Dataset:
    """
    contains a set of data regarding a particular topic. self.data_num contains
    the number of keys in the dataset.
    """
    def __init__(self, code = '', data = [], dtype = ''):
        self.code = code
        self.data = data
        self.dtype = dtype

    def make_dict():
        """
        takes data and years and makes it into a dictionary
        """
        years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998',\
                 '1999','2000','2001','2002','2003','2004','2005','2006','2007',\
                 '2008','2009','2010','2011','2012','2013']
        d_new = {}
        for i in range(len(years)):
            d_new[years[i]] = self.data[i]
        self.data = d_new

class Location:
    """
    contains the information describing a country or locale, specifically the
    information from imf.org, and the graphical description of the location
    """
    def __init__(self, name = 'Default', info = Dataset()):
        self.name = name
        self.info = info


class Map():
    """
    contains all locations, is used to access everything conveniently.
    is called in visualize. locations holds set or list or something containing
    Location objects
    """
    def __init__(self, locations = None):
        self.locations = locations
        years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998',\
                 '1999','2000','2001','2002','2003','2004','2005','2006','2007',\
                 '2008','2009','2010','2011','2012','2013']
        year_buttons = []
        for year in years:
            year_buttons.append(dict(
                args = [year],
                label = year,
                method = 'restyle'
            ))
        self.layout = dict(
            updatemenus = [
                dict(
                    x = .1,
                    y = 1,
                    buttons = list([
                        dict(
                            args = ['gdi'],
                            label = 'Gender Development Index',
                            method = 'restyle'
                        ),
                        dict(
                            args = ['gei'],
                            label = 'Gender Equality Index',
                            method = 'restyle'
                        )
                    ]),
                    yanchor = 'top'
                ),
                dict(
                    x = .1,
                    y = .95,
                    buttons = list(year_buttons),
                    yanchor = 'top'
                )
            ],
            title = 'Gender Equality Map',
            geo = dict(
                showframe = False,
                showcoastlines = True,
                projection = dict(
                    type = 'Mercator'
                )
            )
        )

    def display(self, flags=[]):
        """
        procedure to display the country on a map, and what data to display.
        flags include:
        -all     displays all data
        -v       displays only visual, no data
        -debug   displays information to help debug
        the default is based on the option bar
        others to be added as needed
        """
        # brings data up from inside locations
        codes = []
        names = []
        index = []
        for location in self.locations:
           names.append(location.name)
           codes.append(location.info.code)
           index.append(location.info.data['2000'])
        if '-v' in flags:
            return [ dict(
                    type = 'choropleth',
                    locations = codes, # uses ISO ALPHA-3 codes
                    text = names,
                    z = [1],
                    # colorscale taken from online example
                    colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
                  ) ]
        else:
            return [ dict(
                type = 'choropleth',
                locations = codes, # uses ISO ALPHA-3 codes
                text = names,
                z = index,
                colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
              ) ]




def insert_data(globe, data):
    """
    takes processed data and inserts it into the Map object, multiple levels
    deep, identifying what data goes where by finding matching strings.
    globe.location[n].data would contain data for n
    """
    # for location in map.location, find corresponding row. just performs operations, doesn't return.
    globe.locations = []
    for i, row in data.iterrows():
        locale = Location(name=row.loc['English short name lower case'], \
                          info = Dataset(code = row.loc['Alpha-3 code'], \
                                         data = row.loc['1990':'2013'], \
                                         dtype = row.loc['Indicator Code'] ))
        locale.info.make_dict
        globe.locations.append(locale)

def visualize(data, category, flag = None):
    """
    takes the processed data and displays the part of the data that is
    in the requested category. Additional options are available with a flag
    """
    # globe = insert_data(globe, data) # inserts data into the map object
    locations = data['English short name lower case']
    globe = Map()
    insert_data(globe,data)
    return dict(data = globe.display(), layout = globe.layout)




import doctest
if __name__ == '__main__':
    data = pd.read_csv('./GENDER_EQUALITY_01-17-2017 15-09-24-32_timeSeries.csv')
    country_code_data = pd.read_csv('./country_codes.csv')
    data = country_code_data.merge(data, left_on='English short name lower case', right_on="Country Name")
    fig = visualize(data, 'test') # should eventually go in map.display() method
    plotly.offline.plot(fig, validate=False, filename='GlobalGenderEqualityMapping.html')
