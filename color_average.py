from PIL import Image 
import math

def culc_color_ave(image, interval=1):
    n=0
    
    pixel_average=(0,0,0)
    
    for y in range(0, image.size[1], interval):
        for x in range(0, image.size[0], interval):
        
            pixel_color = image.getpixel((x,y))
            pixel_average = tuple(i+j for i,j in zip(pixel_average, pixel_color))
            n=n+1
    pixel_average = (math.floor(i/n) for i in pixel_average)
    return tuple(pixel_average)


if __name__=="__main__":
    
    img = Image.open( "img_0.jpg" )
    print(culc_color_ave(img, 1))