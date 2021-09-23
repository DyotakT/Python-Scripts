from PIL import Image, ImageOps
import sys

img = Image.open(r"image.png")

darkBackground = sys.argv[1]

smolimg = img.resize((50,50)) # Resizing image to make it small
greypix = ImageOps.grayscale(smolimg) # Turning image into greyscale
pix_val_grey = list(greypix.getdata())

# greypix.show() # Use this to see the grey and small image that will be used

width, height = smolimg.size

pex = [[0 for x in range(width)] for y in range(height)] 

count = 0 # To Count 
heightcount = 0
for x in range(height):
    for y in range(width):
        pex[x][y]=pix_val_grey[count]
        if(darkBackground==1):
            if(pex[x][y]>204):
                pex[x][y]=" "
            elif(pex[x][y]>153 and pex[x][y]<205):
                pex[x][y]="."
            elif(pex[x][y]>102 and pex[x][y]<154):
                pex[x][y]="x"
            elif(pex[x][y]>51 and pex[x][y]<103):
                pex[x][y]="0"
            elif(pex[x][y]<52):
                pex[x][y]="@"
        else:
            if(pex[x][y]>204):
                pex[x][y]="@"
            elif(pex[x][y]>53 and pex[x][y]<205):
                pex[x][y]="0"
            elif(pex[x][y]>102 and pex[x][y]<154):
                pex[x][y]="x"
            elif(pex[x][y]>51 and pex[x][y]<103):
                pex[x][y]="."
            elif(pex[x][y]<52):
                pex[x][y]=" "
        count=count+1
    heightcount=heightcount+1

for x in range(height):
    print(*pex[x], sep="") # Printing the art into terminal