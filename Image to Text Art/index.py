from PIL import Image, ImageOps
import sys, math

img = Image.open(r"image.png") # Image to be used path
elements = " .:cx0@" # Elements to be used; from least dense to most dense
charLength = int(sys.argv[2]) # Get the characters length of art from second command line argument

if(int(sys.argv[1])==0): # Get if the background is dark or light from first command line argument
    elements = elements[::-1] # Reverse the elements string if background is light

smolimg = img.resize((charLength,charLength)) # Resizing image to make it small
greypix = ImageOps.grayscale(smolimg) # Turning image into greyscale
pix_val_grey = list(greypix.getdata())

# greypix.show() # Use this to see the grey and small image that will be used

width, height = smolimg.size # Getting height and width of the resized image
pex = [[0 for x in range(width)] for y in range(height)] # Declaring a 2D Array
definition = len(elements) # Get the number of elements being used for future step of normalization

count = 0 # Used to traverse the pix_val_grey array 
for x in range(height):
    for y in range(width):
        pex[x][y] = elements[math.floor((pix_val_grey[count]/255)*definition)] # Picking the element at index of the normalized value
        count += 1
    print(*pex[x], sep="") # Printing the art into terminal