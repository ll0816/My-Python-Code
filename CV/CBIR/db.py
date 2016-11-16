import argparse
import cv2
import glob

from descriptor import ImageDescriptor

'''
create features database for images
'''
args = argparse.ArgumentParser()
args.add_argument("--images", default="images", help="path to the images folder")
args.add_argument("--db", default="db.csv", help="path to the database")
args = vars(args.parse_args())

descriptor = ImageDescriptor((8, 12, 3))
db = open(args["db"], "w")

for image_path in glob.glob(args["images"] + "/*.png"):
    name = image_path[image_path.rfind("/") + 1:]
    image = cv2.imread(image_path)
    features = descriptor.describe(image)
    features = [str(f) for f in features]
    db.write("%s,%s\n" % (name, ",".join(features)))

db.close()
