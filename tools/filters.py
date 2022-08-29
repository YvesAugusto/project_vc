import numpy as np
import cv2 as cv
def mean_filter(size: tuple = (3, 3)):
    return (1 / (size[0] * size[1])) * np.ones(size)

def gaussian(l=5, sig=1.):
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

def prewitt_gx():
    return np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])

def prewitt_gy():
    return np.array([
        [1 ,  1,  1],
        [0 ,  0,  0],
        [-1, -1, -1]
    ])

def sobel_gx():
    return np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

def sobel_gy():
    return np.array([
        [1 ,  2,  1],
        [0 ,  0,  0],
        [-1, -2, -1]
    ])

# def laplacian():
#     return np.array([
#         [1, 1,  1],
#         [1, -8, 1],
#         [1, 1,  1]
#     ])

def laplacian():
    return np.array([
        [0, 1,  0],
        [1, -4, 1],
        [0, 1,  0]
    ])

if __name__ == '__main__':
    img = gaussian(100, 4.0)
    cv.imwrite('./images/gaussian_filter.png', img)