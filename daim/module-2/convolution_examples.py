from PIL import Image, ImageFilter
import numpy as np

im = Image.open("./cat_2.png").convert("L")  

kern_sharp = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
], dtype=float)

kern_blur = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=float)

kern_edge = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2 ,1]
], dtype=float)

filter_sharp = ImageFilter.Kernel((3, 3), kern_sharp.flatten(), 1, 0)
filter_blur  = ImageFilter.Kernel((3, 3), kern_blur.flatten(), 16, 0)
filter_edge  = ImageFilter.Kernel((3, 3), kern_edge.flatten(), 1, 0)

blurred_img = im.filter(filter_sharp)
blurred_img.show()