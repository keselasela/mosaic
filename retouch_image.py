from PIL import Image
def retouch_image(image, average, color):
    difference = tuple(i-j for i,j in zip(color, average))
    r,g,b = image.split()
    r = r.point(lambda x : x+difference[0] if 0 <= x+difference[0] and x+difference[0] <=255 else 0 if x+difference[0] else 255)
    g = g.point(lambda x : x+difference[1] if 0 <= x+difference[1] and x+difference[1] <=255 else 0 if x+difference[1] else 255)
    b = b.point(lambda x : x+difference[2] if 0 <= x+difference[2] and x+difference[2] <=255 else 0 if x+difference[2] else 255)
    return Image.merge("RGB", (r,g,b))
if __name__=="__main__":
    
    image = Image.open( "img_0.jpg" )
    retouch_image(image, (50,50,40), (60,60,60)).show()
    
    
    
