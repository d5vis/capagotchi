from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont
import time

def main():
    epd = epd2in13_V4.EPD()
    epd.init()

    epd.Clear(0xFF)

    image1 = Image.open('/home/pi/class_of.png').convert('1')
    image1 = image1.resize((epd.width, epd.height), Image.ANTIALIAS)
    image1 = image1.rotate(180)
    epd.display(epd.getbuffer(image1))

    time.sleep(2)

    image2 = Image.open('/home/pi/2025.png').convert('1')
    image2 = image2.resize((epd.width, epd.height), Image.ANTIALIAS)
    image2 = image2.rotate(180)
    epd.display(epd.getbuffer(image2))

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
