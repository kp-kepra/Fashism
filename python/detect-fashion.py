import caffe, os, sys
import cv2
from fast_rcnn.test import im_detect
caffe.set_mode_gpu()

class Fashism:
    def __init__(self, model="fashion_detector.prototxt", weights="fashion_detector.caffemodel"):
        
        self.model = model
        self.weights = weights
        self.classes = ('upper', 'lower', 'full')

        self.net = caffe.net(model, weights, caffe.TEST)


    def detect(self, image):
        im = cv2.imread(im_file)
        scores, boxes = im_detect(self.net, im)
        return (scores, boxes)

