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

    def get_layout(self):
        years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998',\
                 '1999','2000','2001','2002','2003','2004','2005','2006','2007',\
                 '2008','2009','2010','2011','2012','2013']
        year_buttons = []
        indexes = {}
        ex_location = self.locations[0]
        dtypes = [ex_location.info.dtype]
        title = ''
        if dtypes[0] == 'GE_GII':
            title_ = 'Gender Inequality Map'
        elif dtypes[0] == 'GE_GDI':
            title_ = 'Gender Development Map'
        for year in years:
            index = []
            for dtype in dtypes:
                for location in self.locations:
                    index.append(location.info.data[year])
            indexes[year] = index
        for i in range(len(years)):
            blank = [False] * len(years)
            blank.pop(i)
            blank.insert(i, True)
            year_buttons.append(dict(
                args = ['visible', blank],
                label = years[i],
                method = 'restyle'
            ))
        layout = dict(
            updatemenus = [
                dict(
                    x = .1,
                    y = .95,
                    buttons = list(year_buttons),
                    yanchor = 'top'
                )
            ],
            title = title_,
            geo = dict(
                showframe = False,
                showcoastlines = True,
                projection = dict(
                    type = 'Mercator'
                )
            )
        )
        return layout

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
        years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998',\
                 '1999','2000','2001','2002','2003','2004','2005','2006','2007',\
                 '2008','2009','2010','2011','2012','2013']
        for location in self.locations:
            names.append(location.name) # edit to add more data
            codes.append(location.info.code)
        indexes = {}
        dtypes = ['gei']
        for year in years:
            index = []
            for dtype in dtypes:
                for location in self.locations:
                    #if location.info.dtype == dtype:
                    index.append(location.info.data[year])
                indexes[year] = index
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
            data = []
            for year in years:
                for dtype in dtypes:
                    data.append(dict(
                    type = 'choropleth',
                    locations = codes, # uses ISO ALPHA-3 codes
                    text = names,
                    itype = dtype,
                    z = indexes[year],
                    colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
                    ))
            return data


def insert_data(globe, data, index):
    """
    takes processed data and inserts it into the Map object, multiple levels
    deep, identifying what data goes where by finding matching strings.
    globe.location[n].data would contain data for n
    """
    # for location in map.location, find corresponding row. just performs operations, doesn't return.
    globe.locations = []
    for i, row in data.iterrows():
        if row.loc['Indicator Code'] == index:
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
    insert_data(globe,data,category)
    return dict(data = globe.display(), layout = globe.get_layout())


import doctest
if __name__ == '__main__':
    data = pd.read_csv('./GENDER_EQUALITY_01-17-2017 15-09-24-32_timeSeries.csv')
    country_code_data = pd.read_csv('./country_codes.csv')
    data = country_code_data.merge(data, left_on='English short name lower case', right_on="Country Name")
    fig = visualize(data, 'GE_GII')
    fig2 = visualize(data, 'GE_GDI')
    plotly.offline.plot(fig, validate=False, filename='GlobalGenderInequalityMapping.html')
    plotly.offline.plot(fig2, validate=False, filename='GlobalGenderDevelopment.html')
