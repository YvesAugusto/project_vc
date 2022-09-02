from tools import adaptive, parse
import numpy as np
from imutils import resize
import matplotlib
import matplotlib.pyplot as plt
import cv2 as cv
import argparse

matplotlib.use('TKAgg')

PATH = "images/adaptive/{}"
function_map = {
    'threshold_mean': adaptive.threshold_mean,
    'threshold_median': adaptive.threshold_median
}
parser = argparse.ArgumentParser()
parser.add_argument('--filepath', '-f',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--block_size', '-w',  default=(3, 3),
                    type=parse.tuple_type, help=parse.HELP_WINDOW)
parser.add_argument('--function', '-fc',  default='threshold_mean',
                    type=str, help=parse.HELP_FUNCTION, choices=function_map.keys())
parser.add_argument('--resize_width', '-rsz',  default=400,
                    type=int, help=parse.HELP_RSZ)
parser.add_argument('--save_filename', '-svf',  default=None,
                    type=str, help=parse.HELP_SAVE)


matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    image = cv.imread(args.filepath, 0)
    image = resize(image, args.resize_width)
    adaptive_thresh = adaptive.adaptive_threshold(image, args.block_size, function_map[args.function])
    filename = args.save_filename
    if not args.save_filename:
        filename = "{}_adaptive_block_{}x{}.png"
        filename = filename.format(
            args.filepath.split("/")[-1].split(".")[0],
            args.block_size[0], args.block_size[1]
        )
    cv.imwrite(PATH.format(filename), adaptive_thresh)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(adaptive_thresh, cmap='gray')
    plt.show()