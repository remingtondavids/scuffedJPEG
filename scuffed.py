from cmath import pi
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt



im = Image.open('test.png') # Opens the image
im = im.convert('YCbCr')    # Converts the image to YCbCr

pix = im.load() # Loads the pixel data into a 2D list of tuples with the form : (Y, Cb, Cr)

rows, cols = im.size    # Gets the size of the image

YChannel = [[0 for x in range(cols)] for y in range(rows)] # Creates a 2D array for our Y channel

for i in range(rows):   # Iterates through the pixel data and adds the Y channel to the array
    for j in range(cols):
        YChannel[i][j] = pix[j,i][0]







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

Quantized = [[0 for x in range(cols)] for y in range(rows)]

Q50 = [[16, 11, 10, 16, 24, 40, 51, 61],
       [12, 12, 14, 19, 26, 58, 60, 55],
       [14, 13, 16, 24, 40, 57, 69, 56],
       [14, 17, 22, 29, 51, 87, 80, 62],
       [18, 22, 37, 56, 68, 109, 103, 77],
       [24, 35, 55, 64, 81, 104, 113, 92],
       [49, 64, 78, 87, 103, 121, 120, 101],
       [72, 92, 95, 98, 112, 100, 103, 99]]





Quantized = [[round(DCTCoefficients[i][j]/Q50[i][j]) for i in range(cols)] for j in range(rows)]








# print("Y channel(shifted): \n")
                
# for i in range(rows):
#     for j in range(cols):
#         print(YChannelShifted[i][j], end = " ")

#     print("\n")

# print("DCT results: \n")

# for i in range(rows):
#     for j in range(cols):
#         print(DCTCoefficients[i][j], end = " ")

#     print("\n")

# print("Quantized coefficients: \n")

# for i in range(rows):
#     for j in range(cols):
#         print(Quantized[j][i], end = " ")

#     print("\n")

# print(np.matrix(YChannelShifted))

# print("\n")

# print(np.matrix(DCTCoefficients))

# print("\n")

# print(np.matrix(Quantized))

print(np.matrix(YChannel))

plt.style.use('_mpl-gallery-nogrid')

fig, ax = plt.subplots()

ax.imshow(np.matrix(YChannel), cmap='gray')

plt.show()








