import numpy as np
import csv
from descriptor import ImageDescriptor
import cv2


class Comparator:
    def __init__(self, db_file, limit=10):
        self.db = db_file
        self.limit = limit

    def compare(self, target_file):
        # initialize dict
        results = {}
        descriptor = ImageDescriptor((8, 12, 3))
        target_image = cv2.imread(target_file)
        target_feature = descriptor.describe(target_image)
        with open(self.db) as f:
            reader = csv.reader(f)
            for row in reader:
                features = [float(x) for x in row[1:]]
                dist = self.chi2_dist(features, target_feature)
                results[row[0]] = dist
            f.close()

        results = sorted([v, k] for (k, v) in results.iteritems())
        cv2.imshow("Target Image", target_image)
        return [(v, k) for (v, k) in results[:self.limit] if v <= 7]

    def chi2_dist(self, feat1, feat2, eps=1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(feat1, feat2)])
        return d
