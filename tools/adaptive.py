import numpy as np

def split_image_into_blocks(img: np.ndarray, block_size: tuple):
    steps_on_y = int(img.shape[0] / block_size[0]) + 1
    steps_on_x = int(img.shape[1] / block_size[1]) + 1
    block_info = []
    for y in range(steps_on_y):
        for x in range(steps_on_x):
            block = {
                'start_y': y * block_size[0], 'end_y': (y + 1) * block_size[0],
                'start_x': x * block_size[1], 'end_x': (x + 1) * block_size[1]
            }
            block_info.append(block)
    return block_info
    
def threshold_mean(block):
    mean = block.mean()
    cp = block.copy()
    cp[block >= mean] = 255
    cp[block < mean] = 0
    return cp

def threshold_median(block):
    mean = np.median(block)
    cp = block.copy()
    cp[block >= mean] = 255
    cp[block < mean] = 0
    return cp

def adaptive_threshold(img: np.ndarray, block_size: tuple, threshold_function=threshold_mean):
    block_info = split_image_into_blocks(img, block_size)
    cp = img.copy()
    for info in block_info:
        (start_y, end_y, start_x, end_x) = info['start_y'], info['end_y'], info['start_x'], info['end_x']
        cp[start_y: end_y, start_x: end_x] = threshold_function(
            cp[start_y: end_y, start_x: end_x]
        )
    return cp


if __name__ == '__main__':
    img = np.arange(13*13).reshape(13, 13)
    t_img = adaptive_threshold(img, (3,3), threshold_median)
    print(t_img)