from PIL import Image;
import math

im = Image.open('test.png') # Opens the image
im = im.convert('YCbCr')    # Converts the image to YCbCr

pix = im.load() # Loads the pixel data into a 2D list of tuples with the form : (Y, Cb, Cr)

rows, cols = im.size    # Gets the size of the image

YChannel = [[0 for x in range(cols)] for y in range(rows)] # Creates a 2D array for our Y channel

for i in range(rows):   # Iterates through the pixel data and adds the Y channel to the array
    for j in range(cols):
        YChannel[i][j] = pix[i,j][0]



# now for the DCT o_o

YChannelShifted = [[0 for x in range(cols)] for y in range(rows)]

for i in range(rows):
    for j in range(cols):
        YChannelShifted[i][j] = YChannel[i][j] - 128

DCTCoefficients = [[0 for x in range(cols)] for y in range(rows)]


def getC(x):
    if x == 0:
        return 1/math.sqrt(2)
    else:
        return 1

DCTSum = 0

CCoverFour = 0 

for i in range(rows):
    for j in range(cols):
        DCTCoefficients[i][j] = 0
        CCoverFour = (getC(i)*getC(j))/4
        for x in range(8):
            for y in range(8):
                DCTSum += YChannelShifted[i][j]*math.cos((math.pi*(2*x+1)*(i+0.5))/16)*math.cos((math.pi*(2*y+1)*(j+0.5))/16)
        DCTCoefficients[i][j] = round(CCoverFour*DCTSum, 1)
                
for i in range(rows):
    for j in range(cols):
        print(YChannelShifted[j][i], end = " ")

    print("\n")


for i in range(rows):
    for j in range(cols):
        print(DCTCoefficients[j][i], end = " ")

    print("\n")






        






