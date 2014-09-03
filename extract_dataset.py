#!/usr/bin/env python
import h5py
import numpy as np
import pandas as pd
from argparse import ArgumentParser
import yaml
from explore import Explorer
from collections import OrderedDict


def main():
    args = parse_args()
    extractor = Extractor(args.config)
    extractor.run()


def parse_args():
    description = 'extract dataset from a set of input files'
    parser = ArgumentParser(description=description)
    parser.add_argument('config', help='YAML file describing how to extract data')
    return parser.parse_args()


class Extractor(object):

    def __init__(self, config):
        self.config = yaml.load(open(config))
        self.datadict = OrderedDict()

    def run(self):
        for filename, features in self.config['files'].iteritems():
            for path, details in features['datasets'].iteritems():
                explorer = Explorer(filename, path)
                self.extract_feature(explorer, details)

        df = pd.DataFrame(self.datadict)
        df.to_csv(self.config['outfile'], index=False)

    def extract_feature(self, explorer, details):
        name = details['name']
        firstday = self.config['firstday']
        lastday = self.config['lastday']
        dayoffset = self.config['files'][explorer.filename]['dayoffset']
        start = firstday + dayoffset
        end = lastday + dayoffset

        if self.config['mode'] == 'time_series':
            if details['aggregation'] == 'all':
                # Extract the data set for each day of the time series
                # as a separate feature.
                for day in range(firstday, lastday + 1):
                    data = explorer.extract_slice(day + dayoffset)
                    self.datadict["{0}.{1}".format(name, day)] = data
            elif details['aggregation'] == 'mean':
                data = explorer.extract_aggregate_data(start, end, np.mean)
                self.datadict[name + '_mean'] = data
        else:
            data = explorer.extract_regression_data(start, end)
            self.datadict[name] = data



if __name__ == '__main__':
    main()
