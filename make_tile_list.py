
from PIL import Image
import math
def make_tile_list(target_image, tile_num=(100,100) ):
    '''
    targetを分割し、そのリストを返します
    tile_numは分割数であり、第一引数がｘ軸方向、第二引数がｙ軸方向
    '''
    x_tile_num = tile_num[0]
    y_tile_num = tile_num[1]
    x_target_size = target_image.size[0]
    y_target_size = target_image.size[1]
    tile_list = []
    for y in range(0, y_tile_num):
        for x in range(0, x_tile_num):
            tile = (x*x_target_size/x_tile_num, y*y_target_size/y_tile_num,
            (x+1)*x_target_size/x_tile_num, (y+1)*y_target_size/y_tile_num )
            tile = tuple(math.floor(i) for i in tile)
            tile_list.append(tile)
    return tile_list

if __name__ == "__main__":
    img = Image.open( "img_0.jpg" )
    print(make_tile_list(img))