from PIL import Image


# ( length, value )

def convert_im(image):
    #opens the image
    im = Image.open(image, 'r')

    #Converts the image to pure black and white
    im = im.convert('1')

     #A str to hold the ones and zeroes
    pix_str = ''
    pix_val = list(im.getdata())

    compressed_tuples = []

    i = 0
    line_length = im.size[0]
    l = 0

    while i < len(pix_val):
        run_length = 0
        value = pix_val[i]
        while True:
            run_length += 1
            i += 1
            l += 1
            if l >= line_length or i >= len(pix_val) or value != pix_val[i]:
                break

        compressed_tuples.append((run_length, value))

        if l >= line_length:
            l = 0


    #Converts the 255 for black to 1
    for n, i in enumerate(pix_val):
        if i == 255:
            pix_val[n] = 1

    #Puts the values into a str
    for pix in pix_val:
        pix_str += str(pix)

    return pix_val, im
