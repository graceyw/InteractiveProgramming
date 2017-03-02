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

class Dataset:
    """
    contains a set of data regarding a particular topic. self.data_num contains
    the number of keys in the dataset.
    """
    def __init__(self, name = 'Default', data = {}):
        self.name = name
        self.data_num = len(data)
        self.data = data


class Location:
    """
    contains the information describing a country or locale, specifically the
    information from imf.org, and the graphical description of the location
    """
    def __init__(self, name = 'Default', visual = None, info = Dataset()):
        self.name = name
        self.visual = visual
        self.info = info


class Map():
    """
    contains all locations, is used to access everything conveniently.
    is called in visualize. locations holds set or list or something containing
    Location objects
    """
    def __init__(self, locations = None):
        self.locations = locations
        self.optionbar = Option_bar(locations)
        self.layout = dict(
            title = 'Gender Equality Map',
            geo = dict(
                showframe = False,
                showcoastlines = True,
                projection = dict(
                    type = 'Mercator'
                )
            )
        )


    def display(self, flags=None):
        """
        procedure to display the country on a map, and what data to display.
        flags include:
        -all     displays all data
        -v       displays only visual, no data
        -debug   displays information to help debug
        the default is based on the option bar
        others to be added as needed
        """
        # brings data up from inside locations, and uses country_code_dict to interpret names to locations
        codes = []
        names = []
        for location in self.locations:
            names.append(location.name)
            if location.name in country_code_dict:
                codes.append(country_code_dict[location.name])
        if '-v' in flags:
            return [ dict(
                    type = 'choropleth',
                    locations = codes, # uses ISO ALPHA-3 codes
                    text = names,
                    z = [21.71],
                    colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
                  ) ]
        else:
            return [ dict(
                type = 'choropleth',
                locations = codes, # uses ISO ALPHA-3 codes
                text = names,
                z = [21.71], # will be replaced by something from location.info
                colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
              ) ]


    def quit(self, event):
        """
        closes map
        """
        # TODO
        pass


class Option_bar:
    """
    optionbar to be displayed, that allows interaction with map. Includes
    checkboxes, and possibly other stuff telling map how to display its data
    """
    def __init__(self, locations):
        """
        taked data from inside locations to figure out what options it should
        generate
        """
        # TODO
        pass


    def update(self, event):
        """
        updates display when the options selected on the option bar change
        """
        # TODO
        pass


def get_data(file_name = 'GENDER_EQUALITY_01-17-2017 15-09-24-32_timeSeries.csv'):
    """
    pulls data from web or, if it already is locally available, accesses
    the apropriate file
    """
    raw_data = []
    f = open(file_name, 'r')
    lines = f.readlines()
    lines = lines[1:]  # cuts out the line with column titles
    f.close
    return lines


def process_data(raw_data):
    """
    takes data in the raw form and processes it into something we can
    understand and manipulate, divided into relevent sublists or dictionaries
    """
    data = {}
    for line in raw_data:
        line = line.replace(', ', '-;')
        line = line.split(',')
        line[0] = line[0].replace('-;', ', ')
        key = line.pop(0)                         # pop grabs one value from list
        key = key.strip(string.punctuation)
        if key in data:
            data[key].append(line)
        else:
            data[key] = [line]
    return data


def insert_data(Map, data):                                     # GRACEY
    """
    takes processed data and inserts it into the Map object, multiple levels
    deep, identifying what data goes where by finding matching strings,
    """
    # TODO
    pass


def visualize(data, category, flag = None):                    # NOAH
    """
    takes the processed data and displays the part of the data that is
    in the requested category. Additional options are available with a flag
    """
    # globe = insert_data(globe, data) # inserts data into the map object
    # currently using the -v flag because data is not yet inserted
    # temporary for testing until insert data is written, only adds location
    locations = []
    for key in data:
        location = Location(key)
        locations.append(location)
    globe = Map(locations)
    return dict(data = globe.display(['-v']), layout = globe.layout)
    pass


def make_code_dict(country_codes):
    """
    creates a dictionary mapping country names to their ISO ALPHA-3 codes
    """
    for line in country_codes:
        line = line.replace(', ', '-;')
        line = line.split(',')
        line[0] = line[0].replace('-;', ', ')
        if line[0] not in country_code_dict:
            country_code_dict[line[0]] = line[2]


import doctest
# main and stuff goes here
if __name__ == '__main__':
    raw_data = get_data()
    country_codes = get_data('country_codes.csv')
    country_code_dict = {}
    make_code_dict(country_codes)
    data = process_data(raw_data)
    print(data['Armenia, Republic of']) # display for debugging
    fig = visualize(data, 'test') # should eventually go in map.display() method
    plotly.offline.plot(fig, validate=False, filename='GlobalGenderEqualityMapping.html')
