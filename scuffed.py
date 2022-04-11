from PIL import Image;

im = Image.open('test.png') # Opens the image
im = im.convert('YCbCr')    # Converts the image to YCbCr

pix = im.load() # Loads the pixel data into a 2D list of tuples with the form : (Y, Cb, Cr)

rows, cols = im.size    # Gets the size of the image

YChannel = [[0 for x in range(cols)] for y in range(rows)] # Creates a 2D array for our Y channel

for i in range(rows):   # Iterates through the pixel data and adds the Y channel to the array
    for j in range(cols):
        YChannel[i][j] = pix[i,j][0]



# now for the DCT o_o






        






