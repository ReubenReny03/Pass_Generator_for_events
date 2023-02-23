from PIL import Image, ImageFont, ImageDraw
import pyqrcode
import png
from pyqrcode import QRCode
import qrcode
from PIL import Image

def make_qr_and_add(list_of_urk):
    for names in list_of_urk:
        Logo_link = 'khacks.png'

        logo = Image.open(Logo_link)
        
        # taking base width
        basewidth = 100
        
        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
    # taking url or text
        # adding URL or text to QRcode
        QRcode.add_data(names)
        # generating QR code
        QRcode.make()
        # taking color name from user
        QRcolor = 'Black'
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        QRimg.save(f'all_qr/qr{names}.png')

        im2 = Image.open(f'all_qr/qr{names}.png')
        my_image.paste(im2,(900, 0))
        my_image.save(f"all_pass/Pass_{names}.jpg")
    print(f"Made {len(list_of_urk)} Passes Successfully")

my_image = Image.open("base.jpg")
title_font = ImageFont.truetype('Stars&Love-BottomHeavy.ttf', 100)
title_text = input("Title:")
image_editable = ImageDraw.Draw(my_image)
image_editable.text((50,15), title_text, (0, 0, 0), font=title_font)
title_font = ImageFont.truetype('Barlow-Bold.ttf', 50)
date = input("Date: ")
time = input("Time: ")
venue = input("Venue: ")
title_text = (f"Date: {date}\nTime: {time}\nVenue: {venue}")
image_editable.text((50,200), title_text, (0, 0, 0), font=title_font)
list_of_people = ["URK21CS1024","URK21CS1002","URK21CS1004","URK21CS1041"]
make_qr_and_add(list_of_people)

