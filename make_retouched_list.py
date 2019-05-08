from get_color_from_tile import get_color_from_tile
from make_matelials_list import make_matelils_list
from retouch_image import retouch_image
from culcurate_color_average import culcurate_color_average
def make_retouched_list(color_list, matelials_list):
    retouched_list = []
    for i in color_list:
        matelial = random.choice(matelials_list)
        color_average = culcurate_color_average(matelial)
        retouche_image(i,culcurate_ )


if __name__ == "__main__":
    matelials_list = make_matelials_list()
