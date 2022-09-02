from tools import otsu, parse, thresholding
import numpy as np
from imutils import resize
import matplotlib
import matplotlib.pyplot as plt
import cv2 as cv
import argparse

matplotlib.use('TKAgg')

PATH = "images/otsu/{}"
parser = argparse.ArgumentParser()
parser.add_argument('--filepath', '-f',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--block_size', '-w',  default=(3, 3),
                    type=parse.tuple_type, help=parse.HELP_WINDOW)
parser.add_argument('--resize_width', '-rsz',  default=400,
                    type=int, help=parse.HELP_RSZ)
parser.add_argument('--save_filename', '-svf',  default=None,
                    type=str, help=parse.HELP_SAVE)


matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    image = cv.imread(args.filepath, 0)
    image = resize(image, args.resize_width)
    otsu_image = otsu.otsu(image, args.block_size)
    filename = args.save_filename
    if not args.save_filename:
        filename = "{}_otsu_block_{}x{}.png"
        filename = filename.format(
            args.filepath.split("/")[-1].split(".")[0],
            args.block_size[0], args.block_size[1]
        )
    cv.imwrite(PATH.format(filename), otsu_image)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(otsu_image, cmap='gray')
    plt.show()