"""
SoftDes Mini-project 4
Interactive programing

Noah Rivkin and Gracey Wilson

Visualize data from imf.org to create intersting infographic
"""

import requests
import pickle
import os

class Dataset:
    """
    contains a set of data regarding a particular topic. self.data_num contains
    the number of entries in each 'row' of the dataset.
    """
    def __init__(self, name = 'Default', data_num = 1, data = []):
        self.name = name
        self.data_num = data_num
        self.data = data


def get_data():
    """
    pulls data from web or, if it already is locally available, accesses
    the apropriate file
    """
    pass


def process_data(data):
    """
    takes data in the raw form and processes it into something we can
    understand and manipulate, divided into relevent sublists or dictionaries
    """
    pass


def visualize(data, category, flag = None):
    """
    takes the processed data and displays the part of the data that is
    in the requested category. Additional options are available with a flag
    """
    pass