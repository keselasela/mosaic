from PIL import Image
import math
import subprocess
import random

def make_mosaic_art(source_directory="source/",
                    tile_num = (100,100),
                    interval = 1,
                    target_size = 5):

    target_image = Image.open(source_directory + "target.jpg")
    target_image = target_image.resize(math.floor(i*target_size) for i in target_image.size)
    tile_list = make_tile_list(target_image, tile_num)
    print("tile_list生成")
    color_list = make_color_list(tile_list, target_image)
    print("color_list生成")
    matelial_size = tuple(math.floor(i/j) for i, j in zip(target_image.size, tile_num))
    resized_matelial_list = make_matelial_list(source_directory, matelial_size)
    print("matelial_list生成")
    matelial_color_list = make_matelial_color_list(resized_matelial_list, interval)
    retouched_list = make_retouched_list(color_list, resized_matelial_list, matelial_color_list)
    print("retouched_list生成")
    
    mosaic_art = paste_matelials(target_image, retouched_list, tile_list)
    mosaic_art.save("mosaic_art.jpg")


def paste_matelials(target_image, retouched_list, tile_list):
    for set in zip(tile_list, retouched_list):
        target_image.paste(set[1], set[0][:2])
    return target_image

def culculate_color_average(matelial, interval):
    '''
    与えられた画像のRGB平均を返します
    インターバルが大きいほど平均の求め方が荒くなります
    '''
    n=0
    color_sum=(0,0,0)
    
    for y in range(0, matelial.size[1], interval):
        for x in range(0, matelial.size[0], interval):
            pixel_color = matelial.getpixel((x,y))
            color_sum= tuple(i+j for i,j in zip(color_sum, pixel_color))
            n=n+1
    color_average = tuple(math.floor(i/n) for i in color_sum)
    return color_average

def make_matelial_color_list(matelial_list, interval):
    matelial_color_list = []
    for i in matelial_list:
        matelial_color_list.append(culculate_color_average(i, interval))
    return matelial_color_list

def make_color_list(tile_list, image):
    '''
    targetを分割し、リスト化したものであるタイルリストを元に
    それぞれのタイルに対応したRGBを格納したリストを返します
    '''
    color_list = []
    for i in tile_list:
        central_color_of_tile = image.getpixel((math.floor((i[2] + i[0]) / 2) , math.floor((i[3] + i[1])/ 2) ))
        
        color_list.append(central_color_of_tile)
    return color_list
    
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

def make_tile_color_list(tile_list, image):
    '''
    targetを分割し、リスト化したものであるタイルリストを元に
    それぞれのタイルに対応したRGBを格納したリストを返します
    '''
    tile_color_list = []
    for i in tile_list:
        central_color_of_tile = image.getpixel((math.floor((i[2] + i[0]) / 2) , math.floor((i[3] + i[1])/ 2) ))
        print(central_color_of_tile)
        tile_color_list.append(central_color_of_tile)
    return tile_color_list
    
def retouch_image(image, average, color):
    difference = tuple(i-j for i,j in zip(color, average))
    r,g,b = image.split()
    r = r.point(lambda x : x+difference[0] if 0 <= x+difference[0] and x+difference[0] <=255 else 0 if x+difference[0]<0 else 255)
    g = g.point(lambda x : x+difference[1] if 0 <= x+difference[1] and x+difference[1] <=255 else 0 if x+difference[1]<0 else 255)
    b = b.point(lambda x : x+difference[2] if 0 <= x+difference[2] and x+difference[2] <=255 else 0 if x+difference[2]<0 else 255)
    return Image.merge("RGB", (r,g,b))

def make_matelial_list(source_directory, matelial_size):

    resource=subprocess.run(["ls",source_directory],stdout=subprocess.PIPE)
    resource = resource.stdout.decode().split("\n")
    resource = resource[:len(resource)-1]
    resized_matelial_list = [Image.open(source_directory+i).resize(matelial_size) for i in resource]
    return resized_matelial_list

def make_retouched_list(color_list, matelial_list, matelial_color_list):
    retouched_list = []
    for i in color_list:
        matelial = random.choice(list(zip(matelial_list, matelial_color_list)))
        matelial = retouch_image(matelial[0], matelial[1], i)
        retouched_list.append(matelial)
    return retouched_list

if __name__ == "__main__":
    print("start")
    make_mosaic_art()

