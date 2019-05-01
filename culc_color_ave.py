def culc_color_ave(image, interval):
    n=0
    pixel_average=(0,0,0)
    for y in range(0, image.size[1], interval):
        for x in range(0, image.size[2], interval):
            pixel_color = image.getpixel((x,y))
            pixel_average = (i+j for i,j in zip(pixel_average, pixel_color))
            n++
    pixel_average = (fmath.floor(i/n) for i in pixel_average)
    return pixel_average

if __name__=="main":
    