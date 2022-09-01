# project_vc
Primeiro Trabalho da disciplina de Visão Computacional

## 1. Clone this repository
``` shell
> git@github.com:YvesAugusto/project_vc.git
```
## 2. Install poetry: 
``` shell
> pip install poetry
```
## 3. Activate virtual environment and install dependencies:
``` shell
> poetry shell
> poetry install
```
## Run some examples - low-pass filters
Lets run mean filter on a (3x3) kernel with a (2, 2) strides step, using the default padding. 
``` shell
> python3 media.py --filepath images/brad.jpg --window_size 3,3 --strides (2,2) --padding "same"
```
Lets run median filter on a (5x5) kernel with a (1, 1) strides step, using the default padding. 
``` shell
> python3 mediana.py --filepath images/brad.jpg --window_size 5,5 --strides (1,1) --padding "same"
```
Lets run gaussian filter on a (5x5) kernel with σ = 1.5, using the default padding. 
``` shell
> python3 mediana.py --filepath images/brad.jpg --window_size 5,5 --sigma 1.5
```
## Run some examples - high-pass filters
Lets run prewitt, sobel and laplacian filters on brad pitt image
``` shell
> python3 prewitt.py --filepath images/brad.jpg
> python3 sobel.py --filepath images/brad.jpg
> python3 laplaciano.py --filepath images/brad.jpg
```
## Run some examples - histogram and histogram equalization
Show histogram using 30 bins
``` shell
> python3 show_histogram.py --filepath images/test.jpg --bins 30
```
Equalize image histogram with 50 bins
``` shell
> python3 equalize.py --filepath images/test.jpg --bins 50
```
## Run some examples - multi-thresholding
Set pixels between 0 and 50 to 0, pixels between 50 and 160 to 127 and those ones between 160 and 255 to 255
``` shell
> python3 threshold.py --filepath images/lena.png --limiares 0,50 50,160 160,255 --valores 0 127 255
```
