from comparator import Comparator
import argparse
import cv2

args = argparse.ArgumentParser()
args.add_argument("--db", default="db.csv", help="path to db file")
args.add_argument("--input", required=True, help="path to the input image")
args.add_argument("--images", default="images", help="path to images folder")
args = vars(args.parse_args())

comparator = Comparator(args["db"])
results = comparator.compare(args["input"])

for (score, idx) in results:
    result = cv2.imread(args["images"] + "/" + idx)
    cv2.imshow(idx + ".png" + " score:" + str(score), result)
    cv2.waitKey(0)
