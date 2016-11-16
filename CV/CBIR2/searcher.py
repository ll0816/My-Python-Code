import numpy as np
import csv

class Searcher:
    def __init__(self, indexPath):
        self.indexPath = indexPath

    def search(self, queryFeatures, limit = 10):
        # initialize dict
        results = {}

        with open(self.indexPath) as f:
            reader = csv.reader(f)

            for row in reader:
                features = [float(x) for x in row[1:]]
                dist = self.chi2_dist(features, queryFeatures)
                results[row[0]] = dist
            f.close()

        results = sorted([v, k] for (k, v) in results.iteritems())
        return [(v, k) for (v, k) in results[:limit] if v < 7]

    def chi2_dist(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
        return d