from values import *
from image import *
from draw import *

def main():

    pix_str, im = convert_im(image)
    set_up()
    row = draw_grid(im)
    print('1234567890')
    draw_pixels(pix_str, im, row)


main()
