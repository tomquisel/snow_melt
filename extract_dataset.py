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

    def run(self):
        datadict = OrderedDict()
        firstday = self.config['firstday']
        lastday = self.config['lastday']
        for filename, features in self.config['files'].iteritems():
            dayoffset = features['dayoffset']
            for path, name in features['datasets'].iteritems():
                explorer = Explorer(filename, path)

                # Extract the data set for each day of the time series
                # as a separate feature.
                for day in range(firstday, lastday + 1):
                    data = explorer.extract_slice(day + dayoffset)
                    datadict["{0}.{1}".format(name, day)] = data

        df = pd.DataFrame(datadict)
        df.to_csv(self.config['outfile'], index=False)


if __name__ == '__main__':
    main()
