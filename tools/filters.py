import numpy as np
import cv2 as cv
def mean_filter(size: tuple = (3, 3)):
    return (1 / (size[0] * size[1])) * np.ones(size)

def gaussian(l=5, sig=1.):
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

if __name__ == '__main__':
    img = gaussian(100, 4.0)
    cv.imwrite('./images/gaussian_filter.png', img)