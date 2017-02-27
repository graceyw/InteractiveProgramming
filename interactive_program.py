"""
SoftDes Mini-project 4
Interactive programing

Noah Rivkin and Gracey Wilson

Visualize data from imf.org to create intersting infographic
"""

import requests
import pickle
import os
import string

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


    def display(self, flags=None):
        """
        procedure to display the country on a map, and what data to display.
        flags include:
        -all     displays all data
        -v       displays only visual, no data
        -debug   displays information to help debug
        others to be added as needed
        """
        # TODO
        pass


    def quit(self, event):
        """
        closes map, and clears data if neccesary
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
    pass


def process_data(data):
    """
    takes data in the raw form and processes it into something we can
    understand and manipulate, divided into relevent sublists or dictionaries
    """
    # TODO
    pass


def insert_data(Map, data):
    """
    takes processed data and inserts it into the Map object, multiple levels
    deep, identifying what data goes where by finding matching strings,
    """
    # TODO
    pass


def visualize(data, category, flag = None):
    """
    takes the processed data and displays the part of the data that is
    in the requested category. Additional options are available with a flag
    """
    # TODO
    pass



import doctest
# main and stuff goes here
