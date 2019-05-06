from make_tile_list import make_tile_list
from PIL import Image 
import math

def get_color_from_tile(tile_list, image):
    tile_color_list = []
    for i in tile_list:
        central_color_of_tile = image.getpixel((math.floor((i[2] + i[0]) / 2) , math.floor((i[3] + i[1])/ 2) ))
        print(central_color_of_tile)
        tile_color_list.append(central_color_of_tile)
    return tile_color_list
if __name__=="__main__":
    
    img = Image.open( "img_0.jpg" )
    tile_list = make_tile_list(img)
    get_color_from_tile(tile_list, img)
    #print(get_color_from_tile(tile_list, img))
