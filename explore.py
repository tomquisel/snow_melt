#!/usr/bin/env python
import h5py
import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt

def main():
    args = parse_args()
    explorer = Explorer(args.infile)
    explorer.plot_day(args.day)

def parse_args():
    description = 'test reading in hdf5 files'
    parser = ArgumentParser(description=description)
    parser.add_argument('infile', help='location of input hdf5 file')
    parser.add_argument('--day', help='day to plot', default=0, type=int)
    return parser.parse_args()

class Explorer(object):

    def __init__(self, filename, data_path):
        self.filename = filename
        self.data_path = data_path
        self.read()

    def read(self):
        f = h5py.File(self.filename)
        self.data = f[self.data_path]
        print "Read file with dimensions:", self.data.shape

    def plot_day(self, day):
        plt.imshow(self.data[day, ...].T)
        plt.show()

    def extract_regression_data(self, firstday, lastday):
        data = self.data[firstday:lastday, ...]
        return data.ravel()

if __name__ == '__main__':
    main()
