#!/usr/bin/env python
import numpy as np
import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score

def main():
    args = parse_args()
    modeler = Modeler(args)
    modeler.evaluate()

def parse_args():
    description = 'train microwave swe -> reconstructed swe model'
    parser = ArgumentParser(description=description)
    parser.add_argument('infile', help='location of csv file')
    return parser.parse_args()

class Modeler(object):

    def __init__(self, args):
        data = pd.read_csv(args.infile)
        data.dropna(inplace=True)
        target = 'recon_swe_mean'
        self.X = data[[col for col in data.columns if col != target]]
        self.y = data[target]

    def evaluate(self):
        model = self.get_model()
        scores = cross_val_score( model, self.X, self.y)
        model.fit(self.X, self.y)
        print "coefficients:"
        print model.intercept_
        print model.coef_
        print "R^2 CV scores:"
        print scores

    @staticmethod
    def get_model():
        return LinearRegression(normalize=True)


if __name__ == '__main__':
    main()
