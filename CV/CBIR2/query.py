from imageDescriptor import ImageDescriptor
from searcher import Searcher
import argparse
import cv2

args = argparse.ArgumentParser()
args.add_argument("--db", default="db.csv", help="Path to index file")
args.add_argument("--input", required=True, help="Path to the query image")
args.add_argument("--images", default="images", help="Path to result")
args = vars(args.parse_args())

descriptor = ImageDescriptor((8, 12, 3))

query = cv2.imread(args["input"])
features = descriptor.describe(query)

searcher = Searcher(args["db"])
results = searcher.search(features)

cv2.imshow("Target Image", query)

for (score, ID) in results:
    result = cv2.imread(args["images"] + "/" + ID)
    cv2.imshow(ID + ".png" + " score: " + str(score), result)
    cv2.waitKey(0)
