import copy
import cv2 as cv
import numpy as np
from PIL.Image import Image
from matplotlib import pyplot as plt

from umbcrawling import ImageToNumberArray, Hough, Mosaic, Canny, Haar, Mosaics, CTX

def MosaicLambda(*params):
    cmd = params[0]
    target = params[1]
    if cmd == 'IMAGE_READ_FOR_CV':
        return (lambda x: cv.imread(CTX+x))(target)
    elif cmd == 'IMAGE_READ_FOR_PLT':
        return cv.cvtColor((lambda x: cv.imread(CTX+x))(target), cv.COLOR_BGR2RGB)
    elif cmd == 'GRAY_SCALE':
        return (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(target)
    elif cmd == 'IMAGE_FROM_ARRAY':
        return (lambda x: Image.fromarray(x))(target)

class MosaicControll(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        cv.imshow('원본', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        arr = ImageToNumberArray(params[1])
        img = MosaicLambda('GRAY_SCALE', arr)
        img = MosaicLambda('IMAGE_FROM_ARRAY', img)
        plt.imshow(img)
        plt.show()

    @staticmethod
    def menu_3(*params):
        img = ImageToNumberArray(params[1])
        img_canny = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_canny, cmap='gray')
        plt.title('CANNY'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        img_canny = cv.Canny(img, 100, 200)  # (image, threshold 1=100, threshold 2=200)
        img_hough = Hough(img_canny)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_hough, cmap='gray')
        plt.title('hough'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        img_cat = cv.imread(CTX+params[1])
        img_mosaic = Mosaic(img_cat, (150, 150, 450, 450), 10)
        cv.imwrite(CTX +'cat-mosaic.png', img_mosaic)
        cv.imshow('CAT MOSAIC', img_mosaic)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        girl = params[1]
        img = MosaicLambda('IMAGE_READ_FOR_PLT', girl)

        gray = MosaicLambda("GRAY_SCALE", img)

        img_canny = Canny(img)
        img_hough = Hough(img_canny)
        img_clone = copy.deepcopy(img)
        rect = Haar(img_clone)

        img_mosaic = Mosaic(img, rect, 10)

        plt.subplot(161), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(img_canny, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(img_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(img_clone, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(img_mosaic, cmap='gray')
        plt.title('mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_7(*params):
        print(params[0])
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_mosaic = Mosaics(img, 10)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_mosaic, cmap='gray')
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()
