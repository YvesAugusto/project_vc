import matplotlib.pyplot as plt
from imutils import resize
import numpy as np
import matplotlib
import cv2 as cv
import argparse
import os
from tools import filters
from tools import parse
from tools import conv

PATH = "images/gauss/{}"
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

if __name__ == '__main__':
    args = parser.parse_args()
    image = cv.imread(args.filepath, 0)
    image = resize(image, args.resize_width)
    kernel = filters.gaussian(args.window_size[0], args.sigma)
    gaussian = conv.conv2d(
        img=image, kernel=kernel, strides=args.strides,
        padding=args.padding,
    )[:,:,0]
    filename = args.save_filename
    if not args.save_filename:
        filename = "{}_gauss_sigma_{}_{}x{}.png"
        filename = filename.format(
            args.filepath.split("/")[-1].split(".")[0],
            args.sigma, kernel.shape[0], kernel.shape[1]
        )
    cv.imwrite(PATH.format(filename), gaussian)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(gaussian, cmap='gray')
    plt.show()