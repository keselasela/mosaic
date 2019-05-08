from make_tile_list import make_tile_list
from PIL import Image 
import math


def make_color_list(tile_list, image):
    '''
    targetを分割し、リスト化したものであるタイルリストを元に
    それぞれのタイルに対応したRGBを格納したリストを返します
    '''
    color_list = []
    for i in tile_list:
        central_color_of_tile = image.getpixel((math.floor((i[2] + i[0]) / 2) , math.floor((i[3] + i[1])/ 2) ))
        print(central_color_of_tile)
        color_list.append(central_color_of_tile)
    return color_list
    
if __name__=="__main__":
    
    img = Image.open( "img_0.jpg" )
    tile_list = make_tile_list(img)
    get_color_from_tile(tile_list, img)
    #print(get_color_from_tile(tile_list, img))
