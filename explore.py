#!/usr/bin/env python
import h5py
import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import pprint

def main():
    args = parse_args()
    explorer = Explorer(args.infile)
    explorer.get_all_info()

def parse_args():
    description = 'explore a snow melt hdf5 file'
    parser = ArgumentParser(description=description)
    parser.add_argument('infile', help='location of input hdf5 file')
    #parser.add_argument('--day', help='day to plot', default=0, type=int)
    return parser.parse_args()

class Explorer(object):

    def __init__(self, filename, data_path = None):
        self.filename = filename
        self.data_path = data_path
        self.read()

    def read(self):
        self.f = h5py.File(self.filename)
        if self.data_path:
            self.data = self.f[self.data_path]
            print "Read dataset with dimensions:", self.data.shape

    def plot_day(self, day):
        plt.imshow(self.data[day, ...].T)
        plt.show()

    def extract_regression_data(self, firstday, lastday):
        data = self.data[firstday:lastday, ...]
        return data.ravel()

    def get_all_info(self):
        def printattributes(attrs, indent=''):
            print indent, 'Attributes:'
            for key, val in attrs.iteritems():
                print indent, key, ':', val
            print ''
        def printinfo(name, obj):
            indent = name.count('/') * '    '
            print indent, name
            indent += '    '
            printattributes(obj.attrs, indent)
        printattributes(self.f.attrs)
        self.f.visititems(printinfo)


if __name__ == '__main__':
    main()
