from ast import arg
import matplotlib.pyplot as plt
from tools import filters
from tools import parse
from tools import conv
from imutils import resize
import numpy as np
import matplotlib
import cv2 as cv
import argparse

PATH = "images/sobel/{}"
parser = argparse.ArgumentParser()
parser.add_argument('--filepath', '-f',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--strides', '-s',  default=(1, 1),
                    type=parse.tuple_type, help=parse.HELP_STRIDES)
parser.add_argument('--window_size', '-w',  default=(3, 3),
                    type=parse.tuple_type, help=parse.HELP_WINDOW)
parser.add_argument('--resize_width', '-rsz',  default=200,
                    type=int, help=parse.HELP_RSZ)
parser.add_argument('--sigma', '-sig',  default=1.,
                    type=float, help=parse.HELP_SIGMA)
parser.add_argument('--padding', '-p',  default='same', type=str,
                    choices=['same', 'valid'], help=parse.HELP_PADDING)
parser.add_argument('--save_filename', '-svf',  default=None,
                    type=str, help=parse.HELP_SAVE)

matplotlib.use('TKAgg')

kernel_gx = filters.sobel_gx().reshape(3, 3, 1)
kernel_gy = filters.sobel_gy().reshape(3, 3, 1)

def prewiit_prod(window, kernel):
    conv_gx = conv.conv_filter_and_window(window, kernel_gx)
    conv_gy = conv.conv_filter_and_window(window, kernel_gy)
    return np.sqrt(conv_gx ** 2 + conv_gy ** 2)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.window_size[0] > 3 or args.window_size[1] > 3:
        print("Só é possível efetuar operações com filtros 3x3 para os casos: laplaciano, prewitt e sobel")
    image = cv.imread(args.filepath, 0)
    image = resize(image, args.resize_width)
    sobel_img = conv.conv2d(
        img=image, kernel=kernel_gx, strides=args.strides,
        padding=args.padding, prod_function=prewiit_prod
    )[:, :, 0]
    sobel_img = abs(sobel_img)
    filename = args.save_filename
    if not args.save_filename:
        filename = "{}_sobel_{}x{}.png"
        filename = filename.format(
            args.filepath.split("/")[-1].split(".")[0],
            kernel_gx.shape[0], kernel_gx.shape[1]
        )
    cv.imwrite(PATH.format(filename), sobel_img)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(sobel_img, cmap='gray')
    plt.show()