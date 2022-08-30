import argparse
from tools import thresholding, parse
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import cv2 as cv

PATH = "images/threshold/{}"
parser = argparse.ArgumentParser()
parser.add_argument('--filepath', '-f',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--limiares', '-l', nargs='+',
                    type=parse.tuple_type, default=[(0, 127), (127, 255)])
parser.add_argument('--valores', '-v', nargs='+', default=[0, 255],
                    type=int)

matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    image = cv.imread(args.filepath, 0)
    if len(args.valores) != len(args.limiares):
        print("O número de pares de limiares({}) deve ser igual ao número de valores({})".format(
            len(args.valores), len(args.limiares)
        ))
        exit(1)
    thresholded_image = thresholding.threshold_image(image, args.limiares, args.valores)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(thresholded_image, cmap='gray')
    plt.show()