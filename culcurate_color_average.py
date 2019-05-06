
from PIL import Image 
import math


def culculate_color_average(image, interval=1):
    '''
    与えられた画像のRGB平均を返します
    インターバルが大きいほど平均の求め方が荒くなります
    '''
    n=0
    pixel_average=(0,0,0)
    
    for y in range(0, image.size[1], interval):
        for x in range(0, image.size[0], interval):
            pixel_color = image.getpixel((x,y))
            pixel_average = tuple(i+j for i,j in zip(pixel_average, pixel_color))
            n=n+1
    pixel_average = tuple(math.floor(i/n) for i in pixel_average)
    return pixel_average


if __name__=="__main__":
    #print(culculate_color_average.__doc__)
    img = Image.open( "img_0.jpg" )
    print(culculate_color_average(img, 1))
