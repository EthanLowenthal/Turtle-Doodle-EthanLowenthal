from PIL import Image

def convert_im(image):
    #opens the image
    im = Image.open(image, 'r')

    #Converts the image to pure black and white
    im = im.convert('1')

     #A str to hold the ones and zeroes
    pix_str = ''
    pix_val = list(im.getdata())

    #Converts the 255 for black to 1
    for n, i in enumerate(pix_val):
        if i == 255:
            pix_val[n] = 1

    #Puts the values into a str
    for pix in pix_val:
        pix_str += str(pix)

    return pix_val, im
