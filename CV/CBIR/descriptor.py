import numpy as np
import cv2


class ImageDescriptor:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        # get dimensions
        (h, w) = image_HSV.shape[:2]

        # get image center
        (top_x, top_y) = (int(h * 0.33), int(w * 0.33))
        (bot_x, bot_y) = (int(h * 0.67), int(w * 0.67))

        # divide image into 9 parts
        segments = [(0, top_x, 0, top_y), (top_x, bot_x, 0, top_y), (bot_x, w, 0, top_y), (0, top_x, top_y, bot_y),
                    (top_x, bot_x, top_y, bot_y), (bot_x, w, top_y, bot_y), (0, top_x, bot_y, h),
                    (top_x, bot_x, bot_y, h), (bot_x, w, bot_y, h)]

        for (start_x, end_x, start_y, end_y) in segments:
            mask = np.zeros(image_HSV.shape[:2], dtype="uint8")
            # cv2.rectangle(img, (pt1), (pt2), color, thickness)
            mask = cv2.rectangle(mask, (start_x, start_y), (end_x, end_y), 255, -1)
            features.extend(self.histogram(image_HSV, mask))
        return features

    def histogram(self, img_matrix, mask):
        # cv2.clcHist([images], [channels], mask, [hist sizes], [ranges])
        hist = cv2.calcHist([img_matrix], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])
        # normalization, show percentage
        hist = cv2.normalize(hist, hist).flatten()
        return hist
