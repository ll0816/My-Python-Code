from imageDescriptor import ImageDescriptor
import argparse, glob, cv2

'''
create features for images as images
'''
args = argparse.ArgumentParser()
args.add_argument("--images", default="images", help="Path to the images dir")
args.add_argument("--db", default="db.csv", help="Path to the database file")
args = vars(args.parse_args())

desciptor = ImageDescriptor((8, 12, 3))
output = open(args["db"], "w")

for imagePath in glob.glob(args["images"] + "/*.png"):
    ID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    features = desciptor.describe(image)
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (ID, ",".join(features)))

output.close()
