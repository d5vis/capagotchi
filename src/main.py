from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont
import time
import os

def main():
    epd = epd2in13_V4.EPD()
    epd.init()

    epd.Clear(0xFF)

    base_path = os.path.dirname(os.path.abspath(__file__))

    class_of = Image.open(os.path.join(base_path, 'class_of.png')).convert('1')
    class_of = class_of.resize((epd.height, epd.width), Image.ANTIALIAS)
    class_of = class_of.rotate(180)
    epd.display(epd.getbuffer(class_of))

    time.sleep(2)

    twenty_twenty_five = Image.open(os.path.join(base_path, '2025.png')).convert('1')
    twenty_twenty_five = twenty_twenty_five.resize((epd.height, epd.width), Image.ANTIALIAS)
    twenty_twenty_five = twenty_twenty_five.rotate(180)
    epd.display(epd.getbuffer(twenty_twenty_five))

    time.sleep(2)

    mfotw = Image.open(os.path.join(base_path, 'mfotw.png')).convert('1')
    mfotw = mfotw.resize((epd.height, epd.width), Image.ANTIALIAS)
    mfotw = mfotw.rotate(180)
    epd.display(epd.getbuffer(mfotw))

    time.sleep(2)

    dav_daw = Image.open(os.path.join(base_path, 'dav_daw.png')).convert('1')
    dav_daw = dav_daw.resize((epd.height, epd.width), Image.ANTIALIAS)
    dav_daw = dav_daw.rotate(180)
    epd.display(epd.getbuffer(dav_daw))

    time.sleep(2)

    epd.Clear(0xFF)
    epd.sleep()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()
    finally:
        epd2in13_V4.epdconfig.module_exit()
