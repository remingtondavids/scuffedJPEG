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

for i in range(rows):  # Nested loop implementation of the DCT
    for j in range(cols):
        DCTCoefficients[i][j] = 0
        CCoverFour = (getC(i)*getC(j))/4
        for x in range(8):
            for y in range(8):
                DCTSum += YChannelShifted[i][j]*math.cos((math.pi*(2*x+1)*(i+0.5))/16)*math.cos((math.pi*(2*y+1)*(j+0.5))/16)
        DCTCoefficients[i][j] = round(CCoverFour*DCTSum, 1)

Quantized = [[0 for x in range(cols)] for y in range(rows)]

Q50 = [[16, 11, 10, 16, 24, 40, 51, 61], # Quantization matrix for quality 50
       [12, 12, 14, 19, 26, 58, 60, 55],
       [14, 13, 16, 24, 40, 57, 69, 56],
       [14, 17, 22, 29, 51, 87, 80, 62],
       [18, 22, 37, 56, 68, 109, 103, 77],
       [24, 35, 55, 64, 81, 104, 113, 92],
       [49, 64, 78, 87, 103, 121, 120, 101],
       [72, 92, 95, 98, 112, 100, 103, 99]]

for i in range(rows):
    for j in range(cols):
        Quantized[i][j] = round(DCTCoefficients[i][j]/Q50[i][j])


# print('Ychannel: \n')
# print(np.matrix(YChannel))
# print('YchannelShifted: \n')
# print(np.matrix(YChannelShifted))
# print('DCTCoefficients: \n')
# print(np.matrix(DCTCoefficients))
# print('Q50: \n')
# print(np.matrix(Q50))
# print('Quantized: \n')
# print(np.matrix(Quantized))

# plt.style.use('_mpl-gallery-nogrid')

# fig, ax = plt.subplots()

# ax.imshow(np.matrix(DCTCoefficients), cmap='gray')

# plt.show()

def listQuantized(list): # arrange matrix of DCT coefficients into a list
    output = []

    i = 0
    j = 0



    while not ((i == 7) & (j == 7)):

        
        if ((i == 0) | (j == 0) | (i == 7) | (j == 7)): # when on an edge

            if (i == 0): # top edge
                if (j % 2 == 0):
                    output.append(list[i][j])
                    j += 1
                else:
                    output.append(list[i][j])
                    i += 1
                    j -= 1

            if (i == 7): # bottom edge              
                if (j % 2 == 0):
                    output.append(list[i][j])
                    j += 1
                else:
                    output.append(list[i][j])
                    i -= 1
                    j += 1

            if (j == 0): # left edge
                if (i % 2 == 0):
                    output.append(list[i][j])
                    i -= 1
                    j += 1
                else:
                    output.append(list[i][j])
                    i += 1
            
            if (j == 7): # right edge
                if ((i == 7) & (j == 7)):
                    output.append(list[i][j])
                    return output

                elif (i % 2 == 0):
                    output.append(list[i][j])
                    i += 1
                    j -= 1
                else:
                    output.append(list[i][j])
                    i += 1
        
        else: # when not on an edge

            if(((i % 2 == 0) & (j % 2 == 0)) | ((i % 2 != 0) & (j % 2 != 0))):
                output.append(list[i][j])
                i -= 1
                j += 1
            
            else:
                output.append(list[i][j])
                i += 1
                j -= 1

    


outputArr = listQuantized(Quantized);

print(outputArr)



# expected arr : [-8, -11, 1, -3, -1, -1, -6, -3, -4, -1, -2, -2, -4, -1, -2, -1, 0, -2, -1, -2, -1, -1, -1, -1, -1, ]



            


        


        


    






