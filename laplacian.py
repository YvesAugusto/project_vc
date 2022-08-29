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

PATH = "images/laplacian/{}"
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
    if args.window_size[0] > 3 or args.window_size[1] > 3:
        print("Só é possível efetuar operações com filtros 3x3 para os casos: laplaciano, prewitt e sobel")
    kernel_gx = filters.laplacian().reshape(3, 3, 1)
    image = cv.imread(args.filepath, 0)
    image = resize(image, args.resize_width)
    laplacian_img = conv.conv2d(
        img=image, kernel=kernel_gx, strides=args.strides,
        padding=args.padding
    )[:, :, 0]
    laplacian_img = abs(laplacian_img).clip(0, 255)
    filename = args.save_filename
    if not args.save_filename:
        filename = "{}_laplacian_{}x{}.png"
        filename = filename.format(
            args.filepath.split("/")[-1].split(".")[0],
            kernel_gx.shape[0], kernel_gx.shape[1]
        )
    cv.imwrite(PATH.format(filename), laplacian_img)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(laplacian_img, cmap='gray')
    plt.show()